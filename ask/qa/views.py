from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST
from django.contrib import auth
from datetime import datetime
import json
from django.contrib.auth import logout
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
    loginform = LoginForm()
    paginator = Paginator(questions, limit)
    paginator.baseulr = '/question/'
    questions = paginator.page(page)
    return render(request, 'qa/questions.html', {
        'questions': questions.object_list,
        'paginator': paginator,
        'page': page,
        'loginform': loginform,
        'user': request.user,
    })

def popularpage(request):
    questions = Question.objects.popular()
    limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(questions, limit)
    paginator.baseulr = '/question/'
    questions = paginator.page(page)
    return render(request, 'qa/popular.html', {
        'questions': questions.object_list,
        'paginator': paginator,
        'page': page,
    })

def questionpage(request, questionid):
    q = Question.objects.get(id = questionid)
    answers = q.answer_set.all()
    form = AnswerForm(initial={'question': q.id})
    return render(request, 'qa/question.html', {
        'question': q,
        'answers': answers,
        'form': form,
    })

def askpage(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if request.user.is_authenticated():
            form._user = request.user
        if form.is_valid():
            q = form.save()
            return HttpResponseRedirect('/question/' + str(q.id) + '/')
    else:
        form = AskForm()
        return render(request, 'qa/ask.html', { 'form': form })

@require_POST
def answerpage(request):
    form = AnswerForm(request.POST)
    if request.user.is_authenticated():
        form._user = request.user
    if form.is_valid():
        a = form.save()
        return HttpResponseRedirect('/question/' + str(a.question.id) + '/')
    else:
        return HttpResponseRedirect('/question/' + str(form.question.id) + '/?err=1')

def signuppage(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = SignupForm()
    return render(request, 'qa/signup.html', { 'form': form })

def loginpage(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.load()
            auth.login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    return render(request, 'qa/login.html', { 'form': form })

def updateanswers(request):
    q = request.GET.get('question')
    time = request.GET.get('time')
    print (time)
    time = str.join(' ', time.split(None)[1:5])
    time = datetime.strptime(time, '%d %b %Y %H:%M:%S')
    try:
        response = Answer.objects.filter(question = q)
        response = response.filter(added_at__gt = time)
    except Exception as e:
        print (e.strerror)

    response = render_to_response('qa/new_answers.html', {'newanswers': response})
    return response

def logoutpage(request):
    if request.method == 'POST':
       logout(request)
    return HttpResponseRedirect('/')