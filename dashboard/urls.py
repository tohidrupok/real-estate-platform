from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
    path('login/', views.custom_login, name='login'),
    path('logout/', views.user_logout, name='logout'), 
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('manager-dashboard/', views.manager_dashboard, name='manager_dashboard'),
    path('delete-manager/<int:user_id>/', views.delete_manager, name='delete_manager'),

    path('', views.public_home, name='home'),
    path('upload/', views.upload_video, name='upload_video'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),


    path('properties/', views.property_list, name='propertys'),
    path('property/list/manage/', views.property_list_manage, name='property_list'),
    path('property/create/', views.property_create, name='property_create'),
    path('property/<slug:slug>/', views.property_detail, name='property_detail'),
    path('property/<slug:slug>/update/', views.property_update, name='property_update'),
    path('property/<slug:slug>/delete/', views.property_delete, name='property_delete'),

    path('sell-land/create/', views.land_create_view, name='sell_land'),
    path('sell-land/success/', lambda request: render(request, 'dashboard/success.html'), name='land_success'),
    path('sell-land/list/', views.land_list, name='land_list'),
    path('sell-land/detail/<int:pk>/', views.land_detail, name='land_detail'),
    path('sell-land/delete/<int:pk>/', views.land_delete, name='land_delete'),

    path('team/', views.team_member_list, name='team_member_list'),
    path('team/<int:pk>/', views.team_member_detail, name='team_member_detail'), 
    path('team/create/', views.team_member_create, name='team_member_create'),
    path('team/<int:pk>/update/', views.team_member_update, name='team_member_update'),
    path('team/<int:pk>/delete/', views.team_member_delete, name='team_member_delete'),

]
