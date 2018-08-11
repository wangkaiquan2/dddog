from django.conf.urls import url
from users import views

urlpatterns = [
    url(r'^test', views.test, name='test'),
    url(r'^registers', views.registers, name='registers'),
    url(r'^logins', views.logins, name='logins'),
    url(r'^quits', views.quits, name='quits'),
    url(r'^inquire-logins', views.inquire_logins, name='inquire-logins'),
    url(r'^inquire-user-infos', views.inquire_user_infos, name='inquire-user-infos'),
    url(r'^update-user-infos', views.update_user_infos, name='update-user-infos'),
    url(r'^update-passwords', views.update_passwords, name='update-passwords'),
]
