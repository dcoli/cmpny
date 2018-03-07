from django.contrib.auth import authenticate
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
# from django.http import HttpResponseRedirect
from django.template import loader
from .models import Job


def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def login(request, email, password):
    user = authenticate(user=email, password=password)
    if user is not None:
        return redirect("/", systemMessage="That combination of email and password does not work.")
    else:
        return redirect('/jobs/')


def jobs(request):
    jobs = Job.objects.order_by('start_date')[:5]
    # output = ', '.join([('<a href="./' + str(j.id) + '">' + j.title + '</a>') for j in jobs])
    template = loader.get_template('jobs/index.html')
    context = {
        'jobs': jobs,
    }
    return HttpResponse(template.render(context, request))


def detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    output = '' + str(job)
    for attr, value in job.__dict__.items():
        # output += ' ' + str(attr) + ' '
        output += '<div class="job ' + attr + '">' + attr + ': ' + str(value) + '</div>'
    return HttpResponse(output)

