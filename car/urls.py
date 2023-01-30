
from django.urls import include, path

from rest_framework import routers
from .views import CarView, ReservationView, ReservationDetailview

router = routers.DefaultRouter()
router.register('car',CarView)
urlpatterns = [
    path('reservation/', ReservationView.as_view()),
    path('reservation/<int:pk>/', ReservationDetailview.as_view())
]

urlpatterns += router.urls