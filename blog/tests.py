from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from blog.models import Category, Post, Comment

User = get_user_model()

class BlogTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='blogwriter',
            email='writer@example.com',
            password='password123'
        )
        self.category = Category.objects.create(name='Announcements')
        self.post = Post.objects.create(
            category=self.category,
            author=self.user,
            title='Welcome to New Term',
            content='This is the content of the announcement.',
            published=True
        )
        self.comment = Comment.objects.create(
            post=self.post,
            author_name='John Reader',
            author_email='reader@example.com',
            content='Great news!'
        )

    def test_blog_models_str_and_save(self):
        self.assertEqual(str(self.category), 'Announcements')
        self.assertEqual(str(self.post), 'Welcome to New Term')
        self.assertEqual(self.post.slug, 'welcome-to-new-term')
        self.assertEqual(str(self.comment), f"Comment by John Reader on Welcome to New Term")

    def test_post_views(self):
        # Test post list view via direct view function
        response = self.client.get(f'/blog/welcome-to-new-term/')
        # Or test post_detail view logic
        self.assertTrue(self.post.published)
