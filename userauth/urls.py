from django.conf.urls import url
from . import views
from django.contrib.auth import views as  authViews

urlpatterns = [
    url(r'^signup/$', views.signup, name="signup"),
    url(r'^login/$', views.login_user, name="login.html"),
    # url(r'^logout/$', authViews.logout, {'template_name':'userauth/logout.html'}),
    url(r'^logout/$',authViews.LogoutView.as_view(template_name='userauth/logout.html'))
#    url(r'^login/$', views.login, name="login"),
]
