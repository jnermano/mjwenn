# -*- coding: utf8 -*-
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import AnnonceForm, LoginForm, RegisterForm, ChangePassword, ProfilForm, AvatarForm, AdresseForm, PassLostForm
from django.http.response import HttpResponseRedirect
from .models import Annonce, Category, Type, Profile, Address

from obgest.forms import SearchForm, AlertForm
from datetime import date
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
import hashlib
from obgest.models import Question

vues = ['/annonce/', '/profil/']
def validate_file(value):
    ext = ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'PNG', 'JPG', 'JPEG', 'GIF', 'BMP']
    try:
        print value['Image'].content_type
        if value['Image'].content_type.split('/')[0] == 'image' and value['Image'].name.split('.')[-1] in ext:
            return ''
        else:
            return 'Seules les images sont acceptées'
    except Exception:
        print 'Exception Image : ', Exception.message
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
            ann = Annonce.objects.filter(owner_last_name__contains=a.owner_last_name, owner_first_name__contains=a.owner_first_name, type_annonce=2, type=a.type)
            for item in ann:
                msg = "Hello,"
                msg += u"<br>Une annonce correspondant à votre alerte a été publiée sur <b>Mjwenn</b>."
                msg += u"<br>Les informations soumises :<br>"
                msg += a.type.type +", "+ a.owner_first_name +" "+ a.owner_last_name
                msg += u"<br/><a href='http://mjwenn.com/details/"+str(a.id) +u"/'>Cliquez ici pour plus de détails!</a><br/>"
                msg += u"Merci d'utiliser <b>Mjwenn</b>.<br/>"
                msg += u"L'équipe <b>Mjwenn</b><br/>"
                send_mail(subject="Alerte Mjwenn", message=None, from_email="mjwenn@alwaysdata.net", recipient_list=[item.owner_email], html_message=msg)
            
            request.META['HTTP_REFERER'] = "annon"
            return HttpResponseRedirect('/')
    else:
        form = AnnonceForm()
        
    context = {'idmenu': 3, 'title':'Annoncez!', 'menu':'active', 'sous_title':u'Annoncez une carte trouvée', 'form':form, 'e':e, 'file_error':file_error, 'type':type_ok, 'contact':contact_ok or (add>0), 'address':addresses}
    return render(request, 'obgest/annonce.html', context)

def search(request):
    results = []
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            results = Annonce.objects.filter(owner_last_name__contains=form.cleaned_data['nom'], owner_first_name__contains=form.cleaned_data['prenom'], type_annonce__exact=1, type=form.cleaned_data['type'])
    
    else:
        form = SearchForm();
    context = {'idmenu': 4, 'title':'Recherchez!', 'menu':'active', 'sous_title':'Recherchez un objet sur mjwenn', 'form':form, 'results':results}
    return render(request, 'obgest/search.html', context)

@login_required
def alert(request):
    if request.method == "POST":
        form = AlertForm(request.POST)
        if form.is_valid():
            
            a = Annonce()
            
            a.user = Profile.objects.get(user=request.user)
            a.type_annonce = 2
            a.category = Category.objects.get(id=1)
            a.type = Type.objects.get(pk=form.cleaned_data['type'])
            a.owner_last_name = form.cleaned_data['nom']
            a.owner_first_name = form.cleaned_data['prenom']
            a.owner_tel = form.cleaned_data['contact_tel']
            a.owner_email = form.cleaned_data['contact_email']
            a.pub_date = date.today()
            a.save()
            return HttpResponseRedirect('/profil/')
    else:
        form = AlertForm();
            
    context = {'idmenu': 5, 'title':'Placer une alerte', 'menu':'active', 'sous_title':'Placez une alerte sur un objet', 'form':form}
    return render(request, 'obgest/alert.html', context)

def Mylogin(request):
    active_error = False
    error = False
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                if Profile.objects.get(user=user).is_active:
                    login(request, user)  # nous connectons l'utilisateur
                    request.session.set_expiry(1800)
                    return redirect(request.POST.get('next','/profil/'))
                else:
                    active_error = True
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = LoginForm();
        
    context = {'idmenu': 0, 'title':'Login', 'menu':'active', 'sous_title':'Authentification', 'form':form, 'active_error':active_error, 'error_auth':error}
    return render(request, 'obgest/login.html', context)

def Mylogout(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def profil(request):
    profile = Profile.objects.filter(user=request.user)[0]
    annonces = Annonce.objects.filter(user=profile)
    adresses = Address.objects.filter(user=profile)

    if request.method == 'POST':
        if 'btn_avatar' in request.POST:
            file_error = validate_file(request.FILES)
            print 'saving file ... '
            if file_error=='':
                profile.avatar = request.FILES.get('Image', "")
                profile.save()
                print 'file saved!'
        elif 'btn_password' in request.POST:
            passForm = ChangePassword(request.POST)
            if passForm.is_valid():
                request.user.set_password(passForm.clean()["password"])
                request.user.save()
                print 'password changed : ', passForm.clean()["password"]
        elif 'btn_adresse' in request.POST:
            adresseForm = AdresseForm(request.POST)
            if adresseForm.is_valid() and validate_contact(request.POST):
                adr = Address()
                adr.user = profile
                adr.contact_name= adresseForm.cleaned_data['contact_name']
                adr.contact_tel= adresseForm.cleaned_data['contact_tel']
                adr.contact_email= adresseForm.cleaned_data['contact_email']
                adr.contact_place= adresseForm.cleaned_data['contact_place']
                adr.desc= adresseForm.cleaned_data['desc']
                adr.add_date = date.today()
                adr.save()
                print 'adresse saved : ', adr.add_date
    

    formAvatar = AvatarForm()
    pform = ProfilForm()
    chgpass = ChangePassword()
    adresseForm = AdresseForm()
    
    context = {'idmenu': 0, 'title':'Profile', 'menu':'active', 'sous_title':'Espace utilisateur', 'profil':profile, 'annonces':annonces, 'adresses':adresses, 'avatar':formAvatar, 'proForm':pform, 'passForm':chgpass, 'adresseForm':adresseForm}
    return render(request, 'obgest/profile.html', context)

def register(request):
    errors = []
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            #passwd = form.cleaned_data['password']
            #passwd2 = form.cleaned_data['password_again']
            
            unam = User.objects.filter(username=username)
            em = User.objects.filter(email=email)
            if unam.count()>0:
                errors.append("pseudo non-disponible")
            if em.count()>0:
                errors.append(u"email déjà inscrit sur mjwenn")
            #passwd == passwd2 and 
            pss =  User.objects.make_random_password()
            print 'register password : ', pss
            
            if len(errors)==0:
                u = User.objects.create_user(username=username, email=email, password=pss)
                p = Profile(user=u)
                p.is_active = True
                p.secret_question = Question(form.cleaned_data['question'])
                p.secret_reponse = form.cleaned_data['reponse']
                p.hach = hashlib.sha1(u.email).hexdigest()
                p.save()
                
                msg = "Hello, <br/>"
                msg += "Merci de vous enregistrer sur <b>mjwenn></b>.<br/>"
                msg += "vos informations :<br/>"
                msg += "<b>email</b>: " + u.email + "<br/><b>pseudo</b> : " + u.username + "<br/><b>mot de passe</b>: " + pss
                msg += u"<br/>À bientôt sur <a href='http://mjwenn.com'>mjwenn</a><br/> L'équipe <b>mjwenn</b>"
                
                send_mail(subject="Nouveau compte", message=None, from_email="mjwenn@alwaysdata.net", recipient_list=[p.user.email], html_message=msg)
                #python -m smtpd -n -c DebuggingServer localhost:1025
                return HttpResponseRedirect('/login/')
    else:
        form = RegisterForm();
    context = {'idmenu': 0, 'title':'Nouveau compte', 'menu':'active', 'sous_title':u'Creer un compte mjwenn', 'form':form, 'errors':errors}
    return render(request, 'obgest/register.html', context)

def sendNewPassword(request):
    msg = []
    if request.method == 'POST': 
        form = PassLostForm(request.POST)
        if form.is_valid():            
            user = User.objects.filter(email=form.cleaned_data['email'])
            if len(user)>0:
                u = user[0]
                profil =  Profile.objects.filter(user=u, secret_question=form.cleaned_data['question'], secret_reponse=form.cleaned_data['reponse'])
                #print profil.secret_question, ', ', profil.secret_reponse
                if len(profil)>0:
                    password = User.objects.make_random_password()                    
                    u.set_password(password)
                    u.save()
                    msghtml = "Hello, <br/>"
                    msghtml += u"Récupération de mot de passe sur <b>mjwenn></b>.<br/>"
                    msghtml += "vos nouvelles informations :<br/>"
                    msghtml += "<b>email</b>: " + u.email + "<br/><b>pseudo</b> : " + u.username + "<br/><b>mot de passe</b>: " + password
                    msghtml += u"<br/>À bientôt sur <a href='http://mjwenn.com'>mjwenn</a><br/> L'équipe <b>mjwenn</b>"
                
                    send_mail(subject="Nouveau mot de passe", message=None, from_email="mjwenn@alwaysdata.net", recipient_list=[u.email], html_message=msghtml)
                
                    msg.append(u"Un message a été envoyé à "+u.email+u" , avec un nouveau mot de passe.")
                else:
                    msg.append(u"Email correct, mais la question et/ou la reponse non.")
            else:
                msg.append(u"Cette adresse n'est pas dans notre base de données. veuillez la vérifier!")
    else:
        form = PassLostForm()
    
    context = {'idmenu': 0, 'title':u'Récupération de compte', 'menu':'active', 'sous_title':u'Mot de passe oublié', 'form':form, 'msg':msg}
    return render(request, 'obgest/passLost.html', context)

def details_annonce(request, annonce_id=0):
    annonce = Annonce()
    if int(annonce_id) > 0:
        a = Annonce.objects.filter(id=int(annonce_id), type_annonce=1)
        if len(a)>0:
            annonce = a[0]
        else:
            annonce = Annonce()
    context = {'idmenu': 0, 'title':u'Détails annonce', 'menu':'active', 'sous_title':u'Détails annonce', 'annonce':annonce}
    return render(request, 'obgest/details.html', context)