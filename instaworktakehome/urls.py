"""instaworktakehome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from usermanagement import views as usermanagement_views

app_name = 'usermanagement'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', usermanagement_views.UserListView.as_view(), name='index'),
    path('edit/<int:user_id>/', usermanagement_views.edit, name='edit'),
    path('edit/submitedit/<int:user_id>/', usermanagement_views.submitedit, name='submitedit'),
    path('delete/<int:user_id>/', usermanagement_views.delete, name='delete'),
    path('createnewuser/', usermanagement_views.create_new_user, name='createnewuser'),
    path('new/', usermanagement_views.new, name='new'),
]
