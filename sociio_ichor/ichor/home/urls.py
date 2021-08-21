from . import views
from django.urls import path

app_name = 'home'

urlpatterns = [
    
    path('donate/', views.BloodListView.as_view(), name='donate'),
    path('search-blood/', views.BloodSearchView.as_view(), name='search-blood'),
    path('detail/<slug:name_slug>/', views.detail_view , name='details'),
    path('draft/<slug:name_slug>/', views.detailDraft_view , name='draft'),
    path('about/', views.about, name='about'),
    path('contactus/', views.contactus, name = 'contact'),
    path('', views.landing, name='land'),
    path('policy/', views.privacy, name='privacy'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('donor/', views.donor_form, name='donor'),
    path('donor/confirm', views.donor_confirm, name='donor_confirm'),

]
