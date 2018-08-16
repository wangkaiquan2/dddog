from django.conf.urls import url
from releases import views

urlpatterns = [
    url(r'^test', views.test, name='test'),
    url(r'^add-states', views.add_states, name='add-states'),
    url(r'^inquire-states', views.inquire_states, name='inquire-states'),
    url(r'^update-states', views.update_states, name='update-states'),
    url(r'^upload-files', views.upload_files, name='upload-files'),
    url(r'^download-files', views.download_files, name='download-files'),
    url(r'^download', views.download, name='download'),
]
