from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import CreateView,ListView,DetailView
from .models import BlogPost
from django.utils import timezone

# Create your views here.

# @login_required
class list_view(ListView):
    model = BlogPost
    template_name = 'home.html'
    context_object_name = 'obj_list'


class article_detial(DetailView):
    model = BlogPost
    template_name = 'articles.html'
    context_object_name = 'art'



class my_blog_list(ListView):
    model = BlogPost
    template_name = 'my_experience.html'
    context_object_name = 'my_obj_list'
        
    def get_queryset(request):
        return BlogPost.objects.filter(author=request.user).order_by('creation_date')



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

