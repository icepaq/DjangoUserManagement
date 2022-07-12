from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import logging

logger = logging.getLogger(__name__)

from .models import User

def index(request):
    user_list = User.objects.all()
    logger.info('sdfsdfsdfsdfsdfsdf')
    

    template = loader.get_template('users/index.html')
    context = {
        'user_list': user_list,
        'user_count': len(user_list),
    }
    return HttpResponse(template.render(context, request))

def edit(request, user_id):
    user = User.objects.get(id=user_id)
    template = loader.get_template('edit/edit.html')

    print(user.first_name)
    context = {
        'user': user,
    }
    return HttpResponse(template.render(context, request))

@csrf_exempt
def submitedit(request, user_id):
    user = User.objects.get(id=user_id)

    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.email = request.POST['email']
    user.number = request.POST['number']
    user.role = request.POST['role']

    user.save()

    return HttpResponse('ok')

@csrf_exempt
def delete(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return HttpResponseRedirect('ok')

@csrf_exempt
def create_new_user(request):
    logging.debug('create_new_user')
    user = User(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        number=request.POST['number'],
        role=request.POST['role'],
    )

    user.save()
    return HttpResponseRedirect('ok')

def new(request):
    template = loader.get_template('new/new.html')
    context = {}
    return HttpResponse(template.render(context, request))