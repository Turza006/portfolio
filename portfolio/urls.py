from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
import jobs.views
import accounts.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',accounts.views.login,name = 'login'),
    path('home/',jobs.views.home,name = 'home'),
    path('create',jobs.views.create,name = 'create'),
    path('blog/', include('blog.urls')),
    path('accounts/', include('accounts.urls')),
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)