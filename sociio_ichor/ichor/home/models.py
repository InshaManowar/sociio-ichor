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
        max_length=20, choices=BG_CHOICES, default=None, blank=True, null=True
    )
    blood_type = models.CharField(
        max_length=50, choices=TYPE, default=None, blank=True, null=True
    )
    acceptable_blood_group = models.CharField(max_length = 100, blank=True, null=True )
    Phone = models.CharField(max_length=10, default='')
    units = models.CharField(max_length=5)
    note = models.TextField(default='', blank=True, null=True)
    address = models.TextField(default='', blank=True, null=True)
    hospital_initials = models.CharField(default='', blank=False, null=False, max_length=50 )
    status = models.IntegerField(choices=STATUS, default=0)
    urgent = models.BooleanField( blank=True, default=False)
    
    class Meta:
        verbose_name = 'Blood Request'
    
    
def pre_save_blog_post_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = slugify(instance.name)
  
pre_save.connect(pre_save_blog_post_receiver, sender=BloodRequest)


class DonorRequest(models.Model):
    full_name = models.CharField(max_length=200, default='')
    date_of_birth = models.DateField(default='')
    email_id = models.EmailField(max_length=200)
    phone = models.CharField(max_length=11, default='')
    city = models.CharField(max_length=100, default='')
    state = models.CharField(max_length=100, default='')
    pin_code = models.IntegerField(default=False)
    weight = models.CharField(max_length=10, default='')
    I_agree_to_the_terms_and_conditions_stated_below = models.BooleanField(blank=False,  default=True)
    blood_group = models.CharField(
        max_length=4, choices=BG_CHOICES, default=None
    )    
    


