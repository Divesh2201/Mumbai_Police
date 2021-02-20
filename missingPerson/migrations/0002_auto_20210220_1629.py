# Generated by Django 3.1.6 on 2021-02-20 10:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('missingPerson', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='missingpersoninfo',
            name='admin_status',
            field=models.CharField(choices=[('under scrutiny', 'Under Scrutiny'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='null', max_length=50),
        ),
        migrations.AlterField(
            model_name='missingpersoninfo',
            name='image',
            field=models.ImageField(default='default.png', upload_to='missing_person_pics'),
        ),
        migrations.AlterField(
            model_name='missingpersoninfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]