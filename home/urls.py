from django.urls import path
from accounts.views import logout_view, change_pass
from .views import list_view, article_detial, my_blog_list, add_new_experience, edit_post


urlpatterns = [
    path('', list_view.as_view(), name='explore'),
    path('articles/<int:pk>', article_detial.as_view(), name='article_details'),
    path('logout/', logout_view, name="logout"),
    path('changepass/', change_pass, name="change_pass"),
    path('add_new_experience/', add_new_experience, name="add_new_experience"),
    path('my_experience/', my_blog_list.as_view(), name="my_experiences"),
    path('edit_post/<int:pk>', edit_post, name="edit_post"),
    path('logout/', logout_view, name="bookmarks"),
    path('logout/', logout_view, name="edit_profile")
]
