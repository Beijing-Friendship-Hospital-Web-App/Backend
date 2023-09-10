from django.urls import path
from .views import *

urlpatterns = [
    path('submit/', QuestionaireSubmitView.as_view(), name='submit'),
]
