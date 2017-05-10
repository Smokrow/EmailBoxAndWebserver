# -*- coding: utf-8 -*-

from EmailBoxAndWebserverApp.functions import Email_string_abrufen,Database_bereinigen
from django.core.management.base import BaseCommand,CommandError

class Command(BaseCommand):
    help = "Lädt die Emails"

    def handle(self, *args, **options):
        Email_string_abrufen()
        Database_bereinigen()
