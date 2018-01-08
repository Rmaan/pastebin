from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from blog.models import Blog
from blog.serializers import BlogListSerializer


class BlogListAPIView(ListAPIView):
    queryset = Blog.objects.filter(publish=True, draft=False)
    serializer_class = BlogListSerializer
    permission_classes = [IsAuthenticated]
