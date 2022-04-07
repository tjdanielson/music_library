from .models import Song
from .serializers import SongSerializer
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class SongList(APIView):

    def get(self, request):
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)