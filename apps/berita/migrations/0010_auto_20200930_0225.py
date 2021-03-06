# Generated by Django 3.1.1 on 2020-09-29 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('berita', '0009_berita_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='berita',
            old_name='is_featured',
            new_name='active',
        ),
        migrations.AddField(
            model_name='berita',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='berita',
            name='tags',
            field=models.ManyToManyField(null=True, to='berita.Tag'),
        ),
    ]
