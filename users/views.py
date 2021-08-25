from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import UserRegisterForm ,UserUpdateForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model

# Create your views here.

def register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)  

        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            messages.success(request,f'You are signed up as {username}')
            return redirect('login')
    else: 
        form = UserRegisterForm()

    return render(request,'users/register.html',{'form':form,'title':"Registration"}) 
@login_required
def editProfile(request):
    if request.method=='POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)

        if u_form.is_valid():
            u_form.save()
            messages.success(request,f'profile updated successfully !')
            return redirect('editProfile')

    else:
        u_form = UserUpdateForm(instance=request.user)
    context = {
            'u_form':u_form,
            'title':"Update profile"
         }

    return render(request,'users/editProfile.html',context=context)

@login_required
def editUsersList(request):
    User = get_user_model()
    users = User.objects.all()
    context = {
        'users': users,
        'title':"Edit Users List"
    }
    return render(request,'users/editUsersList.html',context)

