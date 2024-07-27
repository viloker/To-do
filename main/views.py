from django.shortcuts import render, redirect

from django.http import HttpResponse

from . import forms

from . import models


def check_user(request):
    if 'check_user' in request.session:
        return redirect('show_tasks')
    return redirect('log_in')


def log_in(request):
    try_again = False
    if request.method == "POST":
        form = forms.Create_User(request.POST)

        if form.is_valid():

            request.session['check_user'] = True
            request.session['username'] = form.cleaned_data['user_name']

            user = models.search_user(request.session['username'])

            if user:
                if models.correct_password(user, form.cleaned_data['password']):
                    request.session['tasks'] = models.get_tasks(user.get('username'))
                try_again = True
            else:
                models.add_user(request.session.get('username'), form.cleaned_data['password'])
                request.session['tasks'] = []

            return redirect('show_tasks')

    form = forms.Create_User()
    return render(request, 'log_in.html', {'form': form, 'try_again': try_again})


def add_task(request):
    if request.method == 'POST':
        task = request.POST.get('InputTask', '')

        models.add_task(request.session.get('username'), task)
        request.session['tasks'] = models.get_tasks(request.session.get('username'))
    return render(request, 'add_task.html')


def delete_task(request, task):
    models.del_task(request.session.get('username'), task)
    request.session['tasks'] = models.get_tasks(request.session.get('username'))
    return redirect('show_tasks')

def show_tasks(request):
    tasks = request.session.get('tasks')
    return render(request, 'show_tasks.html', {'tasks':tasks})
