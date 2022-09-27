
from django.urls import  include, re_path
from django.contrib.auth import views as auth_views 
from . import views

urlpatterns = [
        re_path(r'^register/$', views.register,name="register"),
        # re_path('^logout', views.logout_view,name="logout"),
        # re_path('^login', views.logout_view,name="login"),
        re_path(r'^password_change/$',auth_views.PasswordChangeView.as_view() ,{'template_name': 'profiles/change-password.html'}),
        re_path(r'^password_change/done',
    auth_views.PasswordChangeDoneView.as_view(),{'template_name':'profiles/password_change_done.html'}),
        re_path(r'^login/$', auth_views.LoginView.as_view()),
        re_path(r'^logout/$', auth_views.LogoutView.as_view(),{'next_page': '/'}),
        re_path(r'^', include('django.contrib.auth.urls')),
]
app_name = 'accounts'