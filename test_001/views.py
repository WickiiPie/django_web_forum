from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect

from django.contrib.auth import authenticate, login, logout

from django.urls import reverse

from .forms import UserLoginForm, UserRegistrationForm

def home_view(request):

    print(request)
    print(request.user)
    return render(request, "base.html")


def user_login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if(form.is_valid()):
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('forum:forum_list_view'))
                else:
                    return HttpResponse("User is not active")
            else:
                return HttpResponse("Not a user")
    else:
        form = UserLoginForm()

    context = {
        'form':form,
    }

    return render(request, 'login.html', context)


def user_logout_view(request):
    logout(request)
    # if request.method == 'POST':
    #     form = UserLoginForm(request.POST)
    #     if(form.is_valid()):
    #         username = request.POST['username']
    #         password = request.POST['password']
    #         user = authenticate(username=username, password=password)
    #         if user:
    #             if user.is_active:
    #                 login(request, user)
    #                 return HttpResponseRedirect(reverse('forum:forum_list_view'))
    #             else:
    #                 return HttpResponse("User is not active")
    #         else:
    #             return HttpResponse("Not a user")
    # else:
    #     form = UserLoginForm()

    # context = {
    #     'form':form,
    # }

    # return render(request, 'forum/forum_list.html')   # view not working
    # return redirect('forum:forum_list_view')  # ok
    return HttpResponseRedirect(reverse('forum:forum_list_view')) #ok

def user_register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            #set password for new user
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return redirect('forum:forum_list_view')
    else:
        form = UserRegistrationForm()
    context = {
        'form':form,
    }

    return render(request, 'register.html', context)
