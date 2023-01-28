from django.urls import path,include
from .views import RegisterAPI

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path("register/", RegisterAPI.as_view())
]
