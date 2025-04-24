from django.urls import path
from .views import PlanListCreateAPIView, PlanRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('plans', PlanListCreateAPIView.as_view(), name='plan-list-create'),
    path('plans/<uuid:id>', PlanRetrieveUpdateDestroyAPIView.as_view(), name='plan-retrieve-update-destroy'),
]