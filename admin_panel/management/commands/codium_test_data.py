"""This module adds command to manage.py commands to flush the database and fill it with test data"""
from django.core.management import call_command
from django.core.management.base import BaseCommand
from admin_panel.management.commands._test_data import load_test_data


class Command(BaseCommand):
    help = 'Flushes the database and fills it with test data'

    def handle(self, *args, **options):
        call_command('flush')
        load_test_data(self.stdout)
