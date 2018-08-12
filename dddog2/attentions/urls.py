from django.conf.urls import url
from attentions import views


urlpatterns = [
    url(r'^test',views.test,name='test'),
    url(r'^attentions-cancels',views.attentions_cancels,name='attentions-cancels'),
    url(r'^inquire-attentions',views.inquire_attentions,name='inquire-attentions'),
]