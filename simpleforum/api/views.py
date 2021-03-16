from simpleforum.models import Forum, SubForum, Thread, Post
from .serializers import ForumSerializer, SubForumSerializer, ThreadSerializer, PostSerializer
from rest_framework import generics, status, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from simpleforum.api.permissions import IsAuthorOrReadOnly
# from simpleforum.api.serializers import AnswerSerializer, QuestionSerializer
# from simpleforum.models import Answer, Question


class ForumViewSet(viewsets.ModelViewSet):

    queryset = Forum.objects.all().order_by("created_at")
    # queryset = Forum.objects.all()
    lookup_field = "id"
    serializer_class = ForumSerializer
    # permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    # user cannot create a forum
    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


# class SubForumViewSet(generics.ListAPIView):
#     queryset = SubForum.objects.filter(forum_id=id).order_by("id")
#     lookup_field = "id"
#     serializer_class = SubForumSerializer


class SubForumViewSet(generics.ListAPIView):
    """Provide the answers queryset of a specific question instance."""
    serializer_class = SubForumSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        id = self.kwargs.get("id")
        return SubForum.objects.filter(forum_id=id)


class ThreadViewSet(generics.ListAPIView, generics.CreateAPIView):
    serializer_class = ThreadSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        id = self.kwargs.get("id")
        return Thread.objects.filter(sub_forum_id=id)


    # class ThreadCreateViewSet():
    """Allow users to answer a question instance if they haven't already."""
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    # permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):

        print("dssfadf", self.request.user)

        request_user = self.request.user
        # kwarg_slug = self.kwargs.get("slug")
        kwarg_slug = self.kwargs.get("id")
        sub_forum_id = get_object_or_404(SubForum, id=kwarg_slug)

        # if question.answers.filter(author=request_user).exists():
        #     raise ValidationError("You have already answered this Question!")

        serializer.save(user_id=request_user, sub_forum_id=sub_forum_id)


class PostViewSet(generics.ListAPIView):
    serializer_class = PostSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        id = self.kwargs.get("id")
        return Post.objects.filter(thread_id=id).order_by("created_at")


class ThreadDetailViewSet(generics.ListAPIView):
    serializer_class = ThreadSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        id = self.kwargs.get("id")
        return Thread.objects.filter(id=id)


class ThreadCreateViewSet(generics.CreateAPIView):
    """Allow users to answer a question instance if they haven't already."""
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        request_user = self.request.user
        # kwarg_slug = self.kwargs.get("slug")
        kwarg_slug = self.kwargs.get("id")
        sub_forum_id = get_object_or_404(SubForum, id=kwarg_slug)
        print(request_user)
        # if question.answers.filter(author=request_user).exists():
        #     raise ValidationError("You have already answered this Question!")

        serializer.save(user_id=request_user.id, sub_forum_id=sub_forum_id)
# class SubForumListViewSet(generics.ListAPIView):
#     serializer_class = SubForumSerializer
#     # permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         id = self.kwargs.get("id")
#         return SubForum.objects.filter(forum_id=id)


from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer