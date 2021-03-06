# Generated by Django 2.0.3 on 2018-04-23 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='CourseSemester',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('course', models.IntegerField()),
                ('semester', models.CharField(max_length=255)),
                ('instructor', models.CharField(max_length=255)),
                ('midterm1', models.FileField(blank=True, upload_to='')),
                ('midterm2', models.FileField(blank=True, upload_to='')),
                ('midterm3', models.FileField(blank=True, upload_to='')),
                ('final', models.FileField(blank=True, upload_to='')),
            ],
        ),
    ]
