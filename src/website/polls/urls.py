from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name="index")  # Map "views.index" (Route handler) to the URL configuration.
]

"""
[NOTES]:
1. "Route Handler": As a generic term, a route handler is the code that is looking for a request to a specific incoming URL, for example,
handle a browser request for a specific web page.
"""
