from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.conf import settings
# from http.client import HTTPResponse
import os
import string
from urllib import response

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
# from django.shortcuts import render, redirect
from workApp.models import  User_Info,Task,Bid
# from django.contrib import auth, messages


# Create your views here.
def home(request):
    return render(request, 'Index.html')
def Sev(request):
    return render(request, 'Services.html')

def Conts(request):
    return render(request, 'Contacts.html')



@login_required
def bid(request, task_id):
    # Fetch the task object from the database using its ID
    task = get_object_or_404(Task, pk=task_id)

    if request.method == 'POST':
        # Process the form submission if the request method is POST
        bid_price = float(request.POST.get('bid_price'))
        if bid_price >= task.price:
            # Save the new bid to the database
            bid = Bid.objects.create(
                task=task,
                user=request.user,
                price=bid_price,
            )
            bid.save()

            # Redirect the user to the task detail page
            return redirect('task_detail', task_id=task.pk)
        else:
            # Display an error message if the bid price is lower than the task price
            error_message = 'Bid price must be greater than or equal to task price.'
            return render(request, 'bid.html', {'task': task, 'error_message': error_message})
    else:
        # Display the bidding page with the task details
        return render(request, 'bid.html', {'task': task})

def task_list(request):
    if request.method == 'POST':
        user = request.user
        document = request.FILES['document']
        description = request.POST['description']
        duration = request.POST['duration']
        price = request.POST['price']

        task = Task(user=user, document=document, description=description, duration=duration, price=price)
        task.save()
        
        return redirect('Available')
    else:
         return render(request, 'Task.html')

        
  

def Available(request):
    tasks=Task.objects.all()
    
    return render(request, 'Available.html',{'tasks': tasks})

def Profile(request):
    content=User_Info.objects.all()
    return render(request, 'Profile.html')

def Login(request):
    if request.method == 'POST':
        uName = request.POST['uName']
        pass1 = request.POST['pass1']

        user = auth.authenticate(username=uName, password=pass1)
        if user is not None:
            auth.login(request, user)
            print('login success')
            return redirect('Profile')
        else:
            print('Invalid login details')
            return redirect('Login')

    return render(request, 'Login.html')
    
def Signup(request):
    if request.method == 'POST':
        
        uName = request.POST['uName']
        phone = request.POST['phone']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=uName).exists():
            print('username iko')
            return redirect('Signup')

        if User_Info.objects.filter(phone=phone).exists():
            print('phone iko')
            return redirect('Signup')
        else:


            user = User.objects.create_user(username=uName, password=pass1)
            user.save()
            user1 = User_Info(user=user, username=uName, phone=phone, )
            user1.save()
            print('user created')
            return redirect('Login')


    

    return render(request, 'Signup.html')