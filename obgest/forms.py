# -*- coding: latin1 -*-
from django import forms
from django.forms import ModelForm
from .models import Category, Type, Annonce


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
    Type = forms.ChoiceField(required=False, choices=toList(Type.objects.all(), 'type'), widget=forms.Select(attrs={'class':'form-control'}))
    Nom = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Prenom = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

class AlertForm(forms.Form):
    #Category = forms.ChoiceField(choices=toList(Category.objects.all(), 'cat'), widget=forms.Select(attrs={'class':'form-control'}))
    Type = forms.ChoiceField(choices=toList(Type.objects.all(), 'type'), widget=forms.Select(attrs={'class':'form-control'}))
    Nom = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Prenom = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    contact_tel = forms.CharField(label=u'Tel', widget=forms.TextInput(attrs={'class':'form-control'}))
    contact_email = forms.CharField(required=False, label=u'Email', widget=forms.TextInput(attrs={'class':'form-control'}))
    
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
class RegisterForm(forms.Form):
    username = forms.CharField(label=u'Pseudo', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label=u'E-mail', widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label=u'Mot de passe', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password_again = forms.CharField(label=u'Répéter mot de passe', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    
    