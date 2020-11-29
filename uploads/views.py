from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator

from qa import models


#from ask.qa.models import Question
#from qa import Question
#from ask import models
from ask.qa import models
#from ask import Question

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def post_details(request, id):
    post = get_object_or_404(Question, id=id)
    try:
        answer = question.answer.filter(id=request.id)[0]
    except Answer.DoesNotExist:
        answer = None
    return render(request, 'blog/post_details.html', {
        'title': question.title,
        'text': question.text,
        'answer': question.answer.all()[:],
    })

def new_questions(request):
    questions = Question.objects.new() #.filter(is_published=True)
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page) # Page
    return render(request, 'blog/new_questions.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })

def post_list_all(request):
    posts = Post.objects.filter(is_published=True)
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, limit)
    paginator.baseurl = '/blog/all_posts/?page='
    page = paginator.page(page) # Page
    return render(request, 'blog/post_by_tag.html', {
        'posts': page.object_list,
        'paginator': paginator, 'page': page,
    })

def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page

def post_list_main(request):
    since = request.GET.get('since')
    posts = Post.objects.main(since)
    return render(request, 'blog/post_main.html', {
        'posts': posts,
        'since': posts[-1].id,
    })