from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.views import logout_view
from .views import list_view, article_detial, my_blog_list, add_new_experience, edit_post, delete_post, MyPasswordChangeView, edit_profile


urlpatterns = [
    path('', list_view.as_view(), name='explore'),
    path('articles/<int:pk>', article_detial.as_view(), name='article_details'),
    path('add_new_experience/', add_new_experience.as_view(), name="add_new_experience"),
    path('my_experience/', my_blog_list.as_view(), name="my_experiences"),
    path('edit_post/<int:pk>', edit_post.as_view(), name="edit_post"),
    path('delete_post/<int:pk>', delete_post.as_view(), name="delete_post"),
    path('logout/', logout_view, name="logout"),


    # change password
    path('change_pass/', MyPasswordChangeView.as_view(template_name = 'password_change.html'), name='change_pass'),

    # edit profile
    path('edit_profile/', edit_profile.as_view(), name="edit_profile"),

    
    path('logout/', logout_view, name="bookmarks"),
    
]




