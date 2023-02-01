from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Resume(models.Model):
    class Status(models.IntegerChoices):
        created = 1, 'Создано, подготовлено к публикации'
        is_published = 2, 'Опубликовано'
        archived = 3, 'В архиве'

    class Grade(models.TextChoices):
        intern = 'intern', 'Intern'
        junior = 'junior', 'Junior'
        middle = 'middle', 'Middle'
        senior = 'senior', 'Senior'
        lead = 'lead', 'Lead'

    class Education(models.TextChoices):
        secondary = 'secondary', 'Среднее общее'
        secondary_special = 'secondary_special', 'Среднее специальное'
        incomplete_higher = 'incomplete_higher', 'Неоконченное высшее'
        higher = 'higher', 'Высшее'

    class Specialty(models.TextChoices):
        frontend = 'frontend', 'Фронтенд'
        backend = 'backend', 'Бэкенд'
        gamedev = 'gamedev', 'Геймдев'
        devops = 'devops', 'Девопс'
        design = 'design', 'Дизайн'
        products = 'products', 'Продукты'
        management = 'management', 'Менеджмент'
        testing = 'testing', 'Тестирование'

    status = models.PositiveSmallIntegerField(
        verbose_name='Статус резюме',
        choices=Status.choices,
        default=Status.created
    )
    grade = models.CharField(
        verbose_name='Уровень',
        max_length=6,
        choices=Grade.choices,
        default=Grade.intern
    )
    specialty = models.CharField(
        verbose_name='Специализация',
        max_length=10,
        choices=Specialty.choices,
        default=Specialty.backend
    )
    education = models.CharField(
        verbose_name='Образование',
        max_length=18,
        choices=Education.choices,
        default=Education.secondary
    )
    experience = models.TextField(
        verbose_name='Опыт работы'
    )
    portfolio = models.URLField(
        verbose_name="Ссылка на портфолио (GitHub или иные ресурсы)"
    )
    title = models.CharField(
        max_length=50,
        verbose_name='Название резюме',
    )
    phone = PhoneNumberField(
        verbose_name='Номер для связи'
    )
    email = models.EmailField(
        verbose_name='Email для связи'
    )
    owner = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='Владелец резюме',
    )

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'

    def __str__(self):
        return self.title
