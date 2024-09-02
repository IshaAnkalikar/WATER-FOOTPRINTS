# calculator/forms.py
from django import forms
from .models import WaterUsage

class WaterUsageForm(forms.ModelForm):
    class Meta:
        model = WaterUsage
        fields = [
            'num_people', 'watering_plants', 'washing_cars', 'washing_utensils',
            'washing_clothes', 'showering', 'cooking'
        ]
        labels = {
            'num_people': 'Number of People in the Household',
            'watering_plants': 'Water Used for Watering Plants (liters)',
            'washing_cars': 'Water Used for Washing Cars (liters)',
            'washing_utensils': 'Water Used for Washing Utensils (liters)',
            'washing_clothes': 'Water Used for Washing Clothes (liters)',
            'showering': 'Water Used for Showering (liters)',
            'cooking': 'Water Used for Cooking (liters)',
        }
        widgets = {
            'num_people': forms.NumberInput(attrs={'placeholder': 'Enter number of people'}),
            'watering_plants': forms.NumberInput(attrs={'placeholder': 'Enter liters used'}),
            'washing_cars': forms.NumberInput(attrs={'placeholder': 'Enter liters used'}),
            'washing_utensils': forms.NumberInput(attrs={'placeholder': 'Enter liters used'}),
            'washing_clothes': forms.NumberInput(attrs={'placeholder': 'Enter liters used'}),
            'showering': forms.NumberInput(attrs={'placeholder': 'Enter liters used'}),
            'cooking': forms.NumberInput(attrs={'placeholder': 'Enter liters used'}),
        }
