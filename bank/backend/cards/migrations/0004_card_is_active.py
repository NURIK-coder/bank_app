# Generated by Django 5.1.2 on 2024-10-21 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_alter_card_card_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Is active'),
        ),
    ]
