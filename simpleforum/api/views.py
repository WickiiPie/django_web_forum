from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from simpleforum.models import Thread
from simpleforum.api.serializers import ThreadSerializer
from django.shortcuts import get_object_or_404

@api_view(["GET", "POST"])
def thread_list_create_api_view(request):
    if request.method == "GET":
        threads = Thread.objects.all()
        serializer = ThreadSerializer(threads, many=True)
        return Response(serializer.data)

    # use built in django restframework
    elif request.method == "POST":
        serializer = ThreadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def thread_detail_api_view(request, pk):
    try:
        thread = Thread.objects.get(pk=pk)
    except Thread.DoesNotExist:
        return Response({"error": {
                            "code": 404,
                            "message": "thread not found!"
                        }}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ThreadSerializer(thread)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ThreadSerializer(thread, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        thread.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
