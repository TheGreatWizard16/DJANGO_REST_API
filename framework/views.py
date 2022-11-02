
import pstats
from django.http import JsonResponse

import framework
from .serializers import ArtisteSerializer
from .serializers import SongSerializer
from .serializers import LyricsSerializer
from .models import Artiste
from .models import Song
from .models import Lyrics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from framework import serializers



@api_view(['GET','POST'])
def framework_list(request):

    if request.method == 'GET':
        framework = Artiste.objects.all()
        serializer = ArtisteSerializer(framework, many = True)
        return JsonResponse({'framework': serializer.data})
        return Response(serializer.data)
        
    if request.method == 'POST':
        serializer= ArtisteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT', 'DELETE'])
def framework_deatil(request, id):
    
    try:
        framework = Artiste.objects.get(pk = id )
    except Artiste.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArtisteSerializer(framework)
        return Response(serializer.data)


    elif request.method == 'PUT':
        serializer = ArtisteSerializer(framework, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        framework.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 


# def framework_list(request):
#     framework = Song.objects.all()
#     serializer = SongSerializer(framework, many = True)
#     return JsonResponse({'framework': serializer.data})

# def framework_list(request):
#     framework = Lyrics.objects.all()
#     serializer = LyricsSerializer(framework, many = True)
#     return JsonResponse({'framework': serializer.data})