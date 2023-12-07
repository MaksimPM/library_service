from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    author = models.CharField(max_length=100, verbose_name='автор')
    publication = models.DateField(verbose_name='дата публикации', **NULLABLE)
    ISBN = models.CharField(max_length=150, verbose_name='ISBN')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'
        ordering = ('pk',)
