from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User

# Create your views here.


@api_view(["POST"])
def signin(request):

    if ("name" not in request.data):
        return Response("Bad Request", status=400)

    name = request.data["name"]
    user, created_new = User.objects.get_or_create(name=name)

    print(user, created_new)

    return Response({"Name is": name})
