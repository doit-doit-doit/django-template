from rest_framework import serializers
from .models.Boards import Boards
from .models.Comments import Comments

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = [
            'id',
            'contents'
        ]

    # def to_representation(self, instance):
    #     self.fields['id'] = BoardRepresentationSerializer(read_only=True)
    #     return super(CommentsSerializer, self).to_representation(instance)

class BoardsSerializer(serializers.ModelSerializer):
    boards = CommentsSerializer(many=True, read_only=True)
    class Meta:
        model = Boards
        fields = [
            'id',
            'title',
            'name',
            'description',
            'boards'
        ]

# class BoardRepresentationSerializer(serializers.ModelSerializer) :
#     class Meta:
#         model = Boards
#         fields = ("id", "title", "name", "description")

