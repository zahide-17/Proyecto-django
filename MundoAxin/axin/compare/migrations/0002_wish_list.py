# Generated by Django 3.1.7 on 2021-03-24 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wish_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_product', models.DecimalField(blank=True, decimal_places=6, max_digits=8, null=True)),
                ('user_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compare.user')),
            ],
        ),
    ]
