from django.db import models


class Merch(models.Model):
    name = models.CharField('Название', max_length=256, null=False, blank=False)
    price = models.DecimalField('Цена', max_digits=10, null=False, blank=False, decimal_places=0)
    description = models.TextField('Описание', blank=True, null=True)
    image = models.ImageField('Фото', blank=False, null=False, upload_to='merch')  # TODO: расширить до нескольких фото
    availability = models.BooleanField('Наличие', blank=False, default=True, null=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'merch'
        verbose_name = 'Мерч'
        verbose_name_plural = 'Мерч'
