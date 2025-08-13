from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
    path('login/', views.custom_login, name='login'),
    path('logout/', views.user_logout, name='logout'), 
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('manager-dashboard/', views.manager_dashboard, name='manager_dashboard'),
    path('delete-manager/<int:user_id>/', views.delete_manager, name='delete_manager'),
    path('delete-contact/<int:message_id>/', views.delete_contact_message, name='delete_contact_message'),

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

    path('property/image/<int:image_id>/delete/', views.delete_property_image, name='delete_property_image'),
    
    path('book-land/', views.book_land, name='book_land'),
    path('delete-land-booking/<int:booking_id>/', views.delete_land_booking, name='delete_land_booking'),
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
    
    path('designs/', views.design_list, name='design_list'),
    path('designs/<int:pk>/', views.design_detail, name='design_detail'),
    path('designs/image/<int:pk>/delete/', views.design_image_delete, name='design_image_delete'),

    
    path('interior/', views.dashboard_view, name='interior_dashboard'),
    path('categories/create/', views.category_create, name='category_create'),
    path('designs/create/', views.design_create, name='design_create'),

    path('categories/<int:pk>/edit/', views.category_edit, name='category_edit'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category_delete'),
    path('designs/<int:pk>/edit/', views.design_edit, name='design_edit'),
    path('designs/<int:pk>/delete/', views.design_delete, name='design_delete'),

    path('page/gallery/', views.gallery_view, name='gallery'),
    path('page/faq/', views.faq_view, name='faq'),


    path('testimonials/', views.testimonial_dashboard, name='testimonial_dashboard'),
    path('testimonials/delete/<int:pk>/', views.delete_testimonial, name='delete_testimonial'),
    path('testimonials/edit/<int:pk>/', views.edit_testimonial, name='edit_testimonial'),

    path('services/', views.service_list, name='service_list'),
    path('admin-dashboard/services/', views.admin_service_list, name='admin-service_list'),
    path('admin-dashboard/services/create/', views.service_create, name='service_create'),
    path('admin-dashboard/services/<int:pk>/edit/', views.service_edit, name='service_edit'),
    path('admin-dashboard/services/<int:pk>/delete/', views.service_delete, name='service_delete'),

    path('admin-dashboard/jomi/', views.jomi_list, name='jomi_list'),
    path('admin-dashboard/jomi/create/', views.jomi_create, name='jomi_create'),
    path('admin-dashboard/jomi/<int:pk>/edit/', views.jomi_edit, name='jomi_edit'),
    path('admin-dashboard/jomi/<int:pk>/delete/', views.jomi_delete, name='jomi_delete'),
    path('admin-dashboard/jomi/image/<int:pk>/delete/', views.jomi_image_delete, name='jomi_image_delete'),
    path('jomi/listing/', views.jomi_public_list, name='jomi_public_list'),

    
    path('search/', views.property_search, name='property-search'),
    path('filter/', views.filtered_properties, name='filtered_properties'),   
    path('investor-policy/', views.investor_policy, name='investor_policy'),


]
