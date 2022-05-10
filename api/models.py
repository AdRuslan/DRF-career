from django.db import models
from authentication.models import User
from simple_history.models import HistoricalRecords


class Finder(models.Model):
    user = models.OneToOneField(User, verbose_name='User', on_delete=models.CASCADE)
    first_name = models.CharField(verbose_name='Имя', max_length=255)
    last_name = models.CharField(verbose_name='Фамилия', max_length=255)
    cv = models.FileField(verbose_name='Резюме', upload_to='users/cv', max_length=100)
    photo = models.ImageField(verbose_name='Фото', upload_to='users/photos')
    about = models.TextField(verbose_name='О себе')

    history = HistoricalRecords()

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Соискатель'
        verbose_name_plural = 'Соискатели'


class Employer(models.Model):
    user = models.OneToOneField(User, verbose_name='User', on_delete=models.CASCADE)
    company_name = models.CharField(verbose_name='Название компании', max_length=255)
    employees_count = models.PositiveIntegerField(verbose_name='Количество работников')
    about = models.TextField(verbose_name='О компании')

    history = HistoricalRecords()

    def __str__(self):
        return str(self.company_name)

    class Meta:
        verbose_name = 'Работодатель'
        verbose_name_plural = 'Работодатели'


class Vacancy(models.Model):
    XP_CHOICES = (('NO', 'Без опыта'), ('1', '1 год'), ('3', '3 года'), )
    employer = models.ForeignKey(Employer, verbose_name='Работодатель', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Заголовок', max_length=255)
    description = models.TextField(verbose_name='О компании')
    required_xp = models.CharField(verbose_name='Необходимый опыт', choices=XP_CHOICES, max_length=255, default='NO')
    hidden = models.BooleanField(verbose_name='Скрыт?', default=True)

    history = HistoricalRecords()

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
