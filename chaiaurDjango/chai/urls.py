
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_chai, name='All_Chai'),
    path('<int:chai_id>/', views.chai_detail, name='Chai_Detail'),
    path('chai_stores/', views.chai_store_view, name='Chai_Stores'),
]