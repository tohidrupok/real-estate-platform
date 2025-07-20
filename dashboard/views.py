from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import PropertyImage, Property, Video, Land, LandImage, TeamMember
from .forms import PropertyForm, VideoForm, LandForm, TeamMemberForm
from django.contrib.auth.models import User, Group 



def public_home(request):
    video = Video.objects.last()  

    featured_properties = Property.objects.filter(is_active=True, featured=True).order_by('-date_posted')[:9]

    # Paginated all properties
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
    return render(request, 'dashboard/home.html', {
        'video': video,
        'featured_properties': featured_properties,
        'properties': properties,
        'members': members
    })

def about(request):
    return render(request, 'dashboard/about.html') 

def contact(request):
    return render(request, 'dashboard/contact.html') 


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
                return redirect('manager_dashboard')
        else:
            return render(request, 'dashboard/login.html', {'error': 'Invalid login'})
    return render(request, 'dashboard/login.html')

from django.contrib.auth import logout


def user_logout(request):
    logout(request)
    return redirect('home') 




@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_dashboard(request):
    total_properties = Property.objects.count()
    total_managers = User.objects.filter(groups__name='Manager').count()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(request, 'dashboard/admin_dashboard.html', {
                'error': 'Username already exists',
                'managers': get_managers(),
                'total_properties': total_properties,
                'total_managers': total_managers
            })

        user = User.objects.create_user(username=username, password=password)
        group = Group.objects.get(name='Manager')
        user.groups.add(group)

        return render(request, 'dashboard/admin_dashboard.html', {
            'success': 'Manager created successfully',
            'managers': get_managers(),
            'total_properties': total_properties,
            'total_managers': total_managers
        })

    return render(request, 'dashboard/admin_dashboard.html', {
        'managers': get_managers(),
        'total_properties': total_properties,
        'total_managers': total_managers
    })

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



def property_list_manage(request):
    properties = Property.objects.all()
    # featured_properties = Property.objects.filter(featured=True).order_by('-date_posted')[:4]
    featured_properties = Property.objects.all()
    print(featured_properties)
    return render(request, 'property/property_list.html', {
        'properties': properties,
        'featured_properties': featured_properties,
    })


def property_detail(request, slug):
    property = get_object_or_404(Property, slug=slug)
    featured_properties = Property.objects.filter(featured=True).order_by('-date_posted')[:4]
    return render(request, 'property/property_detail.html', {'property': property, 'featured_properties': featured_properties,})



def property_create(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        images = request.FILES.getlist('images')
        if form.is_valid():
            property = form.save()
            for img in images:
                PropertyImage.objects.create(property=property, image=img)
            return redirect('property_list')
    else:
        form = PropertyForm()
    return render(request, 'property/property_form.html', {'form': form})



def property_update(request, slug):
    property = get_object_or_404(Property, slug=slug)
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property)
        if form.is_valid():
            form.save()
            return redirect('property_detail', slug=property.slug)
    else:
        form = PropertyForm(instance=property)
    return render(request, 'property/property_form.html', {'form': form})


def property_delete(request, slug):
    property = get_object_or_404(Property, slug=slug)
    if request.method == 'POST':
        property.delete()
        return redirect('property_list')
    return render(request, 'property/property_confirm_delete.html', {'property': property}) 

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def property_list(request):
    property_list = Property.objects.filter(is_active=True).order_by('-date_posted')
    
    # Setup paginator
    paginator = Paginator(property_list, 15)  # Show 15 properties per page
    page = request.GET.get('page')

    try:
        properties = paginator.page(page)
    except PageNotAnInteger:
        properties = paginator.page(1)
    except EmptyPage:
        properties = paginator.page(paginator.num_pages)
    
    featured_properties = Property.objects.filter(featured=True, is_active=True).order_by('-date_posted')[:4]

    return render(request, 'property/property_listing.html', {'properties': properties, 'featured_properties': featured_properties,})



def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VideoForm()
    return render(request, 'dashboard/upload_video.html', {'form': form})


def land_create_view(request):
    if request.method == 'POST':
        form = LandForm(request.POST, request.FILES)
        images = request.FILES.getlist('extra_images')  # Multiple image field

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

def land_delete(request, pk):
    land = get_object_or_404(Land, pk=pk)
    if request.method == 'POST':
        land.delete()
        return redirect('land_list')
    return render(request, 'lands/land_confirm_delete.html', {'land': land})

def land_detail(request, pk):
    land = get_object_or_404(Land, pk=pk)
    return render(request, 'lands/land_detail.html', {'land': land})


#            Team member                 Team member                 Team member                 Team member  #

def team_member_list(request):
    members = TeamMember.objects.all()
    return render(request, 'team/member_list.html', {'members': members})

# Create a new team member
def team_member_create(request):
    if request.method == 'POST':
        form = TeamMemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('team_member_list')
    else:
        form = TeamMemberForm()
    return render(request, 'team/member_form.html', {'form': form})

# Update an existing member
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

# Delete a member
def team_member_delete(request, pk):
    member = get_object_or_404(TeamMember, pk=pk)
    if request.method == 'POST':
        member.delete()
        return redirect('team_member_list')
    return render(request, 'team/member_confirm_delete.html', {'member': member})

def team_member_detail(request, pk):
    member = get_object_or_404(TeamMember, pk=pk)
    return render(request, 'team/member_detail.html', {'member': member}) 


