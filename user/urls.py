from django.urls import path
from . import views
from .views import register_view,login_view,register_table_view

urlpatterns = [
	
	path('login/', views.UserLogin.as_view(), name='login'),
    


	path('logout/', views.UserLogout.as_view(), name='logout'),
]