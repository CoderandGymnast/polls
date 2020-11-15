from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.urls import reverse
from django.db.models import F
from django.views import generic
from django.utils import timezone

from .models import Question, Choice

class IndexView(generic.ListView):  # Class-based view.
	template_name = "polls/index.html"
	context_object_name = "latest_question_list"  # For ListView, the automatically generated context variable is question_list. To override this we provide the context_object_name attribute, specifying that we want to use latest_question_list instead.

	def get_queryset(self):  # QuerySet API reference: https://docs.djangoproject.com/en/3.1/ref/models/querysets/
		"""Return the last five published questions."""
		return Question.objects.filter(published_date__lte=timezone.now()).order_by("-published_date")[:5]  # Get the 5 most recent.

class DetailView(generic.DetailView):
	model = Question  # Get model question by the requested PK (Primary Key) and send it to the context of the view's template.
	template_name = "polls/detail.html"  # The view's template. By default, the "DetailView" generic view uses a template called <application name>/<model name>_detail.html.

	def get_queryset(self):
		"""
		Excludes any questions that aren't published yet.
		"""
		return Question.objects.filter(published_date__lte=timezone.now())

class ResultsView(generic.DetailView):
	model = Question
	template_name = "polls/results.html"


"""
[GENERIC VIEW]:
* "template_name" and "context_object_name" are used to override the default behaviors of the Django Generic View.
"""

# def index(request):  # Function-based view.
# 	print(request)
# 	latest_question_list = Question.objects.order_by("-published_date")[:5]  # [0; 5); "order_by": https://docs.djangoproject.com/en/3.1/ref/models/querysets/
# 	# template = loader.get_template("polls/index.html")
# 	context = {  # Dictionary; Variables of the template.
# 		"latest_question_list": latest_question_list,
# 	}
# 	# output = ", ".join([q.question_text for q in latest_question_list])  # Comma-separated.
# 	# return HttpResponse(template.render(context, request))
# 	return render(request, "polls/index.html", context)  # Returns an HttpResponse object of the given template rendered with the given context. "render" must be passed in the "request".
#
# def detail(request, question_id):
# 	# try:
# 	# 	question = Question.objects.get(pk=question_id)
# 	# except Question.DoesNotExist:  # Reference: https://docs.djangoproject.com/en/3.0/ref/exceptions/
# 	# 	raise Http404("Question does not exist")
# 	question = get_object_or_404(Question, pk=question_id)  # "pk=question_id" is passed to the "get()" function of the model's manager. Could try this by using Python interective shell.
# 	# return HttpResponse(f"You're looking at question '{question_id}'")
# 	return render(request, "polls/detail.html", {"question": question})
#
# def results(request, question_id):
# 	question = get_object_or_404(Question, pk=question_id)
# 	# return HttpResponse(f"You're looking at the result of question '{question_id}'")
# 	return render(request, "polls/results.html", {"question": question})
#
def vote(request, question_id):  # "<int:question_id>/vote/": API for voting + URL to a web page.
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST["choice"])  # "request.POST["choice"] value are always string.
	except KeyError:  # Redisplay the question voting form.
		return render(request, "polls/detail.html", {
			"question": question,
			"error_message": "You didn't select a choice",
		})
	except Choice.DoesNotExist:
		return render(request, "polls/detail.html", {
			"question": question,
			"error_message": "[Error]: invalid choice"
		})
	else:
		selected_choice.votes = F("votes") + 1  # Avoid race conditions.
		selected_choice.save()
	# return HttpResponse("Vote result page")  # Similar to "url" template tag: "{% url '...' ... %}"; Redirection path: Detail - Vote - Result.
	return HttpResponseRedirect(reverse("polls:results", args=[question.id]))  # Could use: (question.id,)
	# reverse("polls:results", args=[question.id]) = "/polls/1/results/".


"""
[NOTES]:
* "views.py" files contains multiple views. 
* View = Web page.
"""

"""
Why do we use a helper function get_object_or_404() instead of automatically catching the ObjectDoesNotExist exceptions at a higher level, or having the model API raise Http404 instead of ObjectDoesNotExist?

Because that would couple the model layer to the view layer. One of the foremost design goals of Django is to maintain loose coupling. Some controlled coupling is introduced in the django.shortcuts module.
"""

"""
[Double Submit Solution]:
1. 
POST /polls/1/vote HTTP/1.1
Host: soloen.com
choice=...
Status code: 302 Found
2.
GET /polls/1/results HTTP/1.1
Host: soloen.com
Status code: 200 OK
"""
