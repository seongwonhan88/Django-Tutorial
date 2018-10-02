from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):

    try:
        question = Question.objects.get(pk=question_id)
        context = {
            'question': question
        }
        return render(request, 'polls/detail.html', context)

    except Question.DoesNotExist:
        raise Http404('question does not exist')



def results(request, question_id):
    response = "you're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("you're voting on question %s." % question_id)
