# Generated by Django 2.2.1 on 2019-10-27 09:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapi', '0003_auto_20191020_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='user',
            field=models.ForeignKey(blank=True, default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]