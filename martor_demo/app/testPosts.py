from django.test import TestCase
from app.models import Post


class PostTestCase(TestCase):
    def testPost(self):
        post = Post(title="My title", description="Blurb", wiki="Post body")
        self.assertEqual(post.title, "My title")
        self.assertEqual(post.description, "Blurb")
        self.assertEqual(post.wiki, "Post body")
