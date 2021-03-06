# Generated by Django 3.1.7 on 2021-03-24 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0014_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wish_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_email', to='compare.user')),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_id', to='compare.product_store')),
            ],
        ),
    ]
