# Generated by Django 3.1.7 on 2021-03-24 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0013_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_product', models.CharField(max_length=50)),
                ('mark', models.CharField(max_length=30)),
                ('image', models.CharField(max_length=256)),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='store_product', to='compare.product_store')),
                ('name_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_category', to='compare.category')),
            ],
        ),
    ]