from django.shortcuts import render


from .models import(
    forum,
    sub_forum
)
# Create your views here.


def home_view(request):

    print(request)
    print(request.user)

    return render(request, "base.html")

def forum_list_view(request):

    queryset = forum.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "forum_list.html", context)


def sub_forum_list_view(request, pk):

    # queryset = sub_forum.objects.all(forum_id=id)
    # context = {
    #     'object_list': queryset
    # }
    # return render(request, "sub_forum_list.html", context)
    print("hello")
    print(pk)

    # guard for out of range

    # obj = get_object_or_404(NewProduct, id=my_id)

    #guard with http404
    try:
        queryset = sub_forum.objects.filter(forum_id=pk)
    except sub_forum.DoesNotExist:
        raise Http404

    # obj = sub_forum.objects.get(id=pk)
    context = {
        'object_list': queryset
    }
    print(context)
    return render(request, "sub_forum_list.html", context)