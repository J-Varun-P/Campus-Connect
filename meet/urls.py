from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path("", views.login_view, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_view, name="logout"),
    path("index/", views.index, name="index"),
    path("profile/", views.profile, name="profile"),
    path("add-activity/", views.addactivity, name="add_activity"),
    path("edit-activity/<int:id>", views.editactivity, name="edit_activity"),
    path("index/delete-activity/<int:id>", views.deleteactivity, name="delete_activity"),
    path("my-activities/", views.myactivities, name="my_activities"),
    path("search-activities/<str:name>/<str:title>", views.searchactivities, name="search_activities"),
    #path("search-activities/<str:name>/<str:title>", views.searchactivities, name="search_activities"),
    path("join-activity/<int:id>", views.joinactivity, name="join_activity"),
    path("leave-activity/<int:id>", views.leaveactivity, name="leave_activity"),
    path("activities/<int:id>", views.displayactivity, name="display_activity"),
    path("password_change_done/", views.PasswordChangeDone, name="password_change_done"),
    path('password-change/', auth_views.PasswordChangeView.as_view(template_name="meet/password_change.html"), name="password_change"),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='meet/password_reset.html'),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='meet/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='meet/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='meet/password_reset_complete.html'),name='password_reset_complete'),
]
