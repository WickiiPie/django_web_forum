from rest_framework import serializers

from simpleforum.models import Thread

class ThreadSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    # user_id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    content = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    # sub_forum_id = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        print(validated_data)
        return Thread.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print(validated_data)
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        # instance.sub_forum_id = validated_data.get('sub_forum_id', instance.sub_forum_id)
        return Thread.objects.create(**validated_data)
