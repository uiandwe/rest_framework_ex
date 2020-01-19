# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Post
from .domain.comment import Comment


class Postserializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)


class CommentSerializer(serializers.Serializer):
    user = UserSerializer()
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

    def validate_content(self, value):
        # 커스텀 valid content
        print("validate_content", value)
        return value

    def validate(self, data):
        # 멀티 필드 valid
        print(data)
        return data

    def create(self, validated_data):
        return Comment(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)

        return instance
