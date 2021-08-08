from re import template
from django.db.models import query
from django.db.models.query import RawQuerySet
from django.shortcuts import render, redirect
from .models import BloodRequest
from django.views.generic import ListView, DetailView
from django.views import generic
from django.shortcuts import render,get_object_or_404
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from .models import STATUS_PUBLISH

from django.db.models import Q

# Create your views here.

class BloodListView(ListView):
    model=BloodRequest
    template_name = 'home/home.html'
    queryset=BloodRequest.objects.filter(status=STATUS_PUBLISH)
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
    blood = get_object_or_404(BloodRequest, slug=name_slug)
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
                send_mail(subject, message, recepient, ['ayurvedproctologyassociation@gmail.com']) 
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect ("home:home")
    
    form = ContactForm(request.POST)
    return render(request, "home/contactus.html", {'contact_form':form})

