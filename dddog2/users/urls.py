from django.conf.urls import url, include
from users import views


urlpatterns = [
    url(r'^test',views.test,name='test')
]