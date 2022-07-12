from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic import ListView, DetailView
from django.views.decorators.csrf import csrf_exempt
from .models import User, UserForm

class UserListView(ListView):
    model = User
    template_name = 'users/index.html'

def edit(request, user_id):
    user = User.objects.get(id=user_id)
    template = loader.get_template('edit/edit.html')

    context = {
        'user': user,
    }

    return HttpResponse(template.render(context, request))

@csrf_exempt
def submitedit(request, user_id):
    user = User.objects.get(id=user_id)
    form = UserForm(request.POST, instance=user)
    form.save()

    return HttpResponse('ok')

@csrf_exempt
def delete(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return HttpResponseRedirect('ok')

@csrf_exempt
def create_new_user(request):
    user = UserForm(request.POST)
    user.save()

    return HttpResponseRedirect('ok')

def new(request):
    template = loader.get_template('new/new.html')
    context = {}
    return HttpResponse(template.render(context, request))