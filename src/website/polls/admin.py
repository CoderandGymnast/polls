from django.contrib import admin

from .models import Question, Choice

# admin.site.register(Question)  # Tell the Django administrator that Question objects have an administrator UI.

# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3  # Not count the existing ones.

class QuestionAdmin(admin.ModelAdmin):
	# fields = ["published_date", "question_text", "testing_field"]
	fieldsets = [
		(None, {"fields": ["question_text"]}),
		("Date information", {"fields": ["published_date", "testing_field"], "classes": ["collapse"]}),
	]
	list_display = ["question_text", "published_date", "was_published_recently"]  # Sorting by the output of an arbitrary method is not supported.
	list_filter = ["published_date"]
	search_fields = ["question_text", "published_date", "testing_field"]  # Filter according to the values of these fields - LIKE operator in SQL.
	inlines = [ChoiceInline]

class ChoiceAdmin(admin.ModelAdmin):
	fieldsets = [
		("Linked question", {"fields": ["question"]}),
		("Content", {"fields": ["choice_text"]}),
		("Vote information", {"fields": ["votes"]}),
	]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)

"""
[NOTES]:
* Change list options: https://docs.djangoproject.com/en/3.1/intro/tutorial07/
"""
