from django.conf.urls import url

from . import views


app_name = 'base'
urlpatterns = [
    url(r'^contact/', views.ContactView.as_view(), name='contact'),
    url(r'^encryption/data_file/', views.EncryptionData.as_view(), name='encryption_data'),
    url(r'^encryption/key_file/', views.EncryptionKey.as_view(), name='encryption_key'),
    url(r'^decryption/data_file/', views.DecryptionData.as_view(), name='decryption_data'),
    url(r'^decryption/key_file/', views.DecryptionKey.as_view(), name='decryption_key'),
    url(r'^select_algorithm/(?P<type>[\w]+)/', views.SelectAlgorithm, name='select_algorithm'),
    url(r'^result/', views.VisualAnalysis.as_view(), name='visual_analysis'),
    url(r'^$', views.IndexView.as_view(), name='index'),
]
