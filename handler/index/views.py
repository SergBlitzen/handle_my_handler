from django.shortcuts import render

from index.models import Handler


def index(request):

    handler = Handler.objects.all()[0]
    template = 'index.html'
    context = {
        'handler': handler
    }

    return render(request, template, context)
