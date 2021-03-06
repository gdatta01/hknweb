# Generated by Django 2.1.3 on 2018-11-05 06:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumnus',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='alumnus',
            name='company',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='alumnus',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='alumnus',
            name='first_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='alumnus',
            name='grad_school',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='alumnus',
            name='grad_semester',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='alumnus',
            name='job_title',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='alumnus',
            name='last_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='alumnus',
            name='location',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='alumnus',
            name='name_id',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='alumnus',
            name='salary',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='alumnus',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='alumnus',
            name='mailing_list',
            field=models.BooleanField(default=''),
        ),
        migrations.AlterField(
            model_name='alumnus',
            name='perm_email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
