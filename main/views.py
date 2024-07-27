from django.shortcuts import render, redirect

from django.http import HttpResponse

from . import forms

from . import models


def check_user(request):
    if 'check_user' in request.session:
        return redirect('show_tasks')
    return redirect('log_in')


def log_in(request):
    if request.method == "POST":
        form = forms.Create_User(request.POST)

        if form.is_valid():

            request.session['check_user'] = True
            request.session['username'] = form.cleaned_data['user_name']

            user = models.search_user(request.session['username'])

            if user:
                request.session['tasks'] = models.get_tasks(user.get('username'))
            else:
                models.add_user(request.session.get('username'), form.cleaned_data['password'])
                request.session['tasks'] = []

            return redirect('show_tasks')

    form = forms.Create_User()
    return render(request, 'log_in.html', {'form': form})


def add_task(reqeust, task):
    ...


def show_tasks(reqeust):
    print(reqeust.session.get('tasks'))
    return HttpResponse(f'show_tasks')
