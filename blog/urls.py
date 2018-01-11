from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^about/$', views.about, name='about'),
	url(r'^courses/$', views.courses, name='courses'),
	url(r'^join/$', views.join, name='join'),
	url(r'^pages/icons/$', views.pages_icons, name='pages_icons'),
	url(r'^pages/codes/$', views.pages_codes, name='pages_codes'),
	url(r'^gallery/$', views.gallery, name='gallery'),
	url(r'^contact/$', views.contact, name='contact'),
	url(r'^login/$', views.login, name='login'),
	url(r'^register/$', views.register, name='register'),

	url(r'^lecture/NP_1$', views.Lecture_NP_1, name='Lecture_NP_1'),
	url(r'^lecture/NP_2$', views.Lecture_NP_2, name='Lecture_NP_2'),
	url(r'^lecture/GS$', views.Lecture_GS, name='Lecture_GS'),

	url(r'^post/$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]