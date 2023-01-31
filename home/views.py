from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, HttpResponseRedirect
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
# from django_filters.rest_framework import DjangoFilterBackend
# from django_filters.rest_framework import generics

# Create your views here.

# explore page
class list_view(LoginRequiredMixin, ListView):
    model = BlogPost
    template_name = 'home.html'
    context_object_name = 'obj_list'
    ordering = ['-id']
    # filter_backends = [DjangoFilterBackend]
    # search_fields = ['^title']

    def get_queryset(self):
        search = self.request.GET.get('search', '').lower()
        searched = []
        for i in BlogPost.objects.all():
            if search in i.title.lower():
                searched.insert(0,i)
        return searched



# details of explore page
class article_detial(LoginRequiredMixin, DetailView):
    model = BlogPost
    template_name = 'articles.html'
    context_object_name = 'art'

    def get_context_data(self, *args, **kwargs):
        context =  super(article_detial, self).get_context_data(**kwargs)
        stuff = get_object_or_404(BlogPost, id=self.kwargs['pk'])
        value = False
        if stuff.bookmark.filter(id=self.request.user.id).exists():
            value = True
        context['value'] = value
        return context



# my experiences page
class my_blog_list(LoginRequiredMixin, ListView):
    model = BlogPost
    template_name = 'my_experience.html'
    context_object_name = 'my_obj_list'
        
    def get_queryset(self):
        current_user = self.request.user
        only_my =  BlogPost.objects.filter(author=current_user).order_by('-id')
        

        # SEARCH FUNCTIONLITY in my experience
        search = self.request.GET.get('search', '').lower()
        searched = []
        for i in only_my:
            if search in i.title.lower():
                searched.append(i)
        return searched





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







# add or remove bookmark
@login_required
def bookmark_toggle(request, pk):
    post = get_object_or_404(BlogPost, id=pk)
    if post.bookmark.filter(id=request.user.id).exists():
        post.bookmark.remove(request.user)
    else:
        post.bookmark.add(request.user)  
    return HttpResponseRedirect(request.META['HTTP_REFERER'])





# list bookmarked post
@login_required
def bookmark_list(request):
    only_bked = []
    for i in BlogPost.objects.all():
        if i.bookmark.filter(id=request.user.id).exists():
            only_bked.insert(0,i)

    # SEARCH FUNCTIONLITY in bookmark
    search = request.GET.get('search', '').lower()
    searched = []
    for i in only_bked:
        if search in i.title.lower():
            searched.append(i)

    return render(request, 'bookmark.html', {'obj_list': searched})