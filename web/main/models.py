from django.db import models


class News(models.Model):
    title = models.CharField('Название', max_length=100)
    text = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
