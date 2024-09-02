# Generated by Django 5.0.6 on 2024-07-11 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='waterusage',
            name='activity',
        ),
        migrations.RemoveField(
            model_name='waterusage',
            name='amount',
        ),
        migrations.AddField(
            model_name='waterusage',
            name='cooking',
            field=models.FloatField(default=0, help_text='Liters of water used for cooking', verbose_name='Cooking (liters)'),
        ),
        migrations.AddField(
            model_name='waterusage',
            name='num_people',
            field=models.IntegerField(default=0, help_text='Number of people in the household', verbose_name='Number of People'),
        ),
        migrations.AddField(
            model_name='waterusage',
            name='showering',
            field=models.FloatField(default=0, help_text='Liters of water used for showering', verbose_name='Showering (liters)'),
        ),
        migrations.AddField(
            model_name='waterusage',
            name='washing_cars',
            field=models.FloatField(default=0, help_text='Liters of water used for washing cars', verbose_name='Washing Cars (liters)'),
        ),
        migrations.AddField(
            model_name='waterusage',
            name='washing_clothes',
            field=models.FloatField(default=0, help_text='Liters of water used for washing clothes', verbose_name='Washing Clothes (liters)'),
        ),
        migrations.AddField(
            model_name='waterusage',
            name='washing_utensils',
            field=models.FloatField(default=0, help_text='Liters of water used for washing utensils', verbose_name='Washing Utensils (liters)'),
        ),
        migrations.AddField(
            model_name='waterusage',
            name='watering_plants',
            field=models.FloatField(default=0, help_text='Liters of water used for watering plants', verbose_name='Watering Plants (liters)'),
        ),
    ]
