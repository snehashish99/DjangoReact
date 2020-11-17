from django.urls import path
from . import views
urlpatterns = [
    path('submit-data/',views.submit_data),
    path('get-data/',views.get_data),
]