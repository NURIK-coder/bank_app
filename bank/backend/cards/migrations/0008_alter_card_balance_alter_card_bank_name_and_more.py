# Generated by Django 5.1.2 on 2024-10-22 13:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0007_alter_card_balance'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='balance',
            field=models.BigIntegerField(blank=True, default=0, verbose_name='Balance'),
        ),
        migrations.AlterField(
            model_name='card',
            name='bank_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Bank name'),
        ),
        migrations.AlterField(
            model_name='card',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
