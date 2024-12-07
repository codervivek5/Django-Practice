from django.shortcuts import render,HttpResponse

# Create your views here.
def receipies(request):
    return render(request, "receipies.html")

