from django.urls import path
from app.views import *

urlpatterns = [
    path('', Index, name='index'),

    # Reports:
    path('reports/hoto-report/', Reports_Hoto, name='hoto_report'),
    
    path('reports/energy-drf/', DRFReport.as_view(), name='atc_site_report'),
    path('reports/energy-fuel-drawn/', FuelDrawnReport.as_view(), name='fuel_drawn'),
    path('reports/energy-energy-reading/', EnergyReadingReport.as_view(), name='diesel_filling'),

    path('reports/energy-dfr-filter/', EnergyDFRFilters.as_view(), name='energy_dfr_filter'),
    path('reports/energy-reading-filter/', EnergyReadingFilters.as_view(), name='energy_reading_filter'),
    path('reports/fuel-drawn-filter/', FuelDrawnFilters.as_view(), name='fuel_drawn_filter'),

    # Forms:
    path('forms/diesel-meter/filling-reading-fill-form/', DieselFillingOrReadingViews.as_view(), name='atcform'),
    path('forms/fuel-drawn-fill-form/', FuelDrawnViews.as_view(), name='fueldrawnform'),

    path('user/logout/', LogOut.as_view(), name='logout'),
]