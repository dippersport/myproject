"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
    path('',include('myapp2.urls')),
    #path('__debug__/', include("debug_toolbar.urls")),
]
# ALTER DATABASE Jeyhun$default CHARACTER SET utf8 COLLATE utf8_general_ci; 
# echo "export SECRET_KEY=c29d1a851acdebbec1c68eb244f5debfa1b58ca3a1a874020e43736808baaae2" >> .env
# echo "export MYSQL_PASSWORD=Kingsport123." >> .env
# echo 'set -a; source ~/myproject1/.env; set +a' >> ~/.virtualenvs/virtualenv/bin/postactivate
# git remote add origin https://github.com/username/myproject.git
#  git push -u origin master
