# Generated by Django 3.1.7 on 2021-04-09 01:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0016_auto_20210407_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='id_product',
        ),
        migrations.AddField(
            model_name='product',
            name='product_store',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='compare.product_store'),
        ),
    ]