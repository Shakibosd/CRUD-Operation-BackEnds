from django.urls import path
from .views import PostApiView, GetApiView, DeleteApiView

urlpatterns = [
    path('plans-post/', PostApiView.as_view(), name='plan-list-post'),
    path('plans-get/', GetApiView.as_view(), name='plan-list-get'),
    path('plans-get/<int:id>/', GetApiView.as_view(), name='plan-list-get'),
    path('plans-put/<int:id>/', GetApiView.as_view(), name='plan-list-put'),
    path('plans-delete/<int:id>/', DeleteApiView.as_view(), name='plan-list-delete'),
]