# Generated by Django 3.0.6 on 2020-05-10 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('prints', '0006_auto_20200508_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='print',
            name='designer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
