from django.db import models
from django.utils.html import format_html


class Merch(models.Model):
    """Модель для хранения позиций мерча"""
    name = models.CharField(
        verbose_name='Название',
        max_length=256,
        null=False,
        blank=False
    )
    price = models.DecimalField(
        verbose_name='Цена',
        max_digits=10,
        null=False,
        blank=False,
        decimal_places=0
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True
    )
    availability = models.BooleanField(
        verbose_name='Наличие',
        blank=False,
        default=True,
        null=False
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'merch'
        verbose_name = 'Мерч'
        verbose_name_plural = 'Мерч'


class MerchGallery(models.Model):
    """Модель для хранения фото мерча"""
    image = models.ImageField(
        verbose_name='Фото',
        blank=False,
        null=False,
        upload_to='merch_gallery'
    )
    is_main = models.BooleanField(
        verbose_name='Главное изображение',
        default=False,
        blank=False
    )
    merch = models.ForeignKey(
        to=Merch,
        on_delete=models.CASCADE,
        related_name='images'
    )

    def __str__(self):
        return self.merch.name

    def image_tag(self):
        return format_html(
            f'<img src="{self.image.url}" style="max-width:300px; '
            f'max-height:300px"/>')

    class Meta:
        db_table = 'merch_photos'
        verbose_name = 'Фото мерча'
        verbose_name_plural = 'Фото мерча'
