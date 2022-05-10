from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.generics import ListAPIView
import django_filters.rest_framework
from .models import Employer, Vacancy, Finder
from .serializers import EmployerSerializer, VacancySerializer, FinderSerializer

class VacancyViewSet(ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

    @action(methods=['GET'], detail=False, url_path='with_xp')
    def get_vacancies_with_xp(self, request):
        data = self.serializer_class(self.queryset.filter(Q(hidden=False), Q(required_xp='1') | Q(required_xp='3')), many=True).data
        return Response(data)

    @action(methods=['POST'], detail=True, url_path='make-visible')
    def make_vacancy_visible(self, request, pk):
        vacancy = Vacancy.objects.get(id=pk)
        vacancy.hidden = False
        vacancy.save()
        return Response(self.serializer_class(vacancy).data)


class EmployersViewSet(ReadOnlyModelViewSet):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer


class FinderViewSet(ReadOnlyModelViewSet):
    queryset = Finder.objects.all()
    serializer_class = FinderSerializer


class GetVacanciesWithoutXPListAPIView(ListAPIView):
    queryset = Vacancy.objects.filter(required_xp='NO', hidden=False)
    serializer_class = VacancySerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name']
