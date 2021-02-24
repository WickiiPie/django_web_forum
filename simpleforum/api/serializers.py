from rest_framework import serializers
from datetime import datetime
# from django.utils.timesince import timesince
from django.utils import timezone
from simpleforum.models import Thread, Post

## normal serializer
# class ThreadSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)

#     # user_id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField()
#     content = serializers.CharField()
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)
#     # sub_forum_id = serializers.IntegerField(read_only=True)

#     def create(self, validated_data):
#         print(validated_data)
#         return Thread.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         print(validated_data)
#         instance.user_id = validated_data.get('user_id', instance.user_id)
#         instance.title = validated_data.get('title', instance.title)
#         instance.content = validated_data.get('content', instance.content)
#         instance.save()
#         # instance.sub_forum_id = validated_data.get('sub_forum_id', instance.sub_forum_id)
#         return Thread.objects.create(**validated_data)


# model serializers
class ThreadSerializer(serializers.ModelSerializer):

    # add extra fields
    time_since_publication = serializers.SerializerMethodField()

    class Meta:
        model = Thread
        exclude = ("id",)

    def get_time_since_publication(self, object):
        publication_date = object.created_at
        ##issue: can't subtract offset-naive and offset-aware datetimes django
        # publication_date = publication_date.replace(tzinfo=None)]

        now = timezone.localtime()
        time_delta = now - publication_date
        return time_delta

    def validate(self, data):
        if data["title"] == data["content"]:
            raise serializers.ValidationError("title and content must be different")
        return data

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("title needs at least 5 chars")
        return value

