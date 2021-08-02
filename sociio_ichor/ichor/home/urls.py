from . import views
from django.urls import path

app_name = 'home'

urlpatterns = [
    
    path('', views.BloodListView.as_view(), name='home'),
    path('search-blood/', views.BloodSearchView.as_view(), name='search-blood'),
    path('detail/<slug:name_slug>/', views.detail_view , name='details'),
    path('about/', views.about, name='about'),
    path('contactus/', views.contactus, name = 'contact')
]
