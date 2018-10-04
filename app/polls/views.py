from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Question, Choice


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    #
    # try:
    #     question = Question.objects.get(pk=question_id)
    #     context = {
    #         'question': question
    #     }
    #     return render(request, 'polls/detail.html', context)
    #
    # except Question.DoesNotExist:
    #     raise Http404('question does not exist')

    question = get_object_or_404(Question, pk=question_id)

    context = {
        'question': question,
    }
    return render(request, 'polls/detail.html', context)


def results(request, question_id):

    # question_id에 해당하는 Question 인스턴스를 redner 함수의 context로 전달
    # template 는 'polls/results.html'을 사용
    # Template에서는 전달받은 Question 인스턴스에 속하는 Choice 목록을 순회하며 보여줌
    # 이떄 각 choice 아이템들의 "choice_text' 및 votes 속성값도 같이 출력

    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question,
    }
    return render(request, 'polls/results.html', context)


def vote(request, question_id):
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
