# Generated by Django 2.1.8 on 2019-09-23 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=200)),
                ('contact_name', models.CharField(blank=True, max_length=200)),
                ('email_address', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='StreetAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stret_name', models.CharField(max_length=200)),
                ('suburb', models.CharField(max_length=200)),
                ('postcode', models.IntegerField()),
                ('state', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='client.StreetAddress'),
        ),
    ]
