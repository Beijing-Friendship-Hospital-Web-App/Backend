from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import PostQuestionaireSerializer
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from users.models import User

class QuestionaireSubmitView(CreateAPIView):
    serializer_class = PostQuestionaireSerializer

    def perform_create(self, serializer):
        user = User.objects.get(name=self.request.data.get('user'))
        serializer.save(user=user)