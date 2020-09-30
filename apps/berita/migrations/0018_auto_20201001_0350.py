# Generated by Django 3.1.1 on 2020-09-30 20:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('berita', '0017_auto_20200930_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='berita',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='thumb'),
        ),
    ]