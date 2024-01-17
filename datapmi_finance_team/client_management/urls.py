from django.urls import path

from .views import homepage, profileview, add_employee, filter_employee, calender, signup, signin, logout, signout

urlpatterns = [
    path('homepage/',homepage,name='homepage'),
    path('profileview/',profileview,name='profileview'),
    path('add_employee/',add_employee,name='add_employee'),
    path('filter_employee/',filter_employee,name='filter_employee'),
    path('calender/',calender,name='calender'),
    path('signup/',signup,name='signup'),
    path('login/',signin,name='login'),
    path('logout/',logout,name='logout'),
    path('signout/',signout,name='signout'),
    
]






