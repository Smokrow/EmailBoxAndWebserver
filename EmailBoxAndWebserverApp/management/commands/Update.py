# -*- coding: utf-8 -*-

from EmailBoxAndWebserverApp.functions import Email_string_abrufen,Database_bereinigen
from django.core.management.base import BaseCommand,CommandError

class Command(BaseCommand):
    help = "Lädt die Emails"
    #das schätzchen hier wird über einen Cronjob aufgerufen und Ruft emails ab. Gleichzeitig bereinigt es die Datenbank, wenn eine Email zulange auf der Box ist und löscht sier aus der Datenbank
    def handle(self, *args, **options):
        Email_string_abrufen()
        Database_bereinigen()
