# Generated by Django 3.2.7 on 2021-09-16 12:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_rename_title_jobdetails_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientdetails',
            name='state',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]