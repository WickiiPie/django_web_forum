from django.shortcuts import render, reverse
from django.shortcuts import (
    Http404,
    HttpResponseRedirect,
    HttpResponse,
    get_object_or_404
)

from .models import(
    Forum,
    SubForum,
    Thread,
    Post,
    UserProfile,
)

from .forms import ThreadCreateForm, ThreadEditForm, PostCreateForm
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

# Create your views here.
def forum_list_view(request):
    queryset = Forum.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "forum/forum_list.html", context)


def sub_forum_list_view(request, id):
    try:
        queryset = SubForum.objects.filter(forum_id=id)
    except SubForum.DoesNotExist:
        raise Http404
    context = {
        'object_list': queryset,

    }
    print(context)

    return render(request, "forum/sub_forum_list.html", context)


def thread_search_view(request):
    query = request.GET.get('q')

    if query:
        object_list = Thread.objects.filter(
            Q(title__icontains=query)
        )
    else:
        # object_list = Thread.objects.all().order_by('-id') # incase no meta class in model
        object_list = Thread.objects.all()

    search_paginator = Paginator(object_list, 2)    # max items in one page 5
    page = request.GET.get('page')

    try:
        object_list = search_paginator.page(page)
    except PageNotAnInteger:
        object_list = search_paginator.page(1)
    except EmptyPage:
        object_list = search_paginator.page(search_paginator.num_pages)

    context = {
        'object_list': object_list,
    }

    return render(request, "forum/thread_search.html", context)


def thread_list_view(request, slug):
    id = SubForum.objects.get(slug=slug).id
    try:
        queryset = Thread.objects.filter(sub_forum_id=id)
    except Thread.DoesNotExist:
        raise Http404

    sub_forum_id = id
    context = {
        'object_list': queryset,
        'get_sub_forum_id': sub_forum_id,
    }
    print(context)

    return render(request, "forum/thread_list.html", context)


def thread_detail_view(request, id):
    try:
        queryset = Thread.objects.filter(id=id)
        querypost = Post.objects.filter(thread_id=id)
    except Thread.DoesNotExist:
        raise Http404

    sub_forum_id = queryset.get().sub_forum_id.id
    if request.method == 'POST':
        post_comment = PostCreateForm(request.POST or None)
        if post_comment.is_valid():
            new_post = post_comment.save(commit=False)
            current_user = request.user
            new_post.user_id = current_user
            new_post.sub_forum_id = SubForum.objects.get(id=sub_forum_id)
            new_post.thread_id = Thread.objects.get(id=id)
            new_post = post_comment.save()

            return HttpResponseRedirect(
                reverse('simpleforum:thread_detail_view', kwargs={"id": id})
                )
    else:
        post_comment = PostCreateForm()

    context = {
        'object_list': queryset,
        'post': querypost,
        'post_comment': post_comment,
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
            new_thread.sub_forum_id = SubForum.objects.get(id=sub_forum_id)
            new_thread = form.save()

            slug = new_thread.sub_forum_id.slug  # ok
            print("slug is :", slug)
            # return HttpResponseRedirect('/forum/%s/thread' % slug)  # ok
            return HttpResponseRedirect(reverse('simpleforum:thread_list_view',
                                                kwargs={"slug": slug}))

        print(form)
        messages.success(request, "Thread created succesffully")
    else:
        form = ThreadCreateForm()

    context = {
        'form': form
    }
    return render(request, "forum/thread_create.html", context)


def thread_edit_view(request, id):
    obj = get_object_or_404(Thread, id=id)

    # if logged in user is not the same as the user creating the Thread
    if obj.user_id != request.user:
        raise Http404()

    if request.method == 'POST':
        form = ThreadEditForm(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()

            print(form)
            messages.success(
                request, "{} has succesfully been updated".format(obj.title))
            # return HttpResponseRedirect(reverse('simpleforum:thread_detail_view') )
            # return HttpResponseRedirect('/forum/%d/details' % id)  # ok
            return HttpResponseRedirect(
                reverse('simpleforum:thread_detail_view',
                        kwargs={"id": id}))
    else:
        form = ThreadEditForm(instance=obj)

    context = {
        'form': form,
        'Thread': obj,
    }
    return render(request, 'forum/thread_edit.html', context)


def thread_delete_view(request, id):
    obj = get_object_or_404(Thread, id=id)
    if obj.user_id != request.user:
        raise Http404()

    # sub_forum_id = obj.sub_forum_id.id
    sub_forum_slug = obj.sub_forum_id.slug
    obj.delete()
    print("Thread id", id, " + is deleted")
    messages.warning(request,
                     "{} has succesfully been deleted".format(obj.title))
    return HttpResponseRedirect(
                reverse('simpleforum:thread_list_view',
                        kwargs={"slug": sub_forum_slug}))


def post_reply_view(request, thread_id, parent_id):
    form = PostCreateForm()
    if request.method == 'POST':
        print('Post is ', request.POST)
        print("thread_id: ", thread_id)
        print("parent_id: ", parent_id)

        form = PostCreateForm(request.POST)
        if form.is_valid():
            new_reply = form.save(commit=False)

            # # TODO if user is logged in, else can not create
            new_reply.thread_id = Thread.objects.get(id=thread_id)
            new_reply.parent_id = Post.objects.get(id=parent_id)
            new_reply.user_id = request.user
            new_reply = form.save()
        print(new_reply)
        messages.success(request, "Reply created")

        return HttpResponseRedirect(
                reverse('simpleforum:thread_detail_view',
                        kwargs={"id": new_reply.thread_id.id}))

    else:
        form = PostCreateForm()

    queryset = Post.objects.filter(id=parent_id)
    context = {
        'form': form,
        'object_list': queryset
    }
    return render(request, "forum/post_reply.html", context)
