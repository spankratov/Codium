from django.db.models.signals import post_save, pre_delete, post_delete, m2m_changed
from django.dispatch import receiver
from django.contrib.auth.models import User
from content.models import Attribute, Property, University, Project, Job, Knowledge
from userdata.models import Character, AttributeLevels, CharacterProperties, CharacterUniversities, CharacterProjects, \
    CharacterJobs, KnowledgeLevels


@receiver(post_save, sender=Attribute, dispatch_uid="attribute_post_save_uid")
def attribute_post_save(sender, **kwargs):
    """Add new attribute to each character."""
    if kwargs['created']:
        attribute = kwargs['instance']
        for character in Character.objects.all():
            AttributeLevels.objects.create(character=character, attribute=attribute, level=attribute.default)


@receiver(pre_delete, sender=Attribute, dispatch_uid="attribute_pre_delete_uid")
def attribute_pre_delete(sender, **kwargs):
    """Delete attribute from each character."""
    attribute = kwargs['instance']
    AttributeLevels.objects.filter(attribute=attribute).delete()


@receiver(pre_delete, sender=Property, dispatch_uid="property_pre_delete_uid")
def property_pre_delete(sender, **kwargs):
    """Delete property from characters."""
    property_instance = kwargs['instance']
    CharacterProperties.objects.filter(property=property_instance).delete()


@receiver(pre_delete, sender=University, dispatch_uid="university_pre_delete_uid")
def university_pre_delete(sender, **kwargs):
    """Delete university from characters."""
    university = kwargs['instance']
    CharacterUniversities.objects.filter(university=university).delete()


@receiver(pre_delete, sender=Project, dispatch_uid="project_pre_delete_uid")
def project_pre_delete(sender, **kwargs):
    """Delete project from characters."""
    project = kwargs['project']
    CharacterProjects.objects.filter(project=project).delete()


@receiver(pre_delete, sender=Job, dispatch_uid="job_pre_delete_uid")
def job_pre_delete(sender, **kwargs):
    """Delete job from characters."""
    job = kwargs['instance']
    CharacterJobs.objects.filter(job=job).delete()


@receiver(post_save, sender=KnowledgeLevels, dispatch_uid="knowledgelevels_post_save_uid")
def knowledgelevels_post_save(sender, **kwargs):
    """If knowledge level for this character is changed, level of parents of this knowledge should be recalculated."""
    if not kwargs['created']:
        kwargs['instance'].calculate_parents_level()


@receiver(post_save, sender=Knowledge, dispatch_uid="knowledge_post_save_uid")
def knowledge_post_save(sender, **kwargs):
    """If knowledge is created, then its levels should be added to each character and calculated.
    If knowledge is changed somehow, then its level for each character should be recalculated."""
    knowledge = kwargs['instance']
    if kwargs['created']:
        for character in Character.objects.all():
            knowledgelevel = KnowledgeLevels.objects.create(character=character, knowledge=knowledge)
            knowledgelevel.calculate_level()
    else:
        for knowledgelevel in KnowledgeLevels.objects.filter(knowledge=knowledge):
            knowledgelevel.calculate_level()


@receiver(pre_delete, sender=Knowledge, dispatch_uid="knowledge_pre_delete_uid")
def knowledge_pre_delete(sender, **kwargs):
    """Delete knowledge from characters."""
    knowledge = kwargs['instance']
    KnowledgeLevels.objects.filter(knowledge=knowledge).delete()


@receiver(post_delete, sender=Knowledge, dispatch_uid="knowledge_post_delete_uid")
def knowledge_post_delete(sender, **kwargs):
    """After knowledge is deleted, its previous parents levels should be recalculated."""
    knowledge = kwargs['instance']
    for knowledgelevel in KnowledgeLevels.objects.filter(knowledge__id=knowledge.id):
        knowledgelevel.calculate_parents_level()


@receiver(m2m_changed, sender=Knowledge.children.through, dispatch_uid="knowledge_m2m_changed_uid")
def knowledge_m2m_changed(sender, **kwargs):
    """Recalculating knowledge levels if hierarchy is changed."""
    knowledge = kwargs['instance']
    action = kwargs['action']
    reverse = kwargs['reverse']
    if action == "post_add" or action == "post_remove":
        if reverse:
            for knowledgelevel in KnowledgeLevels.objects.filter(knowledge__id__in=kwargs['pk_set']):
                knowledgelevel.calculate_level()
        else:
            for knowledgelevel in KnowledgeLevels.objects.filter(knowledge=knowledge):
                knowledgelevel.calculate_level()
    elif action == "pre_clear":
        if reverse:
            knowledge._old_m2m = knowledge.parents.values_list('pk', flat=True)
    elif action == "post_clear":
        if reverse:
            for knowledgelevel in KnowledgeLevels.objects.filter(knowledge__id__in=knowledge._old_m2m):
                knowledgelevel.calculate_level()


@receiver(post_save, sender=User, dispatch_uid="user_post_save_uid")
def user_post_save(sender, **kwargs):
    """Create character for each non-admin user."""
    user = kwargs['instance']
    if kwargs['created'] and not user.is_staff:
        Character.objects.create(user=user)


@receiver(post_save, sender=Character, dispatch_uid="character_post_save_uid")
def character_post_save(sender, **kwargs):
    """Create attribute and knowledge levels for new character."""
    character = kwargs['instance']
    if kwargs['created']:
        for attribute in Attribute.objects.all():
            AttributeLevels.objects.create(character=character, attribute=attribute, level=attribute.default)
        for knowledge in Knowledge.objects.all():
            KnowledgeLevels.objects.create(character=character, knowledge=knowledge, level=0)


@receiver(pre_delete, sender=Character, dispatch_uid="character_pre_delete_uid")
def character_pre_delete(sender, **kwargs):
    """Delete all character information before its removal."""
    character = kwargs['instance']
    AttributeLevels.objects.filter(character=character).delete()
    CharacterJobs.objects.filter(character=character).delete()
    CharacterProjects.objects.filter(character=character).delete()
    CharacterProperties.objects.filter(character=character).delete()
    CharacterUniversities.objects.filter(character=character).delete()
    KnowledgeLevels.objects.filter(character=character).delete()
