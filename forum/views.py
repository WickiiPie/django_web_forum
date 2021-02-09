from django.shortcuts import render
from django.shortcuts import Http404, HttpResponseRedirect

from .models import(
    forum,
    sub_forum,
    thread,
    post,
)
# Create your views here.
def forum_list_view(request):

    queryset = forum.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "forum/forum_list.html", context)

def sub_forum_list_view(request, id):

    try:
        queryset = sub_forum.objects.filter(forum_id=id)
    except sub_forum.DoesNotExist:
        raise Http404
    context = {
        'object_list': queryset,

    }
    print(context)

    return render(request, "forum/sub_forum_list.html", context)

def thread_list_view(request, id):

    try:
        queryset = thread.objects.filter(sub_forum_id=id)
    except thread.DoesNotExist:
        raise Http404
    context = {
        'object_list': queryset
    }
    print(context)

    return render(request, "forum/thread_list.html", context)

# def thread_detail_view(request, sub_forum_id, id):
def thread_detail_view(request, id):
    try:
        queryset = thread.objects.filter(id=id)
        querypost = post.objects.filter(thread_id=id)
    except thread.DoesNotExist:
        raise Http404

    context = {
        'object_list' :queryset,
        'post': querypost
    }

    print(context)

    return render(request, "forum/thread_detail.html", context)
