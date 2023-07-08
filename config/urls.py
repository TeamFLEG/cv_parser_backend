from django.contrib import admin
from django.urls import path, include

import authentication
import fileupload

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('upload/', include('fileupload.urls')),
]
