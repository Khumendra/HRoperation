# Generated by Django 2.1.1 on 2018-12-09 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0002_auto_20181207_1617'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('hr_email', models.EmailField(max_length=254)),
                ('comp_name', models.CharField(max_length=100)),
            ],
        ),
    ]
