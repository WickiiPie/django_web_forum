from django.urls import path, include
from rest_framework.routers import DefaultRouter

from simpleforum.api import views as fv
from rest_framework_simplejwt.views import (
    TokenObtainPairView
    # TokenRefreshView
)


router = DefaultRouter()
router.register(r"forum", fv.ForumViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("forum/<int:id>/subforum/",
         fv.SubForumViewSet.as_view(), name="subforum_list"),
    path("forum/subforum/<int:id>/",
         fv.ThreadViewSet.as_view(), name="threadviewset"),
    path("node/<int:id>/", fv.PostViewSet.as_view(), name="threaddetailview"),
    path("node/thread/<int:id>/",
         fv.ThreadDetailViewSet.as_view(), name="threadview"),
    path("forum/subforum/<int:id>/",
         fv.ThreadCreateViewSet.as_view(), name="threadCreate"),

    path('login/', TokenObtainPairView.as_view()),

    path('register/', fv.RegisterView.as_view(), name='auth_register'),
    # path("questions/<slug:slug>/answers/",
    #      qv.AnswerListAPIView.as_view(),
    #      name="answer-list"),

    # path("questions/<slug:slug>/answer/",
    #      qv.AnswerCreateAPIView.as_view(),
    #      name="answer-create"),

    # path("answers/<int:pk>/",
    #      qv.AnswerRUDAPIView.as_view(),
    #      name="answer-detail"),

    # path("answers/<int:pk>/like/",
    #      qv.AnswerLikeAPIView.as_view(),
    #      name="answer-like")
]
