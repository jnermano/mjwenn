from django.conf.urls import url
from . import views
from mjwenn.settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home, name='home'), 
    url(r'^apropos/$', views.about, name='about'),
    url(r'^annonce/$', views.annonce, name='annonce'),
    url(r'recherche/$', views.search, name='search'),
    url(r'alerte/$', views.alert, name='alert'),
    url(r'login/$', views.Mylogin, name='login'),
    url(r'profil/$', views.profil, name='profil'),
    url(r'register/$', views.register, name='register'),
    url(r'logout/$', views.Mylogout, name='logout'),
    url(r'mot_de_passe_perdu/$', views.sendNewPassword, name='new_password'),
    url(r'(?P<annonce_id>[0-9]+)/$', views.details_annonce, name="details_annonce"),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)