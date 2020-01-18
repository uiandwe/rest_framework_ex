from django.core.files.storage import FileSystemStorage
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.views import APIView

from .models import Post, Installer
from .serializers import PostSerializer, InstallerSerializer


class PostView(viewsets.ModelViewSet):

    queryset = Post.objects.all().select_related('installer')
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class InstallerView(viewsets.ModelViewSet):

    queryset = Installer.objects.all()

    serializer_class = InstallerSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def put(self, request, format=None):
        if 'file' not in request.data:
            raise ParseError("Empty content")

        folder = 'media'
        f = request.data['file']
        fs = FileSystemStorage(location=folder)  # defaults to   MEDIA_ROOT
        filename = fs.save(f.name, f)
        file_url = fs.url(filename)
        print(file_url)

        return Response(status=HTTP_201_CREATED)
