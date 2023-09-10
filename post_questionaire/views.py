from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import PostQuestionaireSerializer

# Create your views here.
@api_view(["POST"])
def submit(request):
    serializer = PostQuestionaireSerializer
    