# Generated by Django 3.2.7 on 2021-09-05 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stud_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cName', models.CharField(max_length=20)),
                ('cSex', models.CharField(default='Male', max_length=6)),
                ('cDob', models.DateField()),
                ('cEmail', models.EmailField(blank=True, default='', max_length=100)),
                ('cPhone', models.CharField(blank=True, default='', max_length=50)),
                ('cAddr', models.CharField(blank=True, default='', max_length=255)),
            ],
        ),
    ]