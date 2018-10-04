#class based view
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic, View

from ..models import Question, Choice


class IndexView(generic.ListView):
    model = Question
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return super().get_queryset().order_by('-pub_date')[:5]

class DetailView(generic.DeleteView):
    model = Question
    template_name = 'polls/detail.html'
    pk_url_kwarg = 'question_id'

class ResultsView(generic.DeleteView):
    model = Question
    template_name = 'polls/results.html'
    pk_url_kwarg = 'question_id'

class VoteView(View):
    def post(self, request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            context = {
                'question': question,
                'error_message': "You didn't select a choice.",
            }
            return render(request, 'polls/detail.html', context)

        else:
            selected_choice.votes += 1
            selected_choice.save()

            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


