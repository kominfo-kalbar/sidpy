# Generated by Django 3.1.1 on 2020-09-14 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site_conf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conf', models.SlugField(max_length=255)),
                ('conf_val', models.TextField(blank=True, null=True)),
                ('title', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True, null=True)),
                ('is_load', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Web Config',
            },
        ),
    ]