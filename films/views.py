from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Film
from .serializers import FilmSerializer, FilmDetailSerializer, FilmValidateSerializer
from django.db import transaction

@api_view(['GET', 'PUT', 'DELETE'])
def film_detail_api_view(request,id):
    try:
        film = Film.objects.get(id=id)
    except Film.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = FilmSerializer(film).data
        return Response(data=data)
    elif request.method == 'PUT':
        serializer = FilmValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        film.name = serializer.validated_data.get('name')
        film.text = serializer.validated_data.get('text')
        film.kp_rating = serializer.validated_data.get('kp_rating')
        film.is_active = serializer.validated_data.get('is_active')
        film.director_id = serializer.validated_data.get('director_id')
        film.genres.set(serializer.validated_data.get('genres'))
        film.save()
        return Response(status=status.HTTP_201_CREATED,
                        data=FilmDetailSerializer(film).data)
    else:
        film.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(http_method_names=['GET', 'POST'])
def film_list_create_api_view(request):
    if request.method == 'GET':
        films = Film.objects.select_related('director').prefetch_related('genres', 'reviews').all()
        data = FilmSerializer(films, many=True).data
        return Response(data=data)
    else:
        serializer = FilmValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)

        name = serializer.validated_data.get('name')
        text = serializer.validated_data.get('text')
        kp_rating = serializer.validated_data.get('kp_rating')
        is_active = serializer.validated_data.get('is_active')
        director_id = serializer.validated_data.get('director_id')
        genres = serializer.validated_data.get('genres')

        with transaction.atomic():
            film=Film.objects.create(
                name=name,
                text=text,
                kp_rating=kp_rating,
                is_active=is_active,
                director_id=director_id)
            film.genres.set(genres)
            film.save()
        return Response(status=status.HTTP_201_CREATED,
                        data=FilmDetailSerializer(film).data)