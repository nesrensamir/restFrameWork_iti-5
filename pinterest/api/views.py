from rest_framework import status
from rest_framework.response import responses, Response
from rest_framework.decorators import api_view
from pinterest.models import Movie
from .serializers import MovieSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, BasePermission

class userCanDelete(BasePermission):

    def has_permission(self, request, view):
        if request.user.groups.filter(name='can-delete').exists():
            return True
        return False


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_list(request):
    movie = Movie.objects.all()
    serialized_movie = MovieSerializer(instance=movie, many=True)
    return Response(data=serialized_movie.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def movie_create(request):
    serialized_movie = MovieSerializer(data=request.data)
    if serialized_movie.is_valid():
        serialized_movie.save()
    else:
        return Response(data=serialized_movie.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(data=serialized_movie.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def movie_details(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Exception as e:
        return Response(data={'message': 'faild:movie doesnot exists'}, status=status.HTTP_400_BAD_REQUEST)
    serialized_movie = MovieSerializer(instance=movie)
    return Response(data=serialized_movie.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([userCanDelete])
def movie_delete(request, pk):
    response = {}
    try:
        movie_obj = Movie.objects.get(pk=pk)
        movie_obj.delete()
        response['data'] = {'message': 'successfully Deleted'}
        response['status'] = status.HTTP_200_OK
    except Exception as e:
        response['data'] = {'message': 'ERROR:While Deleting movie'}
        response['status'] = status.HTTP_400_BAD_REQUEST

    return Response(**response)


@api_view(['PUT', 'PATCH'])
def movie_update(request, pk):
    movie = Movie.objects.get(pk=pk)

    if request.method == 'PUT':
        serialized_movie = MovieSerializer(instance=movie, data=request.data)
    elif request.method == 'PATCH':
        serialized_movie = MovieSerializer(instance=movie, data=request.data, partial=True)

    if serialized_movie.is_valid():
        serialized_movie.save()
        return Response(data=serialized_movie.data, status=status.HTTP_200_OK)

    return Response(data=serialized_movie.errors, status=status.HTTP_400_BAD_REQUEST)
