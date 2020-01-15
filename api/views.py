from rest_framework import viewsets
from .serializers import PostSerializer, InstallerSerializer
from .models import Post, Installer
from rest_framework import permissions


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
