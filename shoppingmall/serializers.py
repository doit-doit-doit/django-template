from rest_framework import serializers
from .models.Boards import Boards

class BoardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boards
        fields = [
            'title',
            'name',
            'description'
        ]