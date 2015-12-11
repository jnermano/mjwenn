# -*- coding: latin1 -*-
from django import forms
from django.forms import ModelForm
from .models import Category, Type, Annonce, Question


def toList(l, type):
    res = []
    res.append((0, u'Type de carte'))
    for x in l:
        if type == 'cat':
            res.append((x.id, x.category))
        elif type == 'type':
            res.append((x.id, x.type))
    return res

#[('0', '--Categorie--'),('1', 'Identification')]
class AnnonceForm(forms.Form):
    #Category = forms.ChoiceField(choices=toList(Category.objects.all(), 'cat'), widget=forms.Select(attrs={'class':'form-control'}))
    Type_de_carte = forms.ChoiceField(choices=toList(Type.objects.all(), 'type'), widget=forms.Select(attrs={'class':'form-control'}))
    Nom_proprietaire = forms.CharField(label='Nom', widget=forms.TextInput(attrs={'class':'form-control'}))
    Prenom_proprietaire = forms.CharField(label=u'Prénom du propriétaire', widget=forms.TextInput(attrs={'class':'form-control'}))
    Image = forms.FileField(required=False)
    
    contact_name = forms.CharField(required=False, label=u'Votre nom / Nom de l\'entreprise', widget=forms.TextInput(attrs={'class':'form-control'}))
    contact_tel = forms.CharField(required=False, label=u'Tel', widget=forms.TextInput(attrs={'class':'form-control'}))
    contact_email = forms.CharField(required=False, label=u'Email', widget=forms.TextInput(attrs={'class':'form-control'}))
    contact_place = forms.CharField(required=False, label=u'Adresse', widget=forms.TextInput(attrs={'class':'form-control'}))
    desc = forms.CharField(required=False, label=u'Autres détails', widget=forms.Textarea(attrs={'class':'form-control', 'cols':'50', 'rows':'3'}))
    
class SearchForm(forms.Form):
    #Category = forms.ChoiceField(required=False, choices=toList(Category.objects.all(), 'cat'), widget=forms.Select(attrs={'class':'form-control'}))
    type = forms.ChoiceField(required=False, choices=toList(Type.objects.all(), 'type'), widget=forms.Select(attrs={'class':'form-control'}))
    nom = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    prenom = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

class AlertForm(forms.Form):
    #Category = forms.ChoiceField(choices=toList(Category.objects.all(), 'cat'), widget=forms.Select(attrs={'class':'form-control'}))
    type = forms.ChoiceField(choices=toList(Type.objects.all(), 'type'), widget=forms.Select(attrs={'class':'form-control'}))
    nom = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    prenom = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    contact_tel = forms.CharField(label=u'Tel', widget=forms.TextInput(attrs={'class':'form-control'}))
    contact_email = forms.CharField(label=u'Email', widget=forms.TextInput(attrs={'class':'form-control'}))
    
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'pseudo'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'mot de passe'}))
    
class RegisterForm(forms.Form):
    username = forms.CharField(label=u'Pseudo', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label=u'E-mail', widget=forms.TextInput(attrs={'class':'form-control'}))
    #password = forms.CharField(label=u'Mot de passe', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    #password_again = forms.CharField(label=u'Répéter mot de passe', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    question = forms.ChoiceField(label=u'Question secrète' , choices=[(x.id, x.question) for x in Question.objects.all()], widget=forms.Select(attrs={'class':'form-control'}))
    reponse = forms.CharField(label=u'Réponse', widget=forms.TextInput(attrs={'class':'form-control'}))

class QuickSearch(forms.Form):
    nom = forms.CharField(label=u'Nom', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nom'}))
    prenom = forms.CharField(label=u'Préom', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':u'Préom'}))
    
class ChangePassword(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={}))
    passagain = forms.CharField(widget=forms.PasswordInput(attrs={}))
    
    def clean(self):
        pass1 = self.cleaned_data.get('password')
        pass2 = self.cleaned_data.get('passagain')
        if pass1 and pass1 != pass2:
            raise forms.ValidationError('Les mots de passe ne correspondent pas')
        return self.cleaned_data
    
class ProfilForm(forms.Form):
    firstname = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    siteweb = forms.CharField(required=False, widget=forms.URLInput(attrs={'class':'form-control'}))

class AvatarForm(forms.Form):
    Image = forms.FileField(required=True)
    
class AdresseForm(forms.Form):
    contact_name = forms.CharField(required=False, label=u'Votre nom / Nom de l\'entreprise', widget=forms.TextInput(attrs={'class':'form-constrol'}))
    contact_tel = forms.CharField(required=False, label=u'Tel', widget=forms.TextInput(attrs={'class':'form-cosntrol'}))
    contact_email = forms.CharField(required=False, label=u'Email', widget=forms.TextInput(attrs={'class':'forsm-control'}))
    contact_place = forms.CharField(required=False, label=u'Adresse', widget=forms.TextInput(attrs={'class':'fsorm-control'}))
    desc = forms.CharField(required=False, label=u'Autres détails', widget=forms.Textarea(attrs={'class':'forms-control', 'cols':'50', 'rows':'3'}))
    
class PassLostForm(forms.Form):
    email = forms.EmailField(required=True, label=u'Email', widget=forms.EmailInput(attrs={'class':'form-control'}))
    question = forms.ChoiceField(choices=[(x.id, x.question) for x in Question.objects.all()], widget=forms.Select(attrs={'class':'form-control'}))
    reponse = forms.CharField(label=u'Réponse', widget=forms.TextInput(attrs={'class':'form-control'}))
