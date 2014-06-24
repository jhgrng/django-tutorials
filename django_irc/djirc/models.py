from django.db import models

# Create your models here.
from django.db.models import permalink


# model for comments that are going to be displayed
class Comment(models.Model):
    pub_date = models.DateTimeField('date published')
    user = models.CharField(max_length=100)
    body = models.TextField()


# model for a comment field that's going to add a new comment




# # Create your models here.
# class Blog(models.Model):
#     title = models.CharField(max_length=100, unique=True)
#     slug = models.SlugField(max_length=100, unique=True)
#     body = models.TextField()
#     posted = models.DateField(db_index=True, auto_now_add=True)
#     category = models.ForeignKey('blog.Category')


#     def __unicode__(self):
#         return '%s' % self.title


#     @permalink
#     def get_absolute_url(self):
#         return ('view_blog_post', None, { 'slug': self.slug })


# class Category(models.Model):
#     title = models.CharField(max_length=100, db_index=True)
#     slug = models.SlugField(max_length=100, db_index=True)


#     def __unicode__(self):
#         return '%s' % self.title


#     @permalink
#     def get_absolute_url(self):
#         return ('view_blog_category', None, { 'slug': self.slug })