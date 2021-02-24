from django.urls import path
from simpleforum.api.views import thread_list_create_api_view


urlpatterns = [
    path("thread_api/", thread_list_create_api_view, name="thread_list_create_api_view")
]