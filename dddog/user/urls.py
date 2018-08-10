from django.conf.urls import url, include
from user import views


urlpatterns = [
    url(r'^test',views.test,name='test')
]