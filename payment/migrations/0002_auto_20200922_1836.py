# Generated by Django 3.1.1 on 2020-09-22 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderlineitem',
            old_name='product',
            new_name='item',
        ),
        migrations.RemoveField(
            model_name='orderlineitem',
            name='product_size',
        ),
    ]