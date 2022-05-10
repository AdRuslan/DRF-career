from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import EmployersViewSet, FinderViewSet, VacancyViewSet, GetVacanciesWithoutXPListAPIView
from authentication.views import AuthenticationViewSet

router = DefaultRouter()
router.register('vacancy', VacancyViewSet)
router.register('employer', EmployersViewSet)
router.register('finder', FinderViewSet)
router.register('auth', AuthenticationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/vacancies/no-xp/', GetVacanciesWithoutXPListAPIView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)


# def trigger_error(request):
#     division_by_zero = 1 / 0

# urlpatterns += [
#     path('sentry-debug/', trigger_error),
# ]
