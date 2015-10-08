# -*- coding: utf8 -*-
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import AnnonceForm, LoginForm, RegisterForm
from django.http.response import HttpResponseRedirect
from .models import Annonce, Category, Type, Profile, Address

from obgest.forms import SearchForm, AlertForm
from time import timezone
from datetime import date
from django.template.context_processors import request
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

vues = ['/annonce/', '/profil/']
def validate_file(value):
    ext = ['jpg', 'jpeg', 'png', 'gif', 'bmp']
    try:
        print value['Image'].content_type
        if value['Image'].content_type.split('/')[0] == 'image' and value['Image'].name.split('.')[-1] in ext:
            return ''
        else:
            return 'Seules les images sont acceptées'
    except Exception:
        return ""
    else:
        return ""
def validate_type(value):
    return value != '0'

def validate_contact(form):
    return len(form['contact_name'])>3 or len(form['contact_tel'])>8 or len(form['contact_email'])>8 or len(form['contact_place'])>6
    

# Create your views here.
def home(request):
    annonce_done = False #request.META['HTTP_REFERER'].split('/')[-2] == 'annonce'   
    context = {'idmenu': 1, 'title':'Accueil', 'menu':'active', 'sous_title':'Mjwenn', 'annonce':annonce_done}
    return render(request, 'obgest/home.html', context)

def about(request):
    context = {'idmenu': 2, 'title':'Nous sommes...', 'menu':'active', 'sous_title':'L\'equipe mjwenn'}
    return render(request, 'obgest/about.html', context)

@login_required
def annonce(request):
    e = u'é'
    file_error = ''
    type_ok = True
    contact_ok = True
    add = 1
    addresses = Address.objects.filter(user=Profile.objects.filter(user=request.user))
    if request.method == 'POST':
        form = AnnonceForm(request.POST, request.FILES)
        
        file_error = validate_file(request.FILES)
        type_ok = validate_type(request.POST['Type_de_carte'])
        contact_ok = validate_contact(request.POST)
        
        try:
            add = request.POST['adresse']
            the_address = Address.objects.filter(id=add, user=Profile.objects.filter(user=request.user))
            if len(the_address)<1:
                add=0
            else:
                print the_address[0].user
        except Exception:
            add = 0
            
        if form.is_valid() and file_error=='' and type_ok and (contact_ok or add>0):
            
            a = Annonce()
            if add > 0:
                a.address = the_address[0]
            else:
                adr = Address()
                adr.user=Profile.objects.get(user=request.user)
                adr.contact_name= form.cleaned_data['contact_name']
                adr.contact_tel= form.cleaned_data['contact_tel']
                adr.contact_email= form.cleaned_data['contact_email']
                adr.contact_place= form.cleaned_data['contact_place']
                adr.desc= form.cleaned_data['desc']
                adr.add_date = date.today()
                adr.save()
                a.address = adr
                                
            a.user = Profile.objects.get(user=request.user)
            a.type_annonce = 1
            a.category = Category.objects.get(id=1)
            a.type = Type.objects.get(pk=form.cleaned_data['Type_de_carte'])
            a.owner_first_name = form.cleaned_data['Prenom_proprietaire']
            a.owner_last_name = form.cleaned_data['Nom_proprietaire']
            a.picture = request.FILES.get('Image', "")
            a.pub_date = date.today()
            
            a.save()
            request.META['HTTP_REFERER'] = "annon"
            return HttpResponseRedirect('/')
    else:
        form = AnnonceForm()
        
    context = {'idmenu': 3, 'title':'Annoncez!', 'menu':'active', 'sous_title':u'Annoncez une carte trouvée', 'form':form, 'e':e, 'file_error':file_error, 'type':type_ok, 'contact':contact_ok or (add>0), 'address':addresses}
    return render(request, 'obgest/annonce.html', context)

def search(request):
    form = SearchForm();
    context = {'idmenu': 4, 'title':'Recherchez!', 'menu':'active', 'sous_title':'Recherchez un objet sur mjwenn', 'form':form}
    return render(request, 'obgest/search.html', context)

def alert(request):
    form = AlertForm();
    context = {'idmenu': 5, 'title':'Placer une alerte', 'menu':'active', 'sous_title':'Placez une alerte sur un objet', 'form':form}
    return render(request, 'obgest/alert.html', context)

def Mylogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
                return redirect(request.POST.get('next','/profil/'))
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = LoginForm();
        
    context = {'idmenu': 0, 'title':'Login', 'menu':'active', 'sous_title':'Authentification', 'form':form}
    return render(request, 'obgest/login.html', context)

def Mylogout(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def profil(request):
    profile = Profile.objects.filter(user=request.user)[0]
    context = {'idmenu': 0, 'title':'Profile', 'menu':'active', 'sous_title':'Espace utilisateur', 'profil':profile}
    return render(request, 'obgest/profile.html', context)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            passwd = form.cleaned_data['password']
            passwd2 = form.cleaned_data['password_again']
            if passwd == passwd2:
                u = User.objects.create_user(username, email, passwd)
                p = Profile(user=u)
                p.save()
                return HttpResponseRedirect('/login/')
    else:
        form = RegisterForm();
    context = {'idmenu': 0, 'title':'Nouveau compte', 'menu':'active', 'sous_title':u'Creer un compte mjwenn', 'form':form}
    return render(request, 'obgest/register.html', context)

