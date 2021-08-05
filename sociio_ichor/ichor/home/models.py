from django.db import models
from django.db.models.aggregates import Max
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.db.models.signals import post_delete
from django.dispatch import receiver

STATUS_DRAFT = 0
STATUS_PUBLISH = 1

STATUS = (
    (STATUS_DRAFT, "Draft"),
    (STATUS_PUBLISH, "Publish")
)


BG_CHOICES = (
    ('A+','A+'),
    ('B+','B+'),
    ('O+','O+'),
    ('AB+', 'AB+'),
    ('A-','A-'),
    ('B-','B-'),
    ('O-','O-'),
    ('AB-', 'AB-'),
    ('Hh', 'Hh'),
)
TYPE=(
    ('Whole Blood', 'Whole Blood'),
    ('Plasma', 'Plasma'),
    ('Platelets', 'Platelets'),
)

#STATUS=(
    #('0', 'Draft'),
    #('1', 'Publish')
#)

# Create your models here.
class BloodRequest(models.Model):
    blood_request_id = models.AutoField(primary_key=True)
    time_stamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=400, unique=True, default=None)
    blood_group = models.CharField(
        max_length=20, choices=BG_CHOICES, default=None
    )
    blood_type = models.CharField(
        max_length=50, choices=TYPE, default=None
    )
    acceptable_blood_group = models.CharField(max_length = 100, blank=False )
    Phone = models.CharField(max_length=10, default='')
    units = models.CharField(max_length=5)
    note = models.TextField(default='', blank=True, null=True)
    address = models.TextField(default='', blank=True, null=True)
    hospital_initials = models.CharField(default='KMC', blank=False, null=False, max_length=50 )
    status = models.IntegerField(choices=STATUS, default=0)
    
    class Meta:
        verbose_name = 'Blood Request'
    
    
def pre_save_blog_post_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = slugify(instance.name)
  
pre_save.connect(pre_save_blog_post_receiver, sender=BloodRequest)
