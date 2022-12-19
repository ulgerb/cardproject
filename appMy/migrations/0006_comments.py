# Generated by Django 4.1.4 on 2022-12-19 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0005_card_priece'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Ad Soyad')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('comment', models.TextField(max_length=500, verbose_name='Yorum')),
            ],
        ),
    ]
