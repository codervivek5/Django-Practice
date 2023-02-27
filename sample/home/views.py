from django.shortcuts import render,HttpResponse
from django.contrib import messages
from datetime import datetime
from home.models import Contact

# Create your views here.
def home(request):
    # return HttpResponse("this is index page")
    return render(request , "index.html")

def about(request): 
    return render(request , "about.html")

def services(request):   
    return render(request , "services.html")

def contact(request): 
    if request.method == "POST":
        fName = request.POST.get('fName')
        lName = request.POST.get('lName')
        Email = request.POST.get('Email')
        Subject = request.POST.get('Subject')
        Message = request.POST.get('Message')
        date = datetime.today()

        # create an object of contact
        contact = Contact(
                            fName = fName,
                            lName = lName,
                            Email= Email,
                            Subject= Subject,
                            Message =Message, 
                            date=date
                        )
        contact.save() 
        messages.success(request, 'Your message has been sent!')  

    return render(request , "contact.html",)