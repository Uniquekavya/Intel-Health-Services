
from django.urls import path
from . import views
from .views import HospitalDetailView


urlpatterns = [
    path('Home/', views.home, name='home'),
    path('list/', views.hospital_list, name='hospital_list'),
    path('list/<int:pk>/', views.hospital_detail, name='hospital_detail'),
    path('search/', views.search_hospitals, name='search_hospitals'),
    path('hospitals/', views.HospitalListView.as_view(), name='hospital_list'),
    path('hospitals/<int:pk>/', views.HospitalDetailView.as_view(), name='hospital_detail'),  
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    
]


