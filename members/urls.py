from django.urls import path

from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path( "", views.index, name="index"),
    path('out/', views.out , name='out'),
    path('addout/', views.addout, name='addout'),
    path('updateout/<str:pk>/', views.updateout, name='updateout'),
    path('return/', views.returnPage, name='return'),
    path('members/', views.memberPage, name='members'),
    path('profile/<str:pk>/', views.memberProfile, name='profile'),
    path('register/', views.register, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('reset_password', auth_views.PasswordResetView.as_view(template_name='members/password_reset.html'), name='reset_password'),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name='members/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='members/password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name='members/password_reset_done.html'), name='password_reset_complete'),

]
