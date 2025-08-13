from django.contrib import admin
from .models import *

class PropertyAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'id_no', 'type', 'purpose', 'price', 'sqft', 'featured_sqft',
              'room', 'bedroom', 'bath', 'big_yard',
              'parking', 'elevator', 'wifi', 'built_in',
              'address','latitude','longitude', 'description_short', 'description_long','features',
              'featured', 'is_active', 'is_complete', 'status') 

    prepopulated_fields = {'slug': ('name',)}  

    list_display = ('name', 'slug', 'id_no', 'type', 'purpose', 'price', 'date_posted', 'is_active')
    list_filter = ('type', 'purpose', 'featured', 'is_active','is_complete' ,'date_posted')
    search_fields = ('name', 'id_no', 'type', 'purpose')


class PropertyImageAdmin(admin.ModelAdmin):
    list_display = ('property', 'image', 'alt_text')
    search_fields = ('property__name', 'alt_text')




admin.site.register(Property, PropertyAdmin)
admin.site.register(PropertyImage, PropertyImageAdmin)
admin.site.register(Land)
admin.site.register(LandImage)
admin.site.register(Video)
admin.site.register(Category)
admin.site.register(DesignItem)
admin.site.register(ClientTestimonial)
admin.site.register(TeamMember)
admin.site.register(Service)
admin.site.register(ContactMessage)
admin.site.register(DesignImage)
admin.site.register(Feature)
admin.site.register(LandBooking)
admin.site.register(Jomi)
admin.site.register(JomiImage)