from django.shortcuts import render

# Create your views here.
def home(request):

    peoples = [
        {'name': 'John', 'age': 25},
        {'name': 'Jane', 'age': 30},
        {'name': 'Bob', 'age': 15},
        {'name':'vivek','age':25},
        {'name':'sachin','age':27},
        {'name':'ankit','age':17},
        ]
    
    vegetables = ["Potato","Tomato","Pumpkin",""] 
    
    return render ( request, 'home/index.html', context = {'people': peoples, 'vegetables':vegetables})


def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')