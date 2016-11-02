from django import forms

from ecosystem.models import Register,ModelRegister
from django.forms import widgets



class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ["email","title","first_name","last_name","birth_date","address_1","city","province","postal_code","telephone_number"]
        widgets = {
            "birth_date":forms.DateTimeInput(
                attrs={'class': 'datepicker'}
            )
        }

class ModelForm(forms.ModelForm):
    class Meta:
        model = ModelRegister
        fields=["purchase_date","robot_model","channel","recommendation"]
        widgets ={
            "purchase_date":forms.DateTimeInput(
                attrs={'class':'datepicker'}
            )
        }