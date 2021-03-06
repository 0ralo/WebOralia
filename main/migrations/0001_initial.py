# Generated by Django 3.1.7 on 2021-02-26 16:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Содержимое')),
                ('is_visible', models.BooleanField(default=False, verbose_name='Показывается')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Посты',
                'verbose_name_plural': 'Пост',
            },
        ),
    ]
