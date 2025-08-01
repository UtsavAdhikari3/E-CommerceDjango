# Generated by Django 5.2.4 on 2025-07-29 13:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('in_stock', models.BooleanField()),
                ('quantity', models.IntegerField(validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(1)])),
                ('created_date', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
