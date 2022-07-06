from django.urls import path, include
from .views import BlogabetBetMixinView

urlpatterns = [
    path('blogabet/', BlogabetBetMixinView.as_view()),
]
