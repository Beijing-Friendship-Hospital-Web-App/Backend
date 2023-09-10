from rest_framework import serializers
from .models import Post_Questionaire

class PostQuestionaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post_Questionaire
        fields = "__all__"