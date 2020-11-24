from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class QuestionManager(models.Manager):
  def new(self):
    return self.order_by('-id')
  def popular(self):
    return self.order_by('-rating')

class PostManager(models.Manager):
  def main(self, since, limit=10):
    qs = self.order_by('-id')
    res = []
    if since is not None:
      qs = qs.filter(id__lt=since)
    for p in qs[:1000]:
      if len(res):
        res.append(p)
      elif res[-1].category != p.category:
        res.append(p)
      if len(res) >= limit:
        break
    return res

class Question(models.Model):
  objects = QuestionManager()
  title = models.CharField(max_length=255)
  text = models.TextField()
  added_at = models.DateTimeField(blank=True, auto_now_add=True)
  rating = models.IntegerField(default=0)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  likes = models.ManyToManyField(User, related_name='likes_set')

class Answer(models.Model):
  text = models.TextField()
  added_at = models.DateTimeField(blank=True, auto_now_add=True)
  question = models.ForeignKey(Question)
  author = models.ForeignKey(User, on_delete=models.CASCADE)

class Tag(models.Model):
  slug = models.SlugField(unique=True)
  title = models.CharField(max_length=64)
  def get_url(self):
    return reverse('blog:tag-details', kwargs={'slug': self.slug})
  def __unicode__(self):
    return self.title

