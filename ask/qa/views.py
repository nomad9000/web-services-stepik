from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST
from forms import *

from models import *

def test(request, *args, **kwargs):
    return HttpResponse('OK', status=200)

def mainpage(request):
    questions = Question.objects.new()
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
    questions = Question.objects.popular()
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
    answers = q.answer_set.all()
    return render(request, 'qa/question.html', {
        'question': q,
        'answers': answers,
        'form': AskForm(),
    })

def askpage(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            q = form.save()
            return HttpResponseRedirect('/question/' + str(q.pk) + '/')
    else:
        form = AskForm()
    return render(request, 'ask.html', { 'form': form })

@require_POST
def answerpage(request):
    form = AnswerForm(request.POST)
    if form.is_valid():
        a = form.save()
        return HttpResponseRedirect('/question/' + str(a.question.pk) + '/')
    else:
        return HttpResponseRedirect('/question/' + str(form.question.pk) + '/?err=1')