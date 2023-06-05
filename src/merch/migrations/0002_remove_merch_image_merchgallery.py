# Generated by Django 4.2.1 on 2023-06-05 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('merch', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='merch',
            name='image',
        ),
        migrations.CreateModel(
            name='MerchGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='merch_gallery', verbose_name='Фото')),
                ('is_main', models.BooleanField(default=False, verbose_name='Главное изображение')),
                ('merch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='merch.merch')),
            ],
            options={
                'verbose_name': 'Фото мерча',
                'verbose_name_plural': 'Фото мерча',
                'db_table': 'merch_photos',
            },
        ),
    ]
