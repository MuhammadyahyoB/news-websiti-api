from main.models import Category, Post
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import serializers

# ----------------------------------- category list, detail --------------------------

@api_view(['GET'])
def category_list(request):
    """List categories"""
    data = Category.objects.all()
    serializers_data = serializers.CategorySerializerList(data, many=True) # json

    return Response(serializers_data.data)

@api_view(['GET'])
def category_detail(request, id):
    """ detail category"""
    data = Category.objects.get(id=id)
    serializers_data = serializers.CategorySerializerDetail(data, many=False) # json

    return Response(serializers_data.data)


# ----------------------------------- post list, detail ----------------------------

@api_view(['GET'])
def post_list(request):
    """List posts"""
    data = Post.objects.all()
    serializers_data = serializers.PostSerializerList(data, many=True) # json
    
    return Response(serializers_data.data)

@api_view(['GET'])
def post_detail(request, id):
    """ detail post"""
    data = Post.objects.get(id=id)
    serializers_data = serializers.PostSerializerDetail(data, many=False) # json
    
    return Response(serializers_data.data)
