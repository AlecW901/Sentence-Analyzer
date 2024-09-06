import imp
from urllib import response
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.urls import is_valid_path
import matplotlib.pyplot as plt

from .forms import UserRegistrationForm
from .forms import SentenceForm
from EnglishGrammar import grammar1
# Create your views here.

def parse_treeC(parse_tree):
    pronoun_c=parse_tree.count("pron")
    verb_c=parse_tree.count("verb")
    noun_c=parse_tree.count('noun')
    preposition_c=parse_tree.count("preposition")
    adjective_c=parse_tree.count("adjective")
    article_c=parse_tree.count("article")
    space_c=parse_tree.count("space")
    adverb_c=parse_tree.count("adverb")
    mark_c=parse_tree.count("mark")

    POS={
        "pron": pronoun_c,

        "verb": verb_c,

        "noun": noun_c,

        "preposition":preposition_c,

        "adjective":adjective_c,

        "article": article_c,

        "space": space_c,

        "adverb": adverb_c,

        "mark":mark_c

    }
    return POS

def dash(request):
    return render(request,'dashboard.html')

def SentenceAnalyzer(request):
    if request.method=='POST':
        form=SentenceForm(request.POST)
        if form.is_valid():
            sentence=request.POST.get('text')
            sentence=str(sentence).lower()
            stats=str(grammar1.parse(sentence))
        else:
            return render(request,'SentenceAnalyzer.html')
        output = parse_treeC(stats)

        return render(request,'SentenceAnalyzer.html',output)
    

    return render(request,'SentenceAnalyzer.html')
    

def register(request):
    if request.method=='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request,f'Your account has been created. You can log in now.')
            return redirect('login')
    else:
        form= UserRegistrationForm()

    context= {'form' : form}
    return render(request,'register.html',context)