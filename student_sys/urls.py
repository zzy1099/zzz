from django.conf.urls import url
from django.contrib import admin

from student.views import index

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^admin/', admin.site.urls),
]
