from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import PropertyImage, LandBooking, Property, Video, Land, LandImage, TeamMember, Category, DesignItem, ClientTestimonial, Service, ContactMessage, DesignImage
from .forms import PropertyForm, ServiceForm, VideoForm, LandForm, TeamMemberForm,CategoryForm, DesignItemForm, ClientTestimonialForm, ContactForm
from django.contrib.auth.models import User, Group 
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def public_home(request):
    video = Video.objects.last()
    featured_properties = Property.objects.filter(is_active=True, featured=True).order_by('-date_posted')[:9]
    testimonials = ClientTestimonial.objects.filter(is_approved=True).order_by('-created_at')
    complete_project_list = Property.objects.filter(is_complete=True).order_by('-date_posted')

    # Paginate all properties
    property_list = Property.objects.filter(is_active=True).order_by('-date_posted')
    paginator = Paginator(property_list, 6)
    page = request.GET.get('page')
    try:
        properties = paginator.page(page)
    except PageNotAnInteger:
        properties = paginator.page(1)
    except EmptyPage:
        properties = paginator.page(paginator.num_pages)

    members = TeamMember.objects.filter(is_active=True)

    # Dynamic dropdown values from Property model
    all_types = Property.objects.values_list('type', flat=True).distinct()
    all_locations = Property.objects.values_list('address', flat=True).distinct()
    all_bedrooms = Property.objects.values_list('bedroom', flat=True).distinct()

    return render(request, 'dashboard/home.html', {
        'video': video,
        'featured_properties': featured_properties,
        'properties': properties,
        'complete_project_list': complete_project_list,
        'members': members,
        'testimonials': testimonials,
        'all_types': all_types,
        'all_locations': all_locations,
        'all_bedrooms': all_bedrooms,
    })


# def public_home(request):
#     video = Video.objects.last()  

#     featured_properties = Property.objects.filter(is_active=True, featured=True).order_by('-date_posted')[:9]
#     testimonials = ClientTestimonial.objects.filter(is_approved=True).order_by('-created_at')

#     # Paginated all properties
#     property_list = Property.objects.filter(is_active=True).order_by('-date_posted')
#     complete_project_list = Property.objects.filter(is_complete=True).order_by('-date_posted')
#     paginator = Paginator(property_list, 6)  
#     page = request.GET.get('page')

#     try:
#         properties = paginator.page(page)
#     except PageNotAnInteger:
#         properties = paginator.page(1)
#     except EmptyPage:
#         properties = paginator.page(paginator.num_pages)

#     members = TeamMember.objects.filter(is_active=True)
#     return render(request, 'dashboard/home.html', {
#         'video': video,
#         'featured_properties': featured_properties,
#         'properties': properties,
#         'complete_project_list': complete_project_list,
#         'members': members,
#         'testimonials': testimonials
#     })

 

def about(request):

    testimonials = ClientTestimonial.objects.filter(is_approved=True).order_by('-created_at')
    members = TeamMember.objects.filter(is_active=True)
    service_list = Service.objects.all()
    paginator = Paginator(service_list, 10)  

    page_number = request.GET.get('page')
    services = paginator.get_page(page_number)

    return render(request, 'dashboard/about.html', {
        'members': members,
        'services': services,
        'testimonials': testimonials,
    }) 


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'dashboard/contact.html', {'form': form}) 


def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            if user.is_superuser:
                return redirect('admin_dashboard')
            elif user.groups.filter(name='Manager').exists():
                return redirect('home')
        else:
            return render(request, 'dashboard/login.html', {'error': 'Invalid login'})
    return render(request, 'dashboard/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('home') 


@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_dashboard(request):
    total_properties = Property.objects.count()
    total_managers = User.objects.filter(groups__name='Manager').count()
    contact_messages = ContactMessage.objects.order_by('-created_at')
    land_bookings = LandBooking.objects.all().order_by('-id')
    lands = Land.objects.all().order_by('-posted_on')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(request, 'dashboard/admin_dashboard.html', {
                'error': 'Username already exists',
                'managers': get_managers(),
                'total_properties': total_properties,
                'total_managers': total_managers,
                'land_bookings': land_bookings,
                'lands': lands, 
            })

        user = User.objects.create_user(username=username, password=password)
        group = Group.objects.get(name='Manager')
        user.groups.add(group)

        return render(request, 'dashboard/admin_dashboard.html', {
            'success': 'Manager created successfully',
            'managers': get_managers(),
            'total_properties': total_properties,
            'total_managers': total_managers,
            'contact_messages': contact_messages,
            'land_bookings': land_bookings,
            'lands': lands, 
        })

    return render(request, 'dashboard/admin_dashboard.html', {
        'managers': get_managers(),
        'total_properties': total_properties,
        'total_managers': total_managers,
        'contact_messages': contact_messages,
        'land_bookings': land_bookings,
        'lands': lands, 
    })



@login_required
def delete_contact_message(request, message_id):
    if request.method == 'POST':
        message = get_object_or_404(ContactMessage, id=message_id)
        message.delete()
    return redirect('admin_dashboard') 



@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_manager(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if user.groups.filter(name='Manager').exists():
        user.delete()
    return redirect('admin_dashboard')



def get_managers():
    return User.objects.filter(groups__name='Manager')
 



@login_required
@user_passes_test(lambda u: u.groups.filter(name='Manager').exists())
def manager_dashboard(request):
    return render(request, 'dashboard/manager_dashboard.html')


@login_required
def property_list_manage(request):
    properties = Property.objects.all()
    # featured_properties = Property.objects.filter(featured=True).order_by('-date_posted')[:4]
    featured_properties = Property.objects.all()
    
    return render(request, 'property/property_list.html', {
        'properties': properties,
        'featured_properties': featured_properties,
    })


def property_detail(request, slug):
    property = get_object_or_404(Property, slug=slug)
    featured_properties = Property.objects.filter(featured=True).order_by('-date_posted')[:4]
    selected_features = property.features.all()

    # Contact form handle
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('property_detail', slug=slug)
    else:
        form = ContactForm()

    context = {
        'property': property,
        'featured_properties': featured_properties,
        'selected_features': selected_features,
        'form': form
    }
    return render(request, 'property/property_detail.html', context)

@login_required
def property_create(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        images = request.FILES.getlist('images')
        if form.is_valid():
            property = form.save(commit=False)  
            property.save() 
            form.save_m2m()  
            for img in images:
                PropertyImage.objects.create(property=property, image=img)
            return redirect('property_list')
    else:
        form = PropertyForm()

    return render(request, 'property/property_form.html', {'form': form})

@login_required
def property_update(request, slug):
    property = get_object_or_404(Property, slug=slug)

    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property)
        images = request.FILES.getlist('images')

        if form.is_valid():
            property_obj = form.save(commit=False)  
            property_obj.save()  
            form.save_m2m()  
          
            for img in images:
                PropertyImage.objects.create(property=property_obj, image=img)

            return redirect('property_detail', slug=property.slug)
    else:
        form = PropertyForm(instance=property)


    return render(request, 'property/property_form.html', {
        'form': form,
        'property': property,
    })

@login_required
def property_delete(request, slug):
    property = get_object_or_404(Property, slug=slug)
    if request.method == 'POST':
        property.delete()
        return redirect('property_list')
    return render(request, 'property/property_confirm_delete.html', {'property': property}) 

from django.views.decorators.http import require_POST
from django.contrib import messages


@require_POST
def delete_property_image(request, image_id):
    image = get_object_or_404(PropertyImage, id=image_id)
    
    # Optional: protect from unauthorized delete
    # You can add login or owner check here

    property_slug = image.property.slug
    image.delete()
    messages.success(request, "Image deleted successfully.")
    return redirect('property_update', slug=property_slug)



def property_list(request):
    property_list = Property.objects.filter(is_active=True).order_by('-date_posted')
    paginator = Paginator(property_list, 15)
    page = request.GET.get('page')

    try:
        properties = paginator.page(page)
    except PageNotAnInteger:
        properties = paginator.page(1)
    except EmptyPage:
        properties = paginator.page(paginator.num_pages)

    featured_properties = Property.objects.filter(featured=True, is_active=True).order_by('-date_posted')[:4]

    # Contact form handling
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('propertys')  
    else:
        form = ContactForm()

    context = {
        'properties': properties,
        'featured_properties': featured_properties,
        'form': form,
    }

    return render(request, 'property/property_listing.html', context)


@login_required
def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VideoForm()
    return render(request, 'dashboard/upload_video.html', {'form': form})

@login_required
def land_create_view(request):
    if request.method == 'POST':
        form = LandForm(request.POST, request.FILES)
        images = request.FILES.getlist('extra_images')  

        if form.is_valid():
            land = form.save()

            # Save each uploaded image
            for img in images:
                LandImage.objects.create(land=land, image=img)

            return redirect('land_success')

    else:
        form = LandForm()

    return render(request, 'dashboard/land_form.html', {'form': form})


def land_list(request):
    lands = Land.objects.all().order_by('-posted_on')
    return render(request, 'lands/land_list.html', {'lands': lands})

@login_required
def land_delete(request, pk):
    land = get_object_or_404(Land, pk=pk)
    if request.method == 'POST':
        land.delete()
        return redirect('admin_dashboard')
    return render(request, 'lands/land_confirm_delete.html', {'land': land})

def land_detail(request, pk):
    land = get_object_or_404(Land, pk=pk)
    return render(request, 'lands/land_detail.html', {'land': land})


#            Team member                 Team member                 Team member                 Team member  #

def team_member_list(request):
    members = TeamMember.objects.all()
    return render(request, 'team/member_list.html', {'members': members})

@login_required
def team_member_create(request):
    if request.method == 'POST':
        form = TeamMemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('team_member_list')
    else:
        form = TeamMemberForm()
    return render(request, 'team/member_form.html', {'form': form})

@login_required
def team_member_update(request, pk):
    member = get_object_or_404(TeamMember, pk=pk)
    if request.method == 'POST':
        form = TeamMemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            return redirect('team_member_list')
    else:
        form = TeamMemberForm(instance=member)
    return render(request, 'team/member_form.html', {'form': form})

@login_required
def team_member_delete(request, pk):
    member = get_object_or_404(TeamMember, pk=pk)
    if request.method == 'POST':
        member.delete()
        return redirect('team_member_list')
    return render(request, 'team/member_confirm_delete.html', {'member': member})

@login_required
def team_member_detail(request, pk):
    member = get_object_or_404(TeamMember, pk=pk)
    return render(request, 'team/member_detail.html', {'member': member}) 


# ----- Category Views -----
@login_required
def dashboard_view(request):
    categories = Category.objects.all()
    designs = DesignItem.objects.select_related('category').all()
    return render(request, 'interior/interior.html', {
        'categories': categories,
        'designs': designs
    })

@login_required
def category_create(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('interior_dashboard')
    return render(request, 'interior/category_form.html', {'form': form})


@login_required
def design_create(request):
    if request.method == 'POST':
        form = DesignItemForm(request.POST)
        images = request.FILES.getlist('images')

        if form.is_valid():
            design = form.save()
            for img in images:
                DesignImage.objects.create(design_item=design, image=img)
            return redirect('design_list')
    else:
        form = DesignItemForm()
    return render(request, 'interior/design_form.html', {'form': form}) 

@login_required
def design_image_delete(request, pk):
    image = get_object_or_404(DesignImage, pk=pk)
    design_id = image.design_item.id
    image.delete()
    return redirect('design_edit', pk=design_id) 


@login_required
def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect('interior_dashboard')
    return render(request, 'interior/category_form.html', {'form': form})

@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('interior_dashboard')
    return render(request, 'interior/category_confirm_delete.html', {'category': category})


# ----- DesignItem Edit/Delete -----

@login_required
def design_edit(request, pk):
    design = get_object_or_404(DesignItem, pk=pk)
    form = DesignItemForm(request.POST or None, request.FILES or None, instance=design)
    if form.is_valid():
        form.save()
        return redirect('interior_dashboard')
    return render(request, 'interior/design_form.html', {
        'form': form,
        'design': design  
    })

@login_required
def design_delete(request, pk):
    design = get_object_or_404(DesignItem, pk=pk)
    if request.method == 'POST':
        design.delete()
        return redirect('interior_dashboard')
    return render(request, 'interior/design_confirm_delete.html', {'design': design}) 


def design_list(request):
    design_qs = DesignItem.objects.select_related('category').all().order_by('name')
    paginator = Paginator(design_qs, 16)  

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'interior/design_list.html', {
        'page_obj': page_obj,
    })

def design_detail(request, pk):
    design = get_object_or_404(DesignItem, pk=pk)
    featured_designs = DesignItem.objects.filter(is_featured=True).exclude(pk=pk)[:8]

    return render(request, 'interior/design_detail.html', {
        'design': design,
        'featured_designs': featured_designs,
    })


def faq_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('faq')
    else:
        form = ContactForm()

    return render(request, 'page/faq.html', {'form': form}) 

def gallery_view(request):
    design_items = DesignItem.objects.select_related('category').all()
    land_images = LandImage.objects.select_related('land').all()
    categories = Category.objects.all()

    paginator = Paginator(design_items, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'page/gallery.html', {
        'page_obj': page_obj,
        'land_images': land_images,
        'categories': categories,
    })
 

@login_required
def testimonial_dashboard(request):
    testimonials = ClientTestimonial.objects.all().order_by('-created_at')

    # Handle form submission
    if request.method == 'POST':
        form = ClientTestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('testimonial_dashboard')
    else:
        form = ClientTestimonialForm()

    return render(request, 'page/testimonial_dashboard.html', {
        'testimonials': testimonials,
        'form': form,
    })

@login_required
def delete_testimonial(request, pk):
    testimonial = get_object_or_404(ClientTestimonial, pk=pk)
    testimonial.delete()
    return redirect('testimonial_dashboard')

@login_required
def edit_testimonial(request, pk):
    testimonial = get_object_or_404(ClientTestimonial, pk=pk)
    if request.method == 'POST':
        form = ClientTestimonialForm(request.POST, request.FILES, instance=testimonial)
        if form.is_valid():
            form.save()
            return redirect('testimonial_dashboard')
    else:
        form = ClientTestimonialForm(instance=testimonial)

    return render(request, 'page/edit_testimonial.html', {'form': form}) 


def service_list(request):
    service_list = Service.objects.all()
    paginator = Paginator(service_list, 10)  

    page_number = request.GET.get('page')
    services = paginator.get_page(page_number)

    return render(request, 'page/services.html', {'services': services}) 

@login_required
def admin_service_list(request):
    service_list = Service.objects.all().order_by('-id')  
    paginator = Paginator(service_list, 50)

    page_number = request.GET.get('page')
    services = paginator.get_page(page_number)

    return render(request, 'page/admin_services.html', {'services': services})

@login_required
def service_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'page/service_form.html', {'form': form, 'title': 'Create Service'})


@login_required
def service_edit(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'page/service_form.html', {'form': form, 'title': 'Edit Service'})


@login_required
def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        service.delete()
        return redirect('service_list')
    return render(request, 'page/service_confirm_delete.html', {'service': service})




def property_search(request):
    query = request.GET.get('q')
    results = Property.objects.filter(is_active=True)

    if query:
        results = results.filter(
            Q(name__icontains=query) |
            Q(id_no__icontains=query) |
            Q(type__icontains=query) |
            Q(purpose__icontains=query) |
            Q(address__icontains=query)
        )

    return render(request, 'property/property_search.html', {'properties': results, 'query': query})
 

def filtered_properties(request):
    properties = Property.objects.filter(is_active=True)

    # Get filters
    property_type = request.GET.get('property_type')
    location = request.GET.get('location')
    max_bedrooms = request.GET.get('max_bedrooms')
    mini_area = request.GET.get('mini_area')
    max_area = request.GET.get('max_area')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    # Apply filters
    if property_type:
        properties = properties.filter(type=property_type)
    if location:
        properties = properties.filter(address__icontains=location)
    if max_bedrooms:
        properties = properties.filter(bedroom__lte=max_bedrooms)
    if mini_area:
        properties = properties.filter(sqft__gte=mini_area)
    if max_area:
        properties = properties.filter(sqft__lte=max_area)
    if min_price:
        properties = properties.filter(price__gte=min_price)
    if max_price:
        properties = properties.filter(price__lte=max_price)

    # Build a readable filter summary
    filters_applied = []
    if property_type:
        filters_applied.append(f"Type: {property_type}")
    if location:
        filters_applied.append(f"Location: {location}")
    if max_bedrooms:
        filters_applied.append(f"Bedrooms ≤ {max_bedrooms}")
    if mini_area:
        filters_applied.append(f"Min Area: {mini_area} sqft")
    if max_area:
        filters_applied.append(f"Max Area: {max_area} sqft")
    if min_price:
        filters_applied.append(f"Min Price: {min_price} Tk")
    if max_price:
        filters_applied.append(f"Max Price: {max_price} Tk")

    filter_summary = ', '.join(filters_applied)

    context = {
        'properties': properties,
        'filter_summary': filter_summary,
        'property_count': properties.count(),
    }
    return render(request, 'property/filtered_list.html', context)


from .forms import LandBookingForm

def book_land(request):
    if request.method == "POST":
        form = LandBookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Land booking has been submitted successfully! Thanks you.")
            return redirect('book_land') 
        else:
            messages.error(request, "❌ Please correct the errors below and try again.")
    else:
        form = LandBookingForm()
    
    return render(request, 'lands/book_land_form.html', {'form': form})


@login_required
def delete_land_booking(request, booking_id):
    booking = get_object_or_404(LandBooking, id=booking_id)
    if request.method == "POST":
        booking.delete()
        return redirect('admin_dashboard')
    return redirect('admin_dashboard')

@login_required
def land_booking_list(request):
    bookings = LandBooking.objects.all().order_by('-id')  # latest first
    return render(request, 'lands/land_booking_list.html', {'bookings': bookings})  


from django.shortcuts import render, redirect, get_object_or_404
from .models import Jomi, JomiImage
from .forms import JomiForm

def jomi_list(request):
    jomis = Jomi.objects.all().order_by('-created_at')
    return render(request, 'jomi/jomi_list.html', {'jomis': jomis})

def jomi_create(request):
    if request.method == 'POST':
        form = JomiForm(request.POST)
        images = request.FILES.getlist('images')
        if form.is_valid():
            jomi = form.save()
            for img in images:
                JomiImage.objects.create(jomi=jomi, image=img)
            return redirect('jomi_list')
    else:
        form = JomiForm()
    return render(request, 'jomi/jomi_form.html', {'form': form, 'jomi': None})

def jomi_edit(request, pk):
    jomi = get_object_or_404(Jomi, pk=pk)
    if request.method == 'POST':
        form = JomiForm(request.POST, instance=jomi)
        images = request.FILES.getlist('images')
        if form.is_valid():
            form.save()
            for img in images:
                JomiImage.objects.create(jomi=jomi, image=img)
            return redirect('jomi_list')
    else:
        form = JomiForm(instance=jomi)
    return render(request, 'jomi/jomi_form.html', {'form': form, 'jomi': jomi})

def jomi_delete(request, pk):
    jomi = get_object_or_404(Jomi, pk=pk)
    if request.method == 'POST':
        jomi.delete()
        return redirect('jomi_list')
    return render(request, 'jomi/jomi_confirm_delete.html', {'jomi': jomi})

def jomi_image_delete(request, pk):
    image = get_object_or_404(JomiImage, pk=pk)
    jomi_id = image.jomi.id
    if request.method == 'POST':
        image.delete()
    return redirect('jomi_edit', pk=jomi_id)  

def jomi_public_list(request):
    jomis = Jomi.objects.all().order_by('-created_at')
    paginator = Paginator(jomis, 20)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'jomi/jomi_public_list.html', {
        'page_obj': page_obj
    }) 

def investor_policy(request):
    return render(request, 'jomi/investor_policy.html')