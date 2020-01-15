# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    temp = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'id',
            'user',
            'title',
            'subtitle',
            'content',
            'temp',
            'created_at',
        )
        read_only_fields = ('created_at',)

    def get_temp(self, obj):
        return obj.temp()
