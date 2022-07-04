from django.urls import path, include

urlpatterns = [
    path('bets/', include('bets.urls')),
]
