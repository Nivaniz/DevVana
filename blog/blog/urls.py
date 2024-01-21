"""
Proyecto Curso Django
"""
from django.contrib import admin
from django.urls import path, re_path, include
from ckeditor_uploader.views import upload, browse  
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('applications.users.urls')),
    path('', include('applications.home.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')) # Hay otros 188 modificados igual que este yo los tengo diferentes
     # path('ckeditor_upload/', upload, name='ckeditor_upload'),
     # path('ckeditor_browse/', browse, name='ckeditor_browse'),    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)