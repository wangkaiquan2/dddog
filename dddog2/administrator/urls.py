from django.conf.urls import url
from administrator import views


urlpatterns = [
    url(r'^test',views.test,name='test'),
    url(r'^add-limits',views.add_limits,name='add-limits'),
    url(r'^inquire-limits',views.inquire_limits,name='inquire-limits'),
    url(r'^update-limits',views.update_limits,name='update-limits'),
    url(r'^delete-limits',views.delete_limits,name='delete-limits'),
]