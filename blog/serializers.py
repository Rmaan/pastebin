from rest_framework.relations import HyperlinkedIdentityField
from rest_framework.serializers import ModelSerializer

from blog.models import Blog


class BlogListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(view_name="blog_api:post_detail", lookup_field="slug")

    class Meta:
        model = Blog
        fields = [
           'url',
           'title',
           'category',
           'date',
           'publish',
           'draft'
         ]
