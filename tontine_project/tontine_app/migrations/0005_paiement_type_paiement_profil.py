# Generated by Django 4.2.4 on 2024-04-02 13:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tontine_app', '0004_remove_paiement_type_paiement_delete_profil'),
    ]

    operations = [
        migrations.AddField(
            model_name='paiement',
            name='type_paiement',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('utilisateur', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
