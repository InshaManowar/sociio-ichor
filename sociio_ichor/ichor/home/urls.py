from . import views
from django.urls import path

app_name = 'home'

urlpatterns = [
    
    path('donate/', views.BloodListView.as_view(), name='donate'),
    path('search-blood/', views.BloodSearchView.as_view(), name='search-blood'),
    path('detail/<slug:name_slug>/', views.detail_view , name='details'),
    path('about/', views.about, name='about'),
    #path('', views.landing, name='land'),
    path('contactus/', views.contactus, name = 'contact')
]
