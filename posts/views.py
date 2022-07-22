from rest_framework import generics, permissions
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            return Post.objects.all()

        return Post.objects.filter(author=user)




class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = []
    queryset = Post.objects.all()
    serializer_class = PostSerializer

