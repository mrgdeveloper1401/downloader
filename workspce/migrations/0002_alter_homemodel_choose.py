# Generated by Django 4.2.5 on 2023-09-26 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspce', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homemodel',
            name='choose',
            field=models.CharField(choices=[('instagram', 'Instagram'), ('facebook', 'Facebook'), ('twitter', 'Twitter')], max_length=9, verbose_name='scoil'),
        ),
    ]
