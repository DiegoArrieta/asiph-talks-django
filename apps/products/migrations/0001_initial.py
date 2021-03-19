# Generated by Django 3.1.7 on 2021-03-19 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sku', models.CharField(max_length=50, unique=True)),
                ('status', models.CharField(choices=[('NEW', 'NEW'), ('USED', 'USED'), ('EXPIRED', 'EXPIRED')], default='NEW', max_length=10)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
