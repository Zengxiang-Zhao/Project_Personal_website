from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
app_name = 'users'
urlpatterns = [
	# LoginView is a class so we should use the class style class.as_view()
	path('login/', LoginView.as_view(template_name='users/login.html'), name='login' ),
	path('logout/', LogoutView.as_view(template_name='app_pw/index.html'),name='logout'),

]

