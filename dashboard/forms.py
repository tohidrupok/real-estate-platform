from django import forms
from .models import LandBooking, Jomi, JomiImage, Service, Property, Feature, Video, Land, TeamMember, Category, DesignItem, ClientTestimonial, ContactMessage

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        exclude = ['slug', 'date_posted']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'id_no': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.TextInput(attrs={'class': 'form-control'}),
            'purpose': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'sqft': forms.TextInput(attrs={'class': 'form-control'}),
            # 'featured_sqft': forms.NumberInput(attrs={'class': 'form-control'}),
            'unit': forms.NumberInput(attrs={'class': 'form-control'}),
            'room': forms.NumberInput(attrs={'class': 'form-control'}),
            'bedroom': forms.NumberInput(attrs={'class': 'form-control'}),
            'bath': forms.NumberInput(attrs={'class': 'form-control'}),
            'big_yard': forms.NumberInput(attrs={'class': 'form-control'}),
            'built_in': forms.NumberInput(attrs={'class': 'form-control'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.000001', 'placeholder': 'Enter Latitude'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.000001', 'placeholder': 'Enter Longitude'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'description_short': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'description_long': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'is_complete': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'features': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        }

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'youtube_url']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter video title'
            }),
            'youtube_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Paste YouTube video link'
            }),
        }


class LandForm(forms.ModelForm):
    class Meta:
        model = Land
        exclude = ['is_published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'district': forms.TextInput(attrs={'class': 'form-control'}),
            'postcode': forms.TextInput(attrs={'class': 'form-control'}),
            'land_type': forms.Select(attrs={'class': 'form-select'}),
            'ownership_type': forms.Select(attrs={'class': 'form-select'}),
            'area_size': forms.NumberInput(attrs={'class': 'form-control'}),
            'road_width': forms.NumberInput(attrs={'class': 'form-control'}),
            'electricity': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'gas': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'water': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'drainage': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'legal_clearance': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'contact_name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'main_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(LandForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, (forms.TextInput, forms.NumberInput, forms.EmailInput, forms.Textarea)):
                field.widget.attrs['class'] = 'form-control'
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select'
            elif isinstance(field.widget, forms.ClearableFileInput):
                field.widget.attrs['class'] = 'form-control'
            elif isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input' 


class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'facebook': forms.URLInput(attrs={'class': 'form-control'}),
            'twitter': forms.URLInput(attrs={'class': 'form-control'}),
            'linkedin': forms.URLInput(attrs={'class': 'form-control'}),
            'instagram': forms.URLInput(attrs={'class': 'form-control'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'years_of_experience': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class DesignItemForm(forms.ModelForm):
    class Meta:
        model = DesignItem
        fields = ['category', 'name', 'description', 'is_featured']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'is_featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class ClientTestimonialForm(forms.ModelForm):
    class Meta:
        model = ClientTestimonial
        fields = ['name', 'designation', 'message', 'photo']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'}),
            'designation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter designation'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Write message'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'is_approved': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        } 


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'number', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name *'
            }),
            'number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone *'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email Address *'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Subject *'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your Message *',
                'rows': 3
            }),
        } 


class LandBookingForm(forms.ModelForm):
    class Meta:
        model = LandBooking
        fields = '__all__'
        widgets = {
            'contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter contact number'}),
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
            'land_location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter location'}),
            'land_size': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter land size'}),
            'booking_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        
    def clean_contact_number(self):
        contact_number = self.cleaned_data.get('contact_number')
        if not contact_number.isdigit():
            raise forms.ValidationError("Contact number must contain digits only.")
        return contact_number
  
    
class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter service name',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe the service',
                'rows': 4,
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
        }


class JomiForm(forms.ModelForm):
    class Meta:
        model = Jomi
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'class': 'form-control', 'placeholder': 'Jomir bistarito bolo'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Jomir Title'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'district': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'District'}),
            'area_size': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Area Size'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'contact_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Name'}),
            'contact_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Phone'}),
        }