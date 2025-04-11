from rest_framework import serializers
from .models import Film

class FilmDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        # fields = ['id', 'name', 'kp_rating', 'created']
        # fields = '__all__'
        # exclude = ['is_active']
        fields = 'id name kp_rating created'.split()