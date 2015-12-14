from django.contrib.auth.models import User
from content.models import *
from userdata.models import *
import userdata.signals


def load_test_data(output):
    # Attributes creation
    Attribute.objects.language('ru').create(name='Здоровье', short_name='hlth', default=100, min_value=0, max_value=100)
    Attribute.objects.language('ru').create(name='Энергия', short_name='nrg', default=50, min_value=0, max_value=100)
    Attribute.objects.language('ru').create(name='Мотивация', short_name='mot', default=50, min_value=0, max_value=100)
    Attribute.objects.language('ru').create(name='Деньги', short_name='money', default=1000, min_value=0)
    output.write('Successfully created attributes')

    # Events creation
    Event.objects.language('ru').create(name='Первая работа',
                                        description='Вы получили первую работу. Можете немного поесть',
                                        short_name='fstjob', affects='money', requirements='skills', chance=50.0)
    Event.objects.language('ru').create(name='Гениальный стартап',
                                        description='Ваш стартап обогнал Apple по капитализации',
                                        short_name='bststartup', affects='everything', requirements='luck', chance=0.1)
    output.write('Successfully created events')

    # Actions creation
    Action.objects.language('ru').create(name='Прогуляться',
                                         description='С вами это случается редко, но вы решили выйти на улицу',
                                         type='rest', short_name='promenade', affects='hlth', requirements='nothing')
    Action.objects.language('ru').create(name='Захватить мир', description='Первый пункт в плане: купить печеньки',
                                         type='important', short_name='cnqrworld', affects='everything',
                                         requirements='luck')
    output.write('Successfully created action')

    # Property creation
    iphone = Property.objects.language('ru').create(name='Айфон', description='Теперь и у вас есть такой', type='phone',
                                                    short_name='iphone', cost=60000)
    audi = Property.objects.language('ru').create(name='Ауди',
                                                  description='Теперь вы можете не только ездить до работы, но и ездить до работы',
                                                  type='car', short_name='audi', cost=100000)
    mcbook = Property.objects.language('ru').create(name='Макбук', description='Think different',
                                                    type='notebook', short_name='mcbook', cost=80000)
    gglinc = Property.objects.language('ru').create(name='Корпорация Гугл', description='Обыденное приобретение',
                                                    type='company',
                                                    short_name='gglinc', cost=666666)
    output.write('Successfully created properties')

    # Universities creation
    spb = University.objects.language('ru').create(name='СПБГУ', description='Можно познакомиться с создателями игры',
                                                   short_name='spb', affects='skills', requirements='skills')
    inn = University.objects.language('ru').create(name='Иннополис', description='Его реклама добралась даже сюда',
                                                   short_name='inn', affects='skills', requirements='skills')
    mit = University.objects.language('ru').create(name='MIT', description='Университет хозяина жизни',
                                                   short_name='mit', affects='everything', requirements='everything')
    output.write('Successfully created universities')

    # Projects creation
    mobgame = Project.objects.language('ru').create(
        description='Вы собираетесь, чтобы создать игру на мобильные устройства... Погодите, рекурсия',
        type='personal_project', short_name='mobgame', affects='skills', requirements='skills',
        time_spending=1000)
    stup = Project.objects.language('ru').create(description='Убийца <подставьте сюда компанию или продукт>',
                                                 type='startup',
                                                 short_name='stup', affects='skills', requirements='skills',
                                                 time_spending=10000)
    opnsrc = Project.objects.language('ru').create(description='Вы решили внести вклад в любимый фреймворк',
                                                   type='open_source',
                                                   short_name='opnsrc', affects='skills', requirements='skills',
                                                   time_spending=10000)
    output.write('Successfully created projects')

    # Jobs creation
    intern = Job.objects.language('ru').create(name='Стажёр',
                                               description='Стрессоустойчивость. Умение разбираться в чужом коде. Опыт - 10 лет. Возраст - не старше 20.',
                                               company_name='Doesnt Matter Inc.', short_name='intern', affects='skills',
                                               requirements='skills')
    snrback = Job.objects.language('ru').create(name='Senior backend-разработчик',
                                                description='Окружающие не понимают, откуда у вас столько денег',
                                                company_name='Instagram', short_name='snrback', affects='skills',
                                                requirements='skills')
    fcbceo = Job.objects.language('ru').create(name='Директор Facebook',
                                               description='Никто не знает, что вы сделали с Цукербергом',
                                               company_name='Facebook', short_name='fcbceo', affects='skills',
                                               requirements='skills')
    output.write('Successfully created jobs')

    # Knowledge creation
    python = Knowledge.objects.language('ru').create(name='Python',
                                                     description='Пришло время создавать виртуальное окружение',
                                                     type='skill', short_name='python', requirements='nothing')
    php = Knowledge.objects.language('ru').create(name='PHP', description='Стандартный выбор',
                                                  type='skill', short_name='php', requirements='nothing')
    ruby = Knowledge.objects.language('ru').create(name='Ruby',
                                                   description='Не забудьте свой макбук и очки в роговой оправе',
                                                   type='skill', short_name='ruby', requirements='nothing')
    backend_langs = Knowledge.objects.language('ru').create(name='Backend languages',
                                                            description='Необязательно знать их все',
                                                            type='one-of-area', short_name='backlangs',
                                                            requirements='nothing')
    backend_langs.children.add(python, php, ruby)
    db_skill = Knowledge.objects.language('ru').create(name='Базы данных', description="Robert'); DROP TABLE students",
                                                       type='skill', short_name='db', requirements='nothing')
    backend = Knowledge.objects.language('ru').create(name='Backend',
                                                      description="Увлекательное путешествие в мир консоли",
                                                      type='area', short_name='back', requirements='nothing')
    backend.children.add(backend_langs, db_skill)
    js = Knowledge.objects.language('ru').create(name='Javascript', description="Без него никуда",
                                                 type='skill', short_name='js', requirements='nothing')
    html = Knowledge.objects.language('ru').create(name='HTML', description="Не язык программирования!!!11",
                                                   type='skill', short_name='html', requirements='nothing')
    css = Knowledge.objects.language('ru').create(name='CSS', description="Язык стилей и боли",
                                                  type='skill', short_name='css', requirements='nothing')
    frontend = Knowledge.objects.language('ru').create(name='Frontend', description="На стыке дизайна",
                                                       type='area', short_name='front', requirements='nothing')
    frontend.children.add(js, html, css)
    fullstack = Knowledge.objects.language('ru').create(name='Web-разработка', description="Fullstack",
                                                        type='area', short_name='flstack', requirements='nothing')
    fullstack.children.add(backend, frontend)
    output.write('Successfully created knowledges')

    # Users creation
    User.objects.create_user(username='junior_player', email='junior_email@gmail.com', password='junior_password')
    User.objects.create_user(username='middle_player', email='middle_email@gmail.com', password='middle_password')
    User.objects.create_user(username='senior_player', email='senior_email@gmail.com', password='senior_password')
    User.objects.create_superuser(username='super_admin', email='super_email@gmail.com', password='super_password')
    junior = Character.objects.get(user__username='junior_player')
    junior.days_lived = 100
    junior.save()
    middle = Character.objects.get(user__username='middle_player')
    middle.days_lived = 1000
    middle.save()
    senior = Character.objects.get(user__username='senior_player')
    senior.days_lived = 10000
    senior.save()
    output.write('Successfully created users, characters and their linkages to attributes and knowledges')

    # AttributeLevels setting
    current_attribute = AttributeLevels.objects.get(character=middle, attribute__short_name='money')
    current_attribute.level = 100000
    current_attribute.save()
    AttributeLevels.objects.get(character=middle, attribute__short_name='mot')
    current_attribute.level = 75
    current_attribute.save()
    current_attribute = AttributeLevels.objects.get(character=middle, attribute__short_name='nrg')
    current_attribute.level = 75
    current_attribute.save()
    current_attribute = AttributeLevels.objects.get(character=senior, attribute__short_name='money')
    current_attribute.level = 1000000
    current_attribute.save()
    current_attribute = AttributeLevels.objects.get(character=senior, attribute__short_name='mot')
    current_attribute.level = 100
    current_attribute.save()
    current_attribute = AttributeLevels.objects.get(character=senior, attribute__short_name='nrg')
    current_attribute.level = 100
    current_attribute.save()
    output.write('Successfully set attribute levels for characters')

    # CharacterProperties creation
    CharacterProperties.objects.create(character=junior, property=iphone, purchase_date=junior.days_lived)
    CharacterProperties.objects.create(character=middle, property=iphone, purchase_date=100)
    CharacterProperties.objects.create(character=middle, property=mcbook, purchase_date=middle.days_lived)
    CharacterProperties.objects.create(character=senior, property=iphone, purchase_date=100)
    CharacterProperties.objects.create(character=senior, property=mcbook, purchase_date=1000)
    CharacterProperties.objects.create(character=senior, property=audi, purchase_date=senior.days_lived)
    CharacterProperties.objects.create(character=senior, property=gglinc, purchase_date=senior.days_lived)
    output.write('Successfully set properties for characters')

    # CharacterUniversities creation
    CharacterUniversities.objects.create(character=junior, university=spb, entering_date=0)
    CharacterUniversities.objects.create(character=middle, university=inn, entering_date=100, finished=True)
    CharacterUniversities.objects.create(character=senior, university=spb, entering_date=0, finished=True)
    CharacterUniversities.objects.create(character=senior, university=mit, entering_date=1000, finished=True)
    output.write('Successfully set universities for characters')

    # CharacterProjects creation
    CharacterProjects.objects.create(character=junior, project=mobgame, name='codium', taking_date=0)
    CharacterProjects.objects.create(character=middle, project=opnsrc, name='Django', taking_date=100)
    CharacterProjects.objects.create(character=senior, project=opnsrc, name='Python', taking_date=100, finished=True)
    CharacterProjects.objects.create(character=senior, project=stup, name='Airbnb', taking_date=1000, finished=True)
    output.write('Successfully set projects for characters')

    # CharacterJobs creation
    CharacterJobs.objects.create(character=junior, job=intern, taking_date=junior.days_lived)
    CharacterJobs.objects.create(character=middle, job=snrback, taking_date=middle.days_lived)
    CharacterJobs.objects.create(character=senior, job=intern, taking_date=100, finished=True)
    CharacterJobs.objects.create(character=senior, job=snrback, taking_date=1000, finished=True)
    CharacterJobs.objects.create(character=senior, job=fcbceo, taking_date=senior.days_lived)
    output.write('Successfully set jobs for characters')

    # KnowledgeLevels setting
    current_knowledge = KnowledgeLevels.objects.get(character=junior, knowledge=python)
    current_knowledge.level = 40
    current_knowledge.save()
    current_knowledge = KnowledgeLevels.objects.get(character=junior, knowledge=db_skill)
    current_knowledge.level = 15
    current_knowledge.save()
    current_knowledge = KnowledgeLevels.objects.get(character=junior, knowledge=js)
    current_knowledge.level = 15
    current_knowledge.save()
    current_knowledge = KnowledgeLevels.objects.get(character=junior, knowledge=html)
    current_knowledge.level = 25
    current_knowledge.save()
    current_knowledge = KnowledgeLevels.objects.get(character=junior, knowledge=css)
    current_knowledge.level = 25
    current_knowledge.save()
    current_knowledge = KnowledgeLevels.objects.get(character=middle, knowledge=python)
    current_knowledge.level = 70
    current_knowledge.save()
    current_knowledge = KnowledgeLevels.objects.get(character=middle, knowledge=db_skill)
    current_knowledge.level = 40
    current_knowledge.save()
    current_knowledge = KnowledgeLevels.objects.get(character=middle, knowledge=js)
    current_knowledge.level = 50
    current_knowledge.save()
    current_knowledge = KnowledgeLevels.objects.get(character=middle, knowledge=html)
    current_knowledge.level = 80
    current_knowledge.save()
    current_knowledge = KnowledgeLevels.objects.get(character=middle, knowledge=css)
    current_knowledge.level = 80
    current_knowledge.save()
    current_knowledge = KnowledgeLevels.objects.get(character=senior, knowledge=python)
    current_knowledge.level = 80
    current_knowledge.save()
    current_knowledge = KnowledgeLevels.objects.get(character=senior, knowledge=ruby)
    current_knowledge.level = 100
    current_knowledge.save()
    current_knowledge = KnowledgeLevels.objects.get(character=senior, knowledge=db_skill)
    current_knowledge.level = 90
    current_knowledge.save()
    current_knowledge = KnowledgeLevels.objects.get(character=senior, knowledge=js)
    current_knowledge.level = 95
    current_knowledge.save()
    current_knowledge = KnowledgeLevels.objects.get(character=senior, knowledge=html)
    current_knowledge.level = 100
    current_knowledge.save()
    current_knowledge = KnowledgeLevels.objects.get(character=senior, knowledge=css)
    current_knowledge.level = 100
    current_knowledge.save()
    output.write('Successfully set knowledge levels for characters')
