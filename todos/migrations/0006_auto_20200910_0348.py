# Generated by Django 3.1.1 on 2020-09-10 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0005_todo_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='labels',
            field=models.ManyToManyField(blank=True, related_name='labels', to='todos.Label'),
        ),
    ]