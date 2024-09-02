from django.shortcuts import render, redirect
from .forms import WaterUsageForm
from .models import WaterUsage

def index(request):
    return render(request, 'calculator/index.html')

def home(request):
    if request.method == 'POST':
        form = WaterUsageForm(request.POST)
        if form.is_valid():
            water_usage = form.save(commit=False)
            total_water_usage = (water_usage.watering_plants +
                                 water_usage.washing_cars +
                                 water_usage.washing_utensils +
                                 water_usage.washing_clothes +
                                 water_usage.showering +
                                 water_usage.cooking)
            context = {
                'water_usage': water_usage,
                'total_water_usage': total_water_usage
            }
            return render(request, 'calculator/results.html', context)
    else:
        form = WaterUsageForm()
    return render(request, 'calculator/home.html', {'form': form})

def results(request):
    return render(request, 'calculator/results.html')

def awareness(request):
    return render(request, 'calculator/awareness.html')
