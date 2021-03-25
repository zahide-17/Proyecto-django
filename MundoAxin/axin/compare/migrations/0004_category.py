# Generated by Django 3.1.7 on 2021-03-24 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0003_auto_20210324_1447'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('L6', 'Labial'), ('S7', 'Sombras'), ('R5', 'Rubor'), ('B5', 'Bases'), ('D0', 'Delineador'), ('I0', 'Iluminador'), ('C9', 'Corrector')], max_length=2)),
            ],
        ),
    ]
