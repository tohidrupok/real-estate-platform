from django.db import models
from django.utils.text import slugify 

class Feature(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Property(models.Model):
    
    STATUS_CHOICES = [
        ('ongoing', 'On Going'),
        ('ready_flat', 'Ready Flat'),
        ('complete', 'Complete Project'),
        ('upcoming', 'Upcoming'),
    ]
    name = models.CharField(max_length=255, verbose_name="Property Name")
    id_no = models.CharField(max_length=50, unique=True, verbose_name="ID NO.")
    type = models.CharField(max_length=100, verbose_name="Type") 
    purpose = models.CharField(max_length=100, verbose_name="Purpose") 
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Price", null=True, blank=True)
    sqft = models.CharField(max_length=50, verbose_name="Square Feet")
    featured_sqft = models.PositiveIntegerField(verbose_name="Featured Sqft", null=True, blank=True)
    unit = models.CharField(max_length=50, verbose_name="Units", null=True, blank=True)
    room = models.PositiveIntegerField(verbose_name="Total Rooms")
    bedroom = models.PositiveIntegerField(verbose_name="Bedrooms")
    bath = models.PositiveIntegerField(verbose_name="Bathrooms")
    big_yard = models.PositiveIntegerField(verbose_name="Big Yard", null=True, blank=True)

    parking = models.BooleanField(default=False, verbose_name="Parking Available")
    elevator = models.BooleanField(default=False, verbose_name="Elevator Available")
    wifi = models.BooleanField(default=False, verbose_name="WiFi Available")

    built_in = models.PositiveIntegerField(verbose_name="Built Year", null=True, blank=True)

    address = models.TextField(verbose_name="Address", null=True, blank=True)
    map_embed_url = models.URLField(verbose_name="Iframe Link Only", blank=True, null=True) 
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, verbose_name="Latitude")
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, verbose_name="Longitude")


    description_short = models.TextField(verbose_name="Short Description", null=True, blank=True)
    description_long = models.TextField(verbose_name="Long Description", null=True, blank=True)

    featured = models.BooleanField(default=False, verbose_name="Featured Property")
    date_posted = models.DateField(verbose_name="Date Posted", auto_now_add=True)


    # Extra convenience fields
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    is_complete = models.BooleanField(default=False, verbose_name="Is Complete")
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft', verbose_name="Status")
    features = models.ManyToManyField('Feature', blank=True, related_name='properties')
    
    def __str__(self):
        return f"{self.name} ({self.id_no})"

    class Meta:
        ordering = ['-date_posted']
    
    @property
    def map_embed_url(self):
        """Generate Google Maps embed URL from latitude & longitude."""
        if self.latitude and self.longitude:
            return f"https://www.google.com/maps?q={self.latitude},{self.longitude}&hl=en&z=14&output=embed"
        return ""

    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            num = 1
            while Property.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug
        super().save(*args, **kwargs) 

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='property_images/')
    alt_text = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.property.name}"
    

class Video(models.Model):
    title = models.CharField(max_length=255)
    youtube_url = models.URLField()

    def __str__(self):
        return self.title 
    


class Land(models.Model):
    LAND_TYPE_CHOICES = [
        ('residential', 'Residential'),
        ('commercial', 'Commercial'),
        ('agricultural', 'Agricultural'),
        ('industrial', 'Industrial'),
        ('others', 'Others'),
    ]

    OWNERSHIP_CHOICES = [
        ('freehold', 'Freehold'),
        ('leasehold', 'Leasehold'),
        ('inherited', 'Inherited'),
        ('others', 'Others'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    postcode = models.CharField(max_length=10, blank=True)

    land_type = models.CharField(max_length=20, choices=LAND_TYPE_CHOICES, default='residential')
    ownership_type = models.CharField(max_length=20, choices=OWNERSHIP_CHOICES, default='freehold')

    area_size = models.DecimalField(max_digits=10, decimal_places=2, help_text='Area in Katha/Decimal/Bigha/etc.')
    road_width = models.DecimalField(max_digits=6, decimal_places=2, help_text='In feet', null=True, blank=True)

    electricity = models.BooleanField(default=False)
    gas = models.BooleanField(default=False)
    water = models.BooleanField(default=False)
    drainage = models.BooleanField(default=False)
    legal_clearance = models.BooleanField(default=True)

    contact_name = models.CharField(max_length=100)
    contact_phone = models.CharField(max_length=20)
    contact_email = models.EmailField(blank=True, null=True)

    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    main_image = models.ImageField(upload_to='lands sell/main_images/', null= True, blank = True)
    is_published = models.BooleanField(default=False, null= True, blank = True)
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_google_maps_embed_url(self):
        if self.latitude and self.longitude:
            return f"https://maps.google.com/maps?q={self.latitude},{self.longitude}&z=15&output=embed"
        return ""


class LandImage(models.Model):
    land = models.ForeignKey(Land, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='lands_sell/extra_images/')

    def __str__(self):
        return f"Image of {self.land.title}" 
    

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='team_photos/')
    bio = models.TextField(blank=True, null=True)
    
    # Optional social media links
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    years_of_experience = models.PositiveIntegerField(default=0) 

    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 
    

from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
    @property
    def slug(self):
        return slugify(self.name)

class DesignItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="design_items")
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="Interior/designs/", null= True, blank= True)
    description = models.TextField(blank=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
 
    @property
    def category_slug(self):
        return slugify(self.category.name)


class DesignImage(models.Model):
    design_item = models.ForeignKey(DesignItem, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to="Interior/designs/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.design_item.name}" 
    

class ClientTestimonial(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100, blank=True)  
    message = models.TextField()
    photo = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=True)  

    def __str__(self):
        return f"{self.name} - Testimonial"
    

class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='service_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 
    
    

class ContactMessage(models.Model):
    name = models.CharField(default="Customer",  max_length=100, blank=True, null=True)
    number = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    subject = models.CharField(default="Contact me urgent", max_length=100, blank=True, null=True)
    message = models.TextField( blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
 

class LandBooking(models.Model):
    contact_number = models.CharField(max_length=20, verbose_name="Contact Number")  

    customer_name = models.CharField(max_length=255, verbose_name="Customer Name", blank=True, null=True)
    email = models.EmailField(verbose_name="Email", blank=True, null=True)
    land_location = models.CharField(max_length=255, verbose_name="Land Location", blank=True, null=True)
    land_size = models.CharField(max_length=50, verbose_name="Land Size", blank=True, null=True)
    booking_date = models.DateField(verbose_name="Booking Date", blank=True, null=True)

    status_choices = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='pending', blank=True, null=True)
    notes = models.TextField(blank=True, null=True, verbose_name="Additional Notes")

    def __str__(self):
        return f"{self.contact_number} - {self.land_location or 'No Location'}"


class Jomi(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('sold', 'Sold'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField( null=True, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    district = models.CharField(max_length=100, null=True, blank=True)
    area_size = models.CharField(max_length=100, null=True, blank=True)  
    address = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    contact_name = models.CharField(max_length=100, null=True, blank=True)
    contact_phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.city}"

class JomiImage(models.Model):
    jomi = models.ForeignKey(Jomi, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='jomi_images/')

    def __str__(self):
        return f"Image for {self.jomi.title}"
