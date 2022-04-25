from cProfile import label
from dataclasses import field
import imp
from tkinter import Label, Widget
from turtle import width
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



class Student(UserCreationForm):
    username = forms.CharField(label='User Name', widget= forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(label='First Name', widget= forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label='Last Name', widget= forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(label='Email', widget= forms.TextInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Conf Pass(again)', widget = forms.PasswordInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password', widget = forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields =["username","first_name","last_name","email"]
        labels = {'username':'User Name','first_name':'First Name', 'last_name':'Last Name','email':'Email'}
        
        Widget = {'username':forms.TextInput(attrs={'class':'form-control'}),
                  'first_name':forms.TextInput(attrs={'class':'form-control'}),
                  'last_name':forms.TextInput(attrs={'class':'form-control'}),
                  'email': forms.EmailInput(attrs={'class':'form-control'}),
                  }
        
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='User Name',widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ["username","password"]
        