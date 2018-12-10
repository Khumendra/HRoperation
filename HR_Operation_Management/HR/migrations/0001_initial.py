# Generated by Django 2.1.1 on 2018-12-07 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant_Registration',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=60, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('phone', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HR_Registration',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=60)),
                ('password', models.CharField(max_length=20)),
                ('company_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Interviewer_Registration',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=60, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('phone', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manager_Registration',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=60, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('phone', models.IntegerField(null=True)),
            ],
        ),
    ]
