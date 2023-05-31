from django.db import models


class Events(models.Model):
    name = models.CharField('Название', max_length=512, null=False, blank=False)
    start_date = models.DateField('Дата начала', max_length=128, null=False, blank=False, auto_now=False)
    end_date = models.DateField('Дата окончания', max_length=128, null=True, blank=True, auto_now=False)
    poster = models.ImageField('Постер', upload_to='media/posters/', blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {str(self.start_date)}'

    class Meta:
        db_table = 'events'
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'
