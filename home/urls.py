from django.urls import path
from accounts.views import logout_view, change_pass
from .views import list_view, article_detial, add_new_experience


urlpatterns = [
    path('', list_view.as_view(), name='explore'),
    path('articles/<int:pk>', article_detial.as_view(), name='article_details'),
    path('logout/', logout_view, name="logout"),
    path('changepass/', change_pass, name="change_pass"),
    path('add_new_experience/', add_new_experience, name="add_new_experience"),
    path('logout/', logout_view, name="my_experiences"),
    path('logout/', logout_view, name="bookmarks"),
    path('logout/', logout_view, name="edit_profile")
]
