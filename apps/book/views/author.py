from apps.book.models import Author
from rest_framework.decorators import api_view
from apps.book.serializer import AuthorSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveAPIView, DestroyAPIView, RetrieveDestroyAPIView
# Function-base - view


@api_view(['GET'])  # B default, it uses a'GET' method
def list_authors(request):
     # Get all the authors
     authors = Author.objects.all()

    # Deserialize using the AuthorSerializer
     data = AuthorSerializer(authors, many=True)

    #  Return data
     return Response (data.data, status=status.HTTP_200_OK)


class DetailAuthor(RetrieveDestroyAPIView):

     # How do we handle genric views
     # ORM
     queryset = Author.objects.all()
     # Serializer
     serializer_class = AuthorSerializer

class DeleteAuthor(DestroyAPIView):
     queryset = Author.objects.all()
     serializer_class = AuthorSerializer