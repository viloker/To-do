from django import forms

class Create_User(forms.Form):
    user_name = forms.CharField(label='Your username: ')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')