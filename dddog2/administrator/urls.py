from django.conf.urls import url
from administrator import views

urlpatterns = [
    url(r'^test', views.test, name='test'),
    url(r'^add-limits', views.add_limits, name='add-limits'),
    url(r'^inquire-limits', views.inquire_limits, name='inquire-limits'),
    url(r'^update-limits', views.update_limits, name='update-limits'),
    url(r'^delete-limits', views.delete_limits, name='delete-limits'),
    url(r'^create-groups', views.create_groups, name='create-groups'),
    url(r'^update-groups', views.update_groups, name='update-groups'),
    url(r'^inquire-groups-infos', views.inquire_groups_infos, name='inquire-groups-infos'),
    url(r'^inquire-group-users', views.inquire_group_users, name='inquire-group-users'),
    url(r'^inquire-group-limits', views.inquire_group_limits, name='inquire-group-limits'),
    url(r'^add-group-users', views.add_group_users, name='add-group-users'),
    url(r'^remove-group-users', views.remove_group_users, name='remove-group-users'),
    url(r'^add-group-limits', views.add_group_limits, name='add-group-limits'),
    url(r'^remove-group-limits', views.remove_group_limits, name='remove-group-limits'),
    url(r'^add-user-limits', views.add_user_limits, name='add-user-limits'),
    url(r'^remove-user-limits', views.remove_user_limits, name='remove-user-limits'),
    url(r'^inquire-user-groups', views.inquire_user_groups, name='inquire-user-groups'),
    url(r'^inquire-user-limits', views.inquire_user_limits, name='inquire-user-limits'),
]
