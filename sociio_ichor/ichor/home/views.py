
from re import template
import re
from django.db.models import query
from django.db.models.query import RawQuerySet
from django.shortcuts import render, redirect
from .models import BloodRequest, DonorRequest, STATUS_DRAFT
from django.views.generic import ListView, DetailView
from django.views import generic
from django.shortcuts import render,get_object_or_404
from .forms import ContactForm
from django.template import RequestContext


from django.core.mail import send_mail, BadHeaderError
from .models import STATUS_PUBLISH, STATUS_DRAFT
from home.forms import DonorForm
from django.db.models import Q
from django.http import HttpResponse


# Create your views here.

class BloodListView(ListView):
    model=BloodRequest
    template_name = 'home/home.html'
    queryset=BloodRequest.objects.filter(status=STATUS_PUBLISH).order_by('-time_stamp')
    context_object_name='blood'
     

class BloodSearchView(ListView):
    model=BloodRequest
    template_name='home/home.html'
    context_object_name='blood'
    
    def get_queryset(self):
        query=self.request.GET.get('q')
        return BloodRequest.objects.filter(blood_group__icontains=query, status=STATUS_PUBLISH)
    

class BloodDetailView(DetailView):
    model = BloodRequest
    template_name = 'home/home.html'
    
    
def detail_view(request, name_slug):
    blood = get_object_or_404(BloodRequest.objects.filter(status=STATUS_PUBLISH), slug=name_slug)
    return render(request, 'home/detail.html', {'blood':blood,})
    
    
def about(request):
    return render(request, 'home/about.html')



def landing(request):
    return render(request, 'home/land.html')

def privacy(request):
    return render(request, 'home/privacy.html')



def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Subject Inquiry"
            body = {
                'name': form.cleaned_data['name'], 
			    'company': form.cleaned_data['company'], 
			    'email': form.cleaned_data['email_address'], 
			    'message':form.cleaned_data['message'], 
			    'phone':form.cleaned_data['phone'], 
       
                }
            message = "\n".join(body.values())
            recepient = str(form['email_address'].value())

            try:
                send_mail(subject, message, recepient, ['sociio.organisation@gmail.com']) 
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect ("home:donate")
    
    form = ContactForm(request.POST)
    return render(request, "home/contactus.html", {'contact_form':form})


def post_draft_list(request):
    posts = BloodRequest.objects.filter(status = STATUS_DRAFT)
    return render(request, 'home/draft.html', {'posts': posts})

def donor_review(request):
    review = DonorRequest.objects.all()
    return render(request, 'home/review.html', {'review':review})

    
def detailDraft_view(request, name_slug):
    posts = get_object_or_404(BloodRequest, slug=name_slug)
    return render(request, 'home/detail-draft.html', {'posts':posts,})
    
def error_404(request, exception):
        data = {}
        return render(request,'home/404.html', data)

def error_500(request, *args):
        data = {}
        return render(request,'home/500.html', data)
    

def donor_form(request):
    form = DonorForm()
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('home:donor_confirm')
    context = {'form':form}
        
    return render(request, 'home/donor.html', context)

def donor_confirm(request):
    return render(request, 'home/donor_confirm.html')
