from django.test import TestCase
import datetime

from django.utils import timezone
from django.urls import reverse

from .models import Post
from django.test import TestCase

# Create your tests here.


# Test de logica en BD
class PostModelTests(TestCase):

    def test_was_published_recently_with_future_post(self):
        """
        was_published_recently() returns False for posts whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_post = Post(pub_date=time)
        self.assertIs(future_post.was_published_recently(), False)

def create_post(post_text, days):
    """
    Create a post with the given `post_text` and published the
    given number of `days` offset to now (negative for posts published
    in the past, positive for posts that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Post.objects.create(post_text=post_text, pub_date=time)

# Test de vistas
class PostIndexViewTests(TestCase):
    def test_no_posts(self):
        """
        If no posts exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('posts:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No posts are available.")
        self.assertQuerysetEqual(response.context['latest_post_list'], [])

    def test_past_post(self):
        """
        posts with a pub_date in the past are displayed on the
        index page.
        """
        post = create_post(post_text="Past post.", days=-30)
        response = self.client.get(reverse('posts:index'))
        self.assertQuerysetEqual(
            response.context['latest_post_list'],
            [post],
        )

    def test_future_post(self):
        """
        posts with a pub_date in the future aren't displayed on
        the index page.
        """
        create_post(post_text="Future post.", days=30)
        response = self.client.get(reverse('posts:index'))
        self.assertContains(response, "No posts are available.")
        self.assertQuerysetEqual(response.context['latest_post_list'], [])

    def test_future_post_and_past_post(self):
        """
        Even if both past and future posts exist, only past posts
        are displayed.
        """
        post = create_post(post_text="Past post.", days=-30)
        create_post(post_text="Future post.", days=30)
        response = self.client.get(reverse('posts:index'))
        self.assertQuerysetEqual(
            response.context['latest_post_list'],
            [post],
        )

    def test_two_past_posts(self):
        """
        The posts index page may display multiple posts.
        """
        post1 = create_post(post_text="Past post 1.", days=-30)
        post2 = create_post(post_text="Past post 2.", days=-5)
        response = self.client.get(reverse('posts:index'))
        self.assertQuerysetEqual(
            response.context['latest_post_list'],
            [post2, post1],
        )
