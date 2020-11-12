from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Category

# Create your tests here.

class Test_Create_Post(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name="django")
        testuser1 = User.objects.create_user(username="test1", password="1234")
        test_post = Post.objects.create(category_id=1, title='Test post', excerpt='Post excerpt', content='Test post content', slug='post-title', author_id=1, status='published')

    def test_blog_content(self):
        post = Post.postobjects.get(id=1)
        cat = Category.objects.get(id=1)
        author = f'{post.author}'
        excerpt = f'{post.excerpt}'
        title = f'{post.title}'
        content = f'{post.content}'
        status = f'{post.status}'
        self.assertEqual(author, 'test1')
        self.assertEqual(title, 'Test post')
        self.assertEqual(content, 'Test post content')
        self.assertEqual(status, 'published')
        self.assertEqual(str(post), 'Test post')
        self.assertEqual(str(cat), 'django')