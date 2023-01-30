from django.shortcuts import render,HttpResponse,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import CreateView,ListView,DetailView, DeleteView, UpdateView
from .models import BlogPost
from accounts.models import NewUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .forms import BlogForm, ChangingPassword, EditProfileForm
from datetime import datetime
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView


# Create your views here.

# explore page
class list_view(LoginRequiredMixin, ListView):
    model = BlogPost
    template_name = 'home.html'
    context_object_name = 'obj_list'
    ordering = ['-id']

# details of explore page
class article_detial(LoginRequiredMixin, DetailView):
    model = BlogPost
    template_name = 'articles.html'
    context_object_name = 'art'


# my experiences page
class my_blog_list(LoginRequiredMixin, ListView):
    model = BlogPost
    template_name = 'my_experience.html'
    context_object_name = 'my_obj_list'
        
    def get_queryset(self):
        current_user = self.request.user
        return BlogPost.objects.filter(author=current_user).order_by('-id')


# for adding new post
class add_new_experience(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = BlogPost
    form_class = BlogForm
    template_name = 'add_new_experience.html'
    success_message = 'Your Blog Posted Successfully !!!'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)






# for delete post
class delete_post(LoginRequiredMixin, DeleteView):
    model = BlogPost
    success_url = reverse_lazy('my_experiences')



# for edit post
class edit_post(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = BlogPost
    template_name = 'edit_post.html'
    form_class = BlogForm
    success_message = 'Your Blog Edited Successfully !!!'
    success_url = reverse_lazy('my_experiences')
    context_object_name = 'post'

    def form_valid(self, form):
        form.instance.pub_date = datetime.now()
        return super().form_valid(form)



# password change
class MyPasswordChangeView(LoginRequiredMixin, SuccessMessageMixin, PasswordChangeView):
    form_class = ChangingPassword
    success_message = 'Password Changed Successfully !!!'
    success_url = reverse_lazy('explore')



# edit profile
class edit_profile(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'edit_profile.html'
    form_class = EditProfileForm
    success_message = 'Profile Changes Saved Successfully !!!'
    success_url = reverse_lazy('explore')

    def get_object(self):
        return self.request.user





