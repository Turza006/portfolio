

from django.urls import path,include

from django.conf.urls.static import static

from .import views
import accounts

urlpatterns = [


    path('signup/',views.signup, name='signup'),
    path('login/',views.login, name='login'),
    path('logout/',views.login, name='logout'),

]