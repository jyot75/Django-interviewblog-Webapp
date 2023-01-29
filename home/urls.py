from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.views import logout_view, change_pass
from .views import list_view, article_detial, my_blog_list, add_new_experience, edit_post, delete_post


urlpatterns = [
    path('', list_view.as_view(), name='explore'),
    path('articles/<int:pk>', article_detial.as_view(), name='article_details'),
    path('add_new_experience/', add_new_experience.as_view(), name="add_new_experience"),
    path('my_experience/', my_blog_list.as_view(), name="my_experiences"),
    path('edit_post/<int:pk>', edit_post.as_view(), name="edit_post"),
    path('delete_post/<int:pk>', delete_post.as_view(), name="delete_post"),
    path('logout/', logout_view, name="logout"),


    # reset password with email auth
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),



    path('changepass/', change_pass, name="change_pass"),
    path('logout/', logout_view, name="bookmarks"),
    path('logout/', logout_view, name="edit_profile")
]




