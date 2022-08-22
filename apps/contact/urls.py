from django.urls import path
from .views import GetInTouchCreateAPIView

app_name = 'contact'

urlpatterns = [
    path('create/', GetInTouchCreateAPIView.as_view())
]
