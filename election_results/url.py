from django.urls import path
from . import views

urlpatterns = [
    path('polling_unit_result/', views.polling_unit_result, name='polling_unit_result'),
    path('lga_summed_results/', views.lga_summed_results, name='lga_summed_results'),
    path('add_polling_unit_result/', views.add_polling_unit_result, name='add_polling_unit_result')
]
