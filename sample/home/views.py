from django.shortcuts import redirect, render,HttpResponse
from django.contrib import messages
from datetime import datetime
from home.models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout





# Create your views here.
def home(request):
    if request.user.is_anonymous:
        return redirect("/login")
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


# Login function
def login(request): 

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')  
        user = authenticate( username=username, password=password)

        if user is not None:
            return redirect("/home")
            # A backend authenticated the credentials
        else:
            # No backend authenticated the credentials
            return render(request , "login.html")

            
    return render(request , "login.html")



def logoutuser(request): 
    logout(request)
    return redirect("/login")
    # return HttpResponse("signup page")