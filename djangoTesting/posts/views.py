from django.http.response import Http404, HttpResponseRedirect
from .models import Comment, Post
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'posts/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """Return the last five published questions."""
        # return Post.objects.order_by('-pub_date')[:5]
        return Post.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

# def index(request):
#     latest_post_list = Post.objects.order_by('-pub_date')[:5]
#     context = {'latest_post_list': latest_post_list}
#     return render(request, 'posts/index.html', context)

def detail(request, comment_id):
    # return HttpResponse("You're looking at comment %s." % comment_id)
    try:
        comment = Comment.objects.get(id=comment_id)
    except Comment.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'posts/detail.html', {'comment': comment})


# class DetailView(generic.DetailView):
#     model = Comment
#     template_name = 'posts/detail.html'


class ResultsView(generic.ListView):
    model = Post
    template_name = 'posts/results.html'

def comment(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Comment.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, 'posts/comment.html', {'post': post})

def post(request):
    return render(request, 'posts/post.html', {})


def createComment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comment = Comment(post=post, comment_text=request.POST['comment'], pub_date=timezone.now())
    comment.save()
    return HttpResponseRedirect(reverse('posts:results', args=(post.id,)))


def createPost(request):
    post = Post(post_text=request.POST['post'], pub_date=timezone.now())
    post.save()
    return HttpResponseRedirect('/posts')


def results(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post)
    return render(
        request,
        'posts/results.html',
        {'post': post, 'comments': comments}
    )
    # response = "You're looking at the results of comment %s."
    # return HttpResponse(response % comment_id)

def vote(request, comment_id):
    return HttpResponse("You're voting on comment %s." % comment_id)


class DetailView(generic.DetailView):

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Post.objects.filter(pub_date__lte=timezone.now())