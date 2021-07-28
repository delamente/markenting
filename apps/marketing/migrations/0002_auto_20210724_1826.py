# Generated by Django 3.0.11 on 2021-07-24 18:26

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_delete_student'),
        ('marketing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Nombre')),
                ('email_or_phone', models.CharField(max_length=128, verbose_name='Celular o e-mail')),
                ('message', models.TextField(verbose_name='Mensaje')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Nombre')),
                ('description', ckeditor.fields.RichTextField(blank=True, default='', verbose_name='Descripción')),
                ('image', models.ImageField(upload_to='services/', verbose_name='Imagen')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='class',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='class',
            name='course',
        ),
        migrations.RemoveField(
            model_name='course',
            name='required_courses',
        ),
        migrations.DeleteModel(
            name='LiveCourse',
        ),
        migrations.DeleteModel(
            name='Class',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
    ]