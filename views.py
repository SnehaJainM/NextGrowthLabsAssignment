from django.shortcuts import render
# "C:\Users\1234\Documents\Django_Tutorials_FollowUp\firstapp"
# Create your views here.
import json

from .models import *
from django.http import HttpResponse 
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required,user_passes_test

from django.db.models import Sum

def home(request):
    data={
        'message':'Welcome to the APPS TRACKER - where you track the number of apps downloaded and rewards are presented to you based on the downloads/ task completions'
    }
    response = HttpResponse(json.dumps(data), content_type='application/json')
    return response


def is_admin(user):
    return user.groups.filter(name='Admins').exists()

@login_required(login_url="/login/")
@user_passes_test(is_admin)
def adminn(request):
    
    if request.method == "POST":
        data=request.POST
        name=data.get('app_name')
        link=data.get('app_link')
        category=data.get('app_category')
        subcategory=data.get('app_subcategory')
        points=data.get('app_points')
        
        #save
        admin_app=AdminApps.objects.create(
           app_name = name,
           app_link = link,
           app_category = category,
           app_subcategory = subcategory,
           app_points= points
        )
        admin_app.save()
        
        #print(name,link,category,subcategory,points)
    return render(request,'adminn.html')



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            raw_password = form.cleaned_data.get('password1')
            username = form.cleaned_data.get('username')
            #print(f"Username: {username}, Password: {raw_password}")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.groups.filter(name='Admins').exists():
                return redirect('admin-page') 
            return redirect('profile')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

from .models import AdminApps

@login_required(login_url="/login/")
def registered_apps_view(request):
    
    apps = AdminApps.objects.all().distinct().order_by('-app_points')

    return render(request, 'registered_apps.html', {'apps': apps})


@login_required(login_url="/login/")
def profile(request):
    user = request.user
    print(user)
    user_apps = UserApps.objects.all().filter(user=user)
    total_points = 0
    for app in user_apps:
        print(app)
        if app.admin_app: 
            total_points += app.admin_app.app_points
        
    
    context = {
        'user': user,
        'total_points':total_points
    }
    return render(request, 'profile.html', context)





@login_required(login_url="/login/")
def tasks(request):
    if request.method == 'POST':
        data=request.POST
        #print(data)
        app_link=data.get('app_link')
        app_name=data.get('app_name')
        app_screenshot = request.FILES.get('app_screenshot')
        
        user_apps=UserApps.objects.create(
        app_name = app_name,
        app_link = app_link,
        app_screenshot= app_screenshot
        )
        user_apps.save()
        
        print(f'App name : {app_name} Link: {app_link} Screenshot : {app_screenshot}')
        
        messages.success(request, 'Your action was successful!')
    return render(request, 'tasks.html')


@login_required(login_url="/login/")
def task_apps(request):
    
    apps = AdminApps.objects.all().order_by('-app_points')

    return render(request, 'regi_apps_users.html', {'apps': apps})



@login_required(login_url="/login/")
def completed_tasks(request):
    
    user_apps = UserApps.objects.all().distinct()
    admin_apps=AdminApps.objects.all()
    user_app_name =user_apps[0].app_name
    context={'user_apps': user_apps,'admin_apps':admin_apps,'user_app_name':user_app_name}
    return render(request, 'completed_tasks.html',context)




