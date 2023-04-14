from django.shortcuts import render
from formsapp import forms
# Create your views here.

def feedbackview(request):
    form=forms.Form_creation()
    if request.method=='POST':
        form=forms.Form_creation(request.POST)
        if form.is_valid():
            print("form validation seucess and printing information here")
            print("FirstName",form.cleaned_data['FirstName'])
    my_dict={'form':form}           
    return render(request,'html.html',my_dict)