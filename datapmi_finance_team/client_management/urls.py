from django.urls import path

from .views import homepage, add_employee, filter_employee, signup, signin, logout_user, signout

urlpatterns = [
    path('homepage/',homepage,name='homepage'),
    # path('profileview/',profileview,name='profileview'),
    path('add_employee/',add_employee,name='add_employee'),
    path('filter_employee/',filter_employee,name='filter_employee'),
    # path('calender/',calender,name='calender'),
    path('signup/',signup,name='signup'),
    path('',signin,name='login'),
    path('logout/',logout_user,name='logout'),
    path('signout/',signout,name='signout'),
    
]






