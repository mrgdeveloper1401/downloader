# Generated by Django 4.2.5 on 2023-09-26 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0004_alter_cardhomemodel_format_linksciol_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CardHomeModel',
            new_name='ResolotionSciolModel',
        ),
        migrations.AlterModelOptions(
            name='resolotionsciolmodel',
            options={'verbose_name': 'ResolotionSciol', 'verbose_name_plural': 'ResolotionSciols'},
        ),
        migrations.AlterModelTable(
            name='resolotionsciolmodel',
            table='ResolotionSciol',
        ),
    ]