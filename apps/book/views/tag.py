from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from apps.book.serializer import TagSerializer
from apps.book.models import Tag


@api_view(['GET']) # when [] it means [get] is default
def list_tags(request):
    tags = Tag.objects.all()
    data = TagSerializer(tags, many=True)
    return Response(data.data, status=status.HTTP_200_OK)
