"""
URL configuration for libmanager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import books.views
import users.views
from users.views import RegisterUser, LoginUser
from libmanager import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', books.views.BookHome.as_view()),
    path('books/', include('books.urls')),
    path('users/', include('users.urls')),
    path('register/', users.views.RegisterUser.as_view(), name='register'),
    path('login/', users.views.LoginUser.as_view(), name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = books.views.page_not_found
