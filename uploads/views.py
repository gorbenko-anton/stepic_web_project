from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, get_object_or_404

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def post_details(request, slug):
    post = get_object_or_404(Post, slug=slug)
    try:
        vote = post.votes.filter(user=request.user)[0]
    except Vote.DoesNotExist:
        vote = None
    return render(request, 'blog/post_details.html', {
        'post': post,
        'category': post.category,
        'tags': post.tags.all()[:],
        'vote': vote,
    })

