from django.db import models


class Record(models.Model):
    title = models.CharField('Название', max_length=255)
    text = models.TextField('Текст')
    pub_date = models.DateTimeField('Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
