from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def signup(request):
    data={'data':'', 'status':''}

    user_serialized = UserSerializer(data=request.data)
    if user_serialized.is_valid():
        user_serialized.save()
        data['data'] = {'user': user_serialized.data.get('email'),
                        'token': Token.objects.get(user__username=user_serialized.data.get('username')).key,
                        'message': 'Created'}
        data['status'] = status.HTTP_201_CREATED
    else:
        data['data'] = user_serialized.errors
        data['status'] = status.HTTP_400_BAD_REQUEST

    return Response(**data)


@api_view(['DELETE'])
def logout(request):
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)