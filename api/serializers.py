from rest_framework.serializers import ModelSerializer
from main.models import Category, Post

# ----------- category list and detail serializer --------------------
""" category serializer list"""
class CategorySerializerList(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

""" category serializer detail """
class CategorySerializerDetail(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


# ----------- --post list and detail serializer ------------------------
""" post serializer list """
class PostSerializerList(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'banner_img', 'category'  ]

""" post serializer detail """
class PostSerializerDetail(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'