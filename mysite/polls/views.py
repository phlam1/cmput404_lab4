from django.shortcuts import render, get_object_or_404
from .models import Question
from .models import Choice
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic

# Create your views here.

from django.http import HttpResponse
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list' : latest_question_list}
	return render(request, 'index.html', context)
	
class IndexView(generic.ListView):
	template_name = 'index.html'
	context_object_name = 'latest_question_list'
	def get_queryset(self):
		return Question.objects.order_by('-pub_date')[:5]
	
def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'detail.html', {'question' : question})
	
class DetailView(generic.DetailView):
	model = Question
	template_name = 'detail.html'
	
class ResultsView(generic.DetailView):
	model = Question
	template_name = 'results.html'
	
def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'results.html', {'question' : question})
	
	
def vote(request, question_id):
	p = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'detail.html', {
							'question' : p,
							'error_message': "You didn't select a choice!"})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

	#return HttpResponse("You're voting on question %s." % (question_id))

