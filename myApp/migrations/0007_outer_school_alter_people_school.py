# Generated by Django 4.1 on 2022-09-05 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0006_people_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='outer',
            name='school',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='school',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
