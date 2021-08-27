from django.db import models
from django.db.models.base import Model
from django.db.models.fields import SlugField
from taggit.managers import TaggableManager

def upload_location(instance, filename, *kwargs):
	file_path = 'section/{subtitle}-{filename}'.format(
     section=str(instance.section), filename=filename)
	return file_path

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(default=None, max_length=100)
    about_author = models.TextField(blank=True)
    publish_date=models.DateTimeField(blank=True, null=True)
    tags = TaggableManager()
    slug = models.SlugField(unique=True, max_length=100)
    
    def __Str__(self):
        return self.title
    
class BlogContent(models.Model):
    section = models.ForeignKey(Blog, default=None , on_delete=models.CASCADE)
    subheading = models.CharField(max_length=250)
    content = models.TextField(default=None)
    image = models.FileField(upload_to=upload_location, blank=True, default=None)
    
