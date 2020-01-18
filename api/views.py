from django.core.files.storage import FileSystemStorage
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from .models import Post, Installer
from .serializers import PostSerializer, InstallerSerializer, FileSerialzer


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
    serializer_class = FileSerialzer

    def put(self, request, format=None):
        if 'file' not in request.data:
            raise ParseError("Empty content")

        folder = 'media'
        f = request.data['file']
        fs = FileSystemStorage(location=folder)  # defaults to   MEDIA_ROOT
        filename = fs.save(f.name, f)
        print("filename", filename)
        file_url = fs.url(filename)
        print(file_url)

        return Response(status=HTTP_201_CREATED)

    def post(self, request):
        print("request.POST", request.POST)
        print("request.FILES", request.FILES)

        form = {
            'title': request.POST.get('title'),
            'photo': request.data['file']
        }
        serializer = FileSerialzer(data=form)
        if serializer.is_valid():
            serializer.save()
            return Response(status=HTTP_201_CREATED)

        return Response(status=HTTP_400_BAD_REQUEST)
