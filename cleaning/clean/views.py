from django.shortcuts import render,redirect
from .models import Contact
from django.views.generic import CreateView
from .forms import ContactForm
from django.contrib import messages
# Create your views here.


def home(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("display/about.html")
    else:
        form = ContactForm()
    context = {"form":form}

    return render(request,"clean/index.html",{'form':form})

class CreateMessage(CreateView):
    template_name = 'clean/index.html'
    model = Contact
    form_class = ContactForm
    success_message = "worked right"
    success_url = '/'

    def form_valid(self,form):
        messages.success(self.request,"Message Sent")

        return super().form_valid(form)

    


    

    