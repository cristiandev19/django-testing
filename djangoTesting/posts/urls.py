from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path(
        '',
        views.IndexView.as_view(template_name="posts/index.html"),
        name='index'
    ),
    # path(
    #     '<int:pk>/',
    #     views.DetailView.as_view(template_name="posts/detail.html"),
    #     name='detail'
    # ),
    path('<int:comment_id>/', views.detail, name='detail'),
    path(
        '<int:post_id>/comment/',
        views.comment,
        name='comment'
    ),
    path(
        '<int:post_id>/create-comment/',
        views.createComment,
        name='create-comment'
    ),
    path(
        '<int:post_id>/results/',
        views.results,
        name='results'
    ),
    path(
        '<int:comment_id>/vote/',
        views.vote,
        name='vote'
    ),
]


