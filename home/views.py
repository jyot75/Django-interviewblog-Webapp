from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import CreateView,ListView,DetailView, DeleteView
from .models import BlogPost
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

# explore page
class list_view(LoginRequiredMixin, ListView):
    model = BlogPost
    template_name = 'home.html'
    context_object_name = 'obj_list'


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
        return BlogPost.objects.filter(author=current_user)



# class delete_post(DeleteView):
#     model = BlogPost
#     success_url = 'home/'



@login_required
def add_new_experience(request):
    if request.method == 'POST':
        title = request.POST['title']
        if BlogPost.objects.filter(title=title).exists():
            messages.error(request, 'This title is already taken by other Blog post.')
            return render(request, 'add_new_experience.html')
        
        company = request.POST['company']
        job_month = request.POST['job_month'] + "-01"
        job_offer = request.POST['job_offer']
        job_profile = request.POST['job_profile']
        body_content = request.POST['body_content']
        
        current_user = request.user
        BlogPost.objects.create(author=current_user,company=company, month_year=job_month, job_offer=job_offer, profile=job_profile, title=title, body=body_content)
        messages.success(request, 'Your Blog posted successfully !!')
        return redirect('/home/')
    return render(request, 'add_new_experience.html')



# for edit post
@login_required
def edit_post(request):
    ed_post = BlogPost.objects.get(id=2)
    old_title = ed_post.title
    old_company = ed_post.company
    old_job_month = ed_post.month_year | "F Y"
    old_job_offer = ed_post.job_offer
    old_job_profile = ed_post.profile
    old_body_content = ed_post.body

    if request.method == 'POST':
        title = request.POST['title']
        if BlogPost.objects.filter(title=title).exists():
            messages.error(request, 'This title is already taken by other Blog post.')
            return render(request, 'edit_post.html')
        
        company = request.POST['company']
        job_month = request.POST['job_month'] + "-01"
        job_offer = request.POST['job_offer']
        job_profile = request.POST['job_profile']
        body_content = request.POST['body_content']
        
        current_user = request.user
        BlogPost.objects.create(author=current_user,company=company, month_year=job_month, job_offer=job_offer, profile=job_profile, title=title, body=body_content)
        messages.success(request, 'Your Blog posted successfully !!')
        return redirect('/home/')
    return render(request, 'edit_post.html', {'title': old_title, 'company': old_company, 'job_month': old_job_month, 'job_offer': old_job_offer, 'job_profile': old_job_profile, 'body_content': old_body_content})

