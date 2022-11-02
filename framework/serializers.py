from rest_framework import serializers
from .models import Artiste, Lyrics
from .models import Song

class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = ['id', 'first_name', 'last_name', 'age']

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'release_date', 'likes', 'artist_id']

class LyricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyrics
        fields = ['id', 'content', 'song_id']
