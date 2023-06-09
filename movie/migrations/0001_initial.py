# Generated by Django 4.2.1 on 2023-05-23 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_th', models.CharField(max_length=100)),
                ('name_en', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('channel', models.CharField(choices=[('netflix', 'Netflix'), ('viu', 'VIU'), ('youtube', 'Youtube')], default='netflix', max_length=10)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
