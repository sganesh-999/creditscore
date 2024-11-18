from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout


# Create your views here.

def index(request):
    if request.user.is_authenticated:
            questions = Question.objects.all()
            context={'questions':questions}
            return render(request,"index.html",context)
    



def handler404(request):
    return render(request, '404.html')

def question_submit(request):
    result_score=0
    print('submitted successfully')
    if request.method=='POST':
        questions = Question.objects.all()
        
        for  question in questions:
            choice_id = request.POST.get(f"question_{question.id}",None)
            print('question - ',question.text,'choice id - ',choice_id)
            if choice_id:
                choice = get_object_or_404(Choice,id=choice_id)
                print('question - ',question.text,'choice id - ',choice_id,"choice = ",choice)
                result_score+=choice.choice_score
    return HttpResponse(f"submitted succesfully {result_score}")
        