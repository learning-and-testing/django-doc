# Generated by Django 3.0.2 on 2020-01-22 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pladform', '0003_subscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pladform.Author', verbose_name='Пользователь'),
        ),
    ]
