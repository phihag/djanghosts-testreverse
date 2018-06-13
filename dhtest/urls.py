from django.conf.urls import url

from django.http import HttpResponse

urlpatterns = [
    url(r'^view1/', lambda _: HttpResponse('This is view1'), name='view1'),
]
