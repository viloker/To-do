from django import forms

class AddTask(forms.Form):
    task = forms.CharField(label='Your task', max_length=64)
