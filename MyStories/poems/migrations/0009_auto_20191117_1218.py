# Generated by Django 2.2.7 on 2019-11-17 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poems', '0008_auto_20191117_1217'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-publish',)},
        ),
    ]
