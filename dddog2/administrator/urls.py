from django.conf.urls import url
from administrator import views


urlpatterns = [
    url(r'^test',views.test,name='test'),
    url(r'^add-limits',views.add_limits,name='add-limits'),
    url(r'^inquire-limits',views.inquire_limits,name='inquire-limits'),
    url(r'^update-limits',views.update_limits,name='update-limits'),
    url(r'^delete-limits',views.delete_limits,name='delete-limits'),
    url(r'^create-groups',views.create_groups,name='create-groups'),
    url(r'^update-groups',views.update_groups,name='update-groups'),
    url(r'^inquire-groups-infos',views.inquire_groups_infos,name='inquire-groups-infos'),
    url(r'^inquire-group-users',views.inquire_group_users,name='inquire-group-users'),
    url(r'^inquire-group-limits',views.inquire_group_limits,name='inquire-group-limits'),
]