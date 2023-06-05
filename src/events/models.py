from django.db import models
from django.utils.html import format_html


class Events(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=512,
        null=False,
        blank=False
    )
    description = models.TextField(
        verbose_name='Описание',
        null=True,
        blank=False
    )
    start_date = models.DateField(
        verbose_name='Дата начала',
        max_length=128,
        null=False,
        blank=False,
        auto_now=False
    )
    end_date = models.DateField(
        verbose_name='Дата окончания',
        max_length=128,
        null=True,
        blank=True,
        auto_now=False
    )
    poster = models.ImageField(
        verbose_name='Постер',
        upload_to='media/posters/',
        blank=True,
        null=True
    )
    tickets_link = models.CharField(
        verbose_name='Ссылка на покупку билетов',
        max_length=512,
        null=True,
        blank=True
    )
    vk_link = models.CharField(
        verbose_name='Ссылка на встречу ВК',
        max_length=512,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.name} - {str(self.start_date)}'

    def image_tag(self):
        return format_html(
            f'<img src="{self.poster.url}" style="max-width:300px; '
            f'max-height:300px"/>')

    class Meta:
        db_table = 'events'
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'
