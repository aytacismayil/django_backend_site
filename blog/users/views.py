from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm   // only views form=UserCreationForm()
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm  
from django.contrib.auth import views as auth_views #login
from django.contrib.auth.decorators import login_required



def register(request):
    if request.method =="POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Your account has been created! You are now able to Log In')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request,'users/register.html',{'form':form})


@login_required
def profile(request):
    if request.method == "POST":
        u_form= UserUpdateForm(request.POST,
                               instance=request.user)
        p_form= ProfileUpdateForm(request.POST,
                                  request.FILES or None,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            obj = p_form.save(commit=False)
            obj.save()
            print('dsadada',request.FILES)
            messages.success(request,f'Your account has been update')
            return redirect('profile')
    else:
        u_form= UserUpdateForm(instance=request.user)
        p_form= ProfileUpdateForm(instance=request.user.profile)

    context={
        'u_form':u_form,
        'p_form':p_form,
    }
    return render(request,'users/profile.html',context)