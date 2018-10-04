#class based view
from django.views import generic

from ..models import Question


class IndexView(generic.ListView):
    model = Question
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return super().objects.order_by('-pub_date')[:5]

# class DetailView(generic.DeleteView):
#     model = Question
#     template_name = 'polls/detail.html'
#
# class ResultsView(generic.DeleteView):
#     model = Question
#     template_name = 'polls/results.html'

