from django.test import TestCase
from django.contrib,auth.models import User

from blog.models import Post

# Create your tests here.
class PostTestCase(TestCase):
  def setUp(self):
    self.user = User.objectos.create(username ="jesusv" , password='ejemplo')
    
  def test_is_publisged_return_false(self):
    post = Post.objects.create(auhor=user , title = "mi titulo")

    is_published = post.is_published()

    self.assertFalse(is_published)
