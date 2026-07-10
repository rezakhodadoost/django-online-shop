from django import forms
from .models import Signup

#signup form
class SignupForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = ["name","phone","password"]



        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Name",
            }),

            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Phone Number",
            }),
            "password": forms.PasswordInput(attrs={
                "class": "form-control",
                "placeholder": "Password",
            }),

        }
#login form
class LoginForm(forms.Form):

    phone= forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
#comment form
class CommentForm(forms.Form):

    text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder":"Write your comment...",
                "rows":4
            }
        )
    )