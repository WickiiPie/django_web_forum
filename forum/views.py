from django.shortcuts import render

# Create your views here.


def home_view(request):

    print(request)
    print(request.user)

    return render(request, "base.html")