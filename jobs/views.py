from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Job


def index(request):
    jobs = Job.objects.order_by('start_date')[:5]
    # output = ', '.join([('<a href="./' + str(j.id) + '">' + j.title + '</a>') for j in jobs])
    template = loader.get_template('jobs/index.html')
    context = {
        'jobs': jobs,
    }
    return HttpResponse(template.render(context, request))


def detail(request, job_id):
    job = Job.objects.get(id=job_id)
    output = '' + str(job)
    for attr, value in job.__dict__.items():
        # output += ' ' + str(attr) + ' '
        output += '<div class="job ' + attr + '">' + attr + ': ' + str(value) + '</div>'
    return HttpResponse(output)

