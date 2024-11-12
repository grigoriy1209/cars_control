"""
URL configuration for configs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.urls import include, path

urlpatterns = [
    path('api/all_users/users', include('apps.all_users.users.urls')),
    path('api/all_users/admins', include('apps.all_users.admins.urls')),
    path('api/all_users/auth', include('apps.all_users.auth.urls')),
    path('api/all_users/accounts', include('apps.all_users.accounts.urls')),
]
