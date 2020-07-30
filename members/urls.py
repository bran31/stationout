from django.urls import path

from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path('out/', views.out, name='out'),
    path('addout/', views.addout, name='addout'),
    path('updateout/<str:pk>/', views.updateout, name='updateout'),
    path('return/', views.returnPage, name='return'),
    path('members/', views.memberPage, name='members'),
    path('addprofile', views.addProfileView, name='add_profile'),
    path('profile/<str:pk>/', views.memberProfileView, name='profile'),
    path('profile/update/<str:pk>/', views.profileupdate, name='profileupdate'),
    path('register/', views.register, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('tour1/', views.tour1, name='tour1'),
    path('tour2/', views.tour2, name='tour2'),
    path('tour3/', views.tour3, name='tour3'),
    path('als/', views.als, name='als'),
    path('bls/', views.bls, name='bls'),
    path('officers/', views.officers, name='officers'),
    path('aplt/', views.aplt, name='aplt'),
    path('bplt/', views.bplt, name='bplt'),
    path('cplt/', views.cplt, name='cplt'),
    path('eplt/', views.eplt, name='eplt'),
    path('fplt/', views.fplt, name='fplt'),
    path('exemptions/', views.aplt, name='exemptions'),
    path('profile_form', views.profileform, name='profile_form'),




    path('reset_password', auth_views.PasswordResetView.as_view(
        template_name='members/password_reset.html'), name='reset_password'),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(
        template_name='members/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='members/password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(
        template_name='members/password_reset_done.html'), name='password_reset_complete'),
    path('change_password/', auth_views.PasswordChangeView.as_view(
        template_name='members/password_change.html', success_url='/'), name='change_password'),

]
