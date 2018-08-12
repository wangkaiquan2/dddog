from django.conf.urls import url
from attentions import views


urlpatterns = [
    url(r'^test',views.test,name='test'),
    url(r'^attentions-cancels',views.attentions_cancels,name='attentions-cancels'),
    url(r'^cancel-attentions',views.cancel_attentions,name='cancel-attentions'),
    url(r'^inquire-attentions',views.inquire_attentions,name='inquire-attentions'),
    url(r'^inquire-fan',views.inquire_fan,name='inquire-fan'),
]