# Generated by Django 3.1.3 on 2020-11-17 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadMarks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam_data',
            name='average',
            field=models.IntegerField(blank=True, null=True, verbose_name='Maths'),
        ),
    ]