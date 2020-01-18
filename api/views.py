from rest_framework import viewsets, views
from .serializers import PostSerializer, InstallerSerializer
from .models import Post, Installer
from rest_framework import permissions
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response


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


class FileUploadView(views.APIView):
    # parser_classes = (FileUploadParser,)

    def put(self, request, filename, format=None):
        file_obj = request.FILES['file']
        print(filename, format)
        print(file_obj)
        # do some stuff with uploaded file
        return Response(status=204)
