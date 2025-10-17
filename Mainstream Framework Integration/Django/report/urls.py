from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),           # Homepage
    path('export/', views.export_report, name='export_report'),  # export  Excel
]
