
# Helps in authenticating the user, username and password again
from apps.reader.serializer import ReaderSerializer
from django.contrib.auth import authenticate  
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.reader.models import Reader
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User



class Login(APIView):  # self made authentification

    def post(self, request):
        # Extract credentials
        password = request.data.get('password')
        username = request.data.get('username')

        # Authenticate the user tocheck if it is available

        user: User | None = authenticate(
            username=username,
            password=password
            )
        
        # Generate token 
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        else:
             return Response(
                 {
                  'error': 'Invalid Credential',
                 'detail': 'Username or password is incorrect'},
                  status=status.HTTP_404_NOT_FOUND
                )
        


@api_view()
def detail_reader(request, pk):
    reader = Reader.objects.get(user__id=pk)

    data = ReaderSerializer(reader)
    return Response({'data': data.data})
