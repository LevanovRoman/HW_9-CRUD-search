from django.db import models
from django.urls import reverse


class RestaurantModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    specialization = models.CharField(max_length=50, verbose_name='Специализация')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    site = models.CharField(max_length=50, verbose_name='Сайт')
    phone = models.CharField(max_length=20, verbose_name='Телефон')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ресторан'
        verbose_name_plural = 'Рестораны'

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

