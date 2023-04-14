from django import forms

class Form_creation(forms.Form):
    FirstName=forms.CharField()
    LastName=forms.CharField()
    Password=forms.PasswordInput()
    re_password=forms.PasswordInput()
    Phone=forms.IntegerField(label="optional" ,required=False)
