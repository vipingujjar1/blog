"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url,include
from blogapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.post_list),
    path('detail/<int:pk>',views.detail_view.as_view()),
    path('logout/',views.logout_page),
    path('signup/',views.signup_page),
    url('accounts/',include('django.contrib.auth.urls')),
    path('dashboard/',views.dashboard),
    path('dashboard/<int:pk>/update',views.update_view),
    path('dashboard/<int:pk>/delete',views.delete_view),
    path('create/',views.create_view),

]
