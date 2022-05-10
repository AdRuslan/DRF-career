from django.core.management.base import BaseCommand
from api.models import Vacancy


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        vacancies = Vacancy.objects.all()
        for vac in vacancies:
            vac.hidden = False
            vac.save()
