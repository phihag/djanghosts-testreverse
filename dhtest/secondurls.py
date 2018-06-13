from django.conf.urls import url

from django.http import HttpResponse

urlpatterns = [
    url(r'^view2/', lambda _: HttpResponse('view2 on another host')),
]
