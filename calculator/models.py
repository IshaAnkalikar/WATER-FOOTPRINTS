# calculator/models.py

from django.db import models

class WaterUsage(models.Model):
    num_people = models.IntegerField(default=0,verbose_name="Number of People", help_text="Number of people in the household")
    watering_plants = models.FloatField(default=0, verbose_name="Watering Plants (liters)", help_text="Liters of water used for watering plants")
    washing_cars = models.FloatField(default=0, verbose_name="Washing Cars (liters)", help_text="Liters of water used for washing cars")
    washing_utensils = models.FloatField(default=0, verbose_name="Washing Utensils (liters)", help_text="Liters of water used for washing utensils")
    washing_clothes = models.FloatField(default=0, verbose_name="Washing Clothes (liters)", help_text="Liters of water used for washing clothes")
    showering = models.FloatField(default=0, verbose_name="Showering (liters)", help_text="Liters of water used for showering")
    cooking = models.FloatField(default=0, verbose_name="Cooking (liters)", help_text="Liters of water used for cooking")

    def total_usage(self):
        return (self.watering_plants + self.washing_cars + self.washing_utensils +
                self.washing_clothes + self.showering + self.cooking)

    def __str__(self):
        return f"Household size: {self.num_people}, Total usage: {self.total_usage()} liters"
