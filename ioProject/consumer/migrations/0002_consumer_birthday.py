# Generated by Django 2.2.3 on 2019-09-03 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumer',
            name='BirthDay',
            field=models.DateField(blank=True, default=None),
        ),
    ]
