# other imports
from . import views
from django.urls import include, path

urlpatterns = [
    # other patterns
    path("", views.index)
]