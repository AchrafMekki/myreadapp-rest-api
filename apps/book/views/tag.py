from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from apps.book.serializer import TagSerializer
from apps.book.models import Tag

"""
    curl http://127.0.0.1:8000/api/v1/book/tag/
    token_header = 'Authorization: Token 15647190d8dce70ead5ca966c82d3fbeef8a34e5'

    curl -H 'Authorization: Token 15647190d8dce70ead5ca966c82d3fbeef8a34e5' http://127.0.0.1:8000/api/v1/book/tag/
"""


@api_view(['GET']) # when [] it means [get] is default
#@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_tags(request):
    tags = Tag.objects.all()  # ORM Complex Data type (query_set)

    data = TagSerializer(tags, many=True)  # Deserialization --> Convert complex data type to native Python data types
    
    return Response(data.data, status=status.HTTP_200_OK)  # Return data
