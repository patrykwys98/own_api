from django.urls import path, include
from .views import BlogabetBetMixinView, ZawodTyperMixinView

urlpatterns = [
    path('blogabet/', BlogabetBetMixinView.as_view()),
    path('zt/', ZawodTyperMixinView.as_view()),
]
