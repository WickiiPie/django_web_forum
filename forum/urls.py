from django.urls import path

from . import views

from forum.views import (
    # home_view,
    forum_list_view,
    sub_forum_list_view,
    thread_list_view,
    thread_detail_view,
    # post_create,
    thread_create_view,
    thread_search_view,
    thread_edit_view,
    thread_delete_view,
)

app_name = 'forum'

urlpatterns = [
    #forum
    path('', forum_list_view, name='forum_list_view'),
    path('<int:id>/', sub_forum_list_view, name='sub_forum_list_view'),
    path('<int:id>/thread/', thread_list_view, name='thread_list_view'),

    # how to pasrse multiple id
    # path('<int:sub_forum_id>/thread/<int:id>', thread_detail_view, name='thread_detail_view'),
    path('<int:id>/details/', thread_detail_view, name='thread_detail_view'),
    path('<int:sub_forum_id>/thread/create/', thread_create_view, name='thread_create_view'),
    path('thread/search/', thread_search_view, name='thread_search_view'),

    path('<int:id>/details/edit', thread_edit_view, name='thread_edit_view'),
    path('<int:id>/details/delete', thread_delete_view, name='thread_delete_view'),
]