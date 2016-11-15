from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from models import *

def test(request, *args, **kwargs):
    return HttpResponse('OK', status=200)

def mainpage(request):
    questions = QuestionManager.new()
    limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(questions, limit)
    paginator.baseulr = '/question/'
    questions = paginator.page(page)
    return render(request, 'qa/questions.html', {
        'questions': questions.object_list,
        'paginator': paginator,
        'page': page,
    })

def popularpage(request):
    questions = QuestionManager.popular()
    limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(questions, limit)
    paginator.baseulr = '/popular/'
    questions = paginator.page(page)
    return render(request, 'qa/questions.html', {
        'questions': questions.object_list,
        'paginator': paginator,
        'page': page,
    })

def questionpage(request, questionid):
    q = Question.objects.get(id = questionid)
    answers = q.answer_set
    return render(request, 'qa/question.html', {
        'question': q,
        'answers': answers,
    })