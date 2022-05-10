from rest_framework.serializers import ModelSerializer

from .models import Vacancy, Employer, Finder

class FinderSerializer(ModelSerializer):
    class Meta:
        model = Finder
        exclude = ['user']

class EmployerSerializer(ModelSerializer):
    class Meta:
        model = Employer
        exclude = ['user']

class VacancySerializer(ModelSerializer):
    employer_info = EmployerSerializer(source='employer')
    class Meta:
        model = Vacancy
        exclude = ['employer']