# Generated by Django 3.1.7 on 2021-03-24 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0002_wish_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id_store', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('url', models.URLField()),
                ('number_products', models.PositiveIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='alias',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=30),
        ),
        migrations.DeleteModel(
            name='Wish_list',
        ),
    ]
