# Generated by Django 2.2.7 on 2019-11-07 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_thumb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumb',
            field=models.ImageField(blank=True, default='default.png', upload_to='images/'),
        ),
    ]
