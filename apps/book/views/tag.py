from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from apps.book.serializer import TagSerializer
from apps.book.models import Tag


@api_view(['GET']) # when [] it means [get] is default
def list_tags(request):
    tags = Tag.objects.all()  # ORM Complex Data type (query_set)

    data = TagSerializer(tags, many=True)  # Deserialization --> Convert complex data type to native Python data types
    
    return Response(data.data, status=status.HTTP_200_OK)  # Return data
