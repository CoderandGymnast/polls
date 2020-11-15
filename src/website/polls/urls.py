from django.urls import path
from . import views

app_name = "polls"  # Application namespace.
urlpatterns = [
	path('', views.IndexView.as_view(), name="index"),
	path("<int:pk>/detail/", views.DetailView.as_view(), name="detail"),
	path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
	path("<int:question_id>/vote/", views.vote, name="vote"),
	# ex: /polls/
	# path("", views.index, name="index"),  # Map "views.index" (Route handler) to the URL configuration.
	# # ex: /polls/37/
	# path("<int:question_id>/", views.detail, name="detail"),  # "<int:x>", "def detail(request, x)": "x" must be the same.
	# path("<int:question_id>/results/", views.results, name="results"),
	# path("<int:question_id>/vote/", views.vote, name="vote"),
]

"""
[NOTES]:
1. "Route Handler": As a generic term, a route handler is the code that is looking for a request to a specific incoming URL, for example,
handle a browser request for a specific web page.
2. "views.index" represents for the view "index".
3. "int"is a converter that defines what patterns should match this part of the URL path.
4. Only need to change URL patterns on this file because we're using "loosely-coupled approach" inside all template files: {% url "<name>" <access to context's properties> %}
"""

"""
[NAMESPACING URLS NAMES]:
The tutorial project has just one app, polls. In real Django projects, there might be five, ten, twenty apps or more. How does Django differentiate the URL names between them? For example, the polls app has a detail view, and so might an app on the same project that is for a blog. How does one make it so that Django knows which app view to create for a url when using the {% url %} template tag?

The answer is to add namespaces to your URLconf. 
"""
