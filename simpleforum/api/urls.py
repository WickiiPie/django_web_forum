from django.urls import path
from simpleforum.api.views import (
    thread_list_create_api_view,
    thread_detail_api_view,

    ThreadListCreateAPIView,
    ThreadDetailAPIView
)


urlpatterns = [
    # path("thread_api/", thread_list_create_api_view, name="thread_list_create_api_view"),
    # path("thread_api/<int:pk>/", thread_detail_api_view, name="thread_detail_api_view"),
    path("thread_api/", ThreadListCreateAPIView.as_view(), name="ThreadListCreateAPIView"),
    path("thread_api/<int:pk>/", ThreadDetailAPIView.as_view(), name="ThreadDetailAPIView"),
]
