# Generated by Django 2.2.4 on 2019-08-10 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviez', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviemodel',
            name='description',
            field=models.CharField(max_length=120),
        ),
    ]
