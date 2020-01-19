# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED

from .models import Post
from .domain.comment import Comment
from .serializers import Postserializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = Postserializer

    # /blog/post/
    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()

        search = self.request.query_params.get('search', '')
        if search:
            queryset = queryset.filter(message__icontains=search)
        return queryset

    # get  /blog/post/get_django/
    @action(detail=False)
    def get_django(self, request):
        queryset = self.get_queryset().filter(message__icontains='django')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # patch  /blog/post/1/set_modified/
    @action(detail=True, methods=['patch'])
    def set_modified(self, request, pk):
        request_data = request.POST.dict()
        instance = self.get_object()
        instance.message = instance.message + request_data['message']
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class CommentViewSet(viewsets.ViewSet):
    serializer_class = CommentSerializer

    def retrieve(self, request, pk=None):
        comment = Comment(email='hare@naver.com', content='test')

        comment_serializer = CommentSerializer(data=comment.__dict__)

        if comment_serializer.is_valid():
            return Response(comment_serializer.data)
        return Response(status=HTTP_400_BAD_REQUEST)

    def create(self, request):
        # get data
        result_data = request.data

        # set class
        comment = Comment(email=result_data['email'], content=result_data['content'], created=result_data['created'])

        # set serializer
        comment_serializer = CommentSerializer(data=comment.__dict__)

        if comment_serializer.is_valid():
            return Response(status=HTTP_201_CREATED)
        return Response(status=HTTP_400_BAD_REQUEST)
