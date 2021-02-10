from django.shortcuts import render, reverse
from django.shortcuts import Http404, HttpResponseRedirect, HttpResponse

from .models import(
    forum,
    sub_forum,
    thread,
    post,
)

from .forms import ThreadCreateForm
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

    sub_forum_id = id
    context = {
        'object_list': queryset,
        'get_sub_forum_id' : sub_forum_id,
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

def thread_create_view(request, sub_forum_id):
    form = ThreadCreateForm()

    if request.method == 'POST':
        print('Post is ', request.POST)
        print(sub_forum_id)
        form = ThreadCreateForm(request.POST)
        if form.is_valid():
            new_thread = form.save(commit=False)

            # TODO if user is logged in, else can not create
            current_user = request.user
            new_thread.user_id = current_user
            new_thread.sub_forum_id = sub_forum.objects.get(id=sub_forum_id)
            new_thread = form.save()
        print(form)

        queryset = thread.objects.filter(sub_forum_id=sub_forum_id)
        context = {
            "object_list" : queryset,
        }
        # TODO return to show thread list on the relational subform id
        # return render(request, "forum/thread_list.html", context)
        # return HttpResponseRedirect(reverse('forum:thread_list_view'))
        return HttpResponseRedirect('/forum/%d/thread'%sub_forum_id) #ok
        # return HttpResponse("thread created") # display only response
    else:
        form = ThreadCreateForm()

    context = {
        'form':form
    }
    return render(request, "forum/thread_create.html", context)
