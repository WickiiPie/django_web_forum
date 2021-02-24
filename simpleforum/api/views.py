from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from simpleforum.models import Thread
from simpleforum.api.serializers import ThreadSerializer

@api_view(["GET", "POST"])
def thread_list_create_api_view(request):
    if request.method == "GET":
        threads = Thread.objects.all()
        serializer = ThreadSerializer(threads, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ThreadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
