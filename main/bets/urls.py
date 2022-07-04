from django.urls import path, include
from .views import BetMixinView

urlpatterns = [
    path('', BetMixinView.as_view()),
]
