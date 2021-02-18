from django.shortcuts import (
    render,
    HttpResponseRedirect,
    HttpResponse,
    redirect,
)
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import (
    UserLoginForm,
    UserRegistrationForm,
    UserEditForm,
    ProfileEditForm,
)
from simpleforum.models import UserProfile

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
                    return HttpResponseRedirect(
                        reverse('simpleforum:forum_list_view'))
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
    return HttpResponseRedirect(reverse('simpleforum:forum_list_view'))  # ok


def user_register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            # set password for new user
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            # link to UserProfile model
            UserProfile.objects.create(user=new_user)

            return redirect('simpleforum:forum_list_view')
    else:
        form = UserRegistrationForm()
    context = {
        'form': form,
    }

    return render(request, 'register.html', context)

# decorator
@login_required
def edit_profile_view(request):
    if request.method == 'POST':
        user_form = UserEditForm(data=request.POST or None,
                                 instance=request.user)
        profile_form = ProfileEditForm(data=request.POST or None,
                                       instance=request.user.profile,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect('simpleforum:forum_list_view')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'forum/edit_profile.html', context)