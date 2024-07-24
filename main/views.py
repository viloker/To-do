from django.shortcuts import render, redirect

from django.http import HttpResponse

from . import forms

all_tasks = []


def delete_task(request, index):
    del all_tasks[index]
    return redirect('index')


def index(request):
    if request.method == 'POST':
        form = forms.AddTask(request.POST)

        if form.is_valid():
            all_tasks.append(form.cleaned_data['task'])
            # request.session['tasks'] = form.cleaned_data['task']
            print(all_tasks)


    form = forms.AddTask()
    return render(request, 'index.html', {'form': form, 'tasks': all_tasks})
