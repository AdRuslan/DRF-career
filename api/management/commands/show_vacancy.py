from django.core.management.base import BaseCommand
from api.models import Vacancy

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='Id of vacancy, that must be hidden')

    def handle(self, *args, **kwargs):
        id = kwargs['id']
        try:
            vacancy = Vacancy.objects.get(id=id)
            vacancy.hidden = False
            vacancy.save()
        except Vacancy.DoesNotExist:
            print(f'Vacancy with id {id} does not exist')