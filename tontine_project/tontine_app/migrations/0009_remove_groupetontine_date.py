# Generated by Django 4.2.4 on 2024-04-02 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tontine_app', '0008_groupetontine_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupetontine',
            name='date',
        ),
    ]
