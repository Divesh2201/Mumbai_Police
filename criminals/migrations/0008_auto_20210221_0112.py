# Generated by Django 3.1.6 on 2021-02-20 19:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('criminals', '0007_auto_20210220_1756'),
    ]

    operations = [
        migrations.RenameField(
            model_name='criminalsinfo',
            old_name='address',
            new_name='height',
        ),
        migrations.RemoveField(
            model_name='criminalsinfo',
            name='datetime',
        ),
        migrations.RemoveField(
            model_name='criminalsinfo',
            name='pincode',
        ),
        migrations.AddField(
            model_name='criminalsinfo',
            name='date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
