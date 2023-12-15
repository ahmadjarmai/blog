from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.views.decorators.http import require_POST
from .models import Post
from .forms import CommentForm 

def post_list(request) :
 post_list =Post.published.all()
 
 paginator = Paginator(post_list, 3)
 page_number = request.GET.get('page')
 try:
   posts = paginator.page(page_number)
 except PageNotAnInteger:
   posts = paginator.page(1)
 except EmptyPage:
   posts = paginator.page(paginator.num_pages)
   
 return render(request,'blog/list.html',
               {'posts': posts})

def post_detail(request, year,month,day,post):
 post = get_object_or_404(Post,
                          status=Post.Status.PUBLISHED,
                          publish__year=year,
                          publish__month=month,
                          publish__day=day,
                          slug=post)

 return render(request,'blog/detail.html',
               {'post': post})

@require_POST
def comment(request,post_id) :
  post =get_object_or_404(Post, status=Post.Status.PUBLISHED)
  comment =None

  form =CommentForm(data=request.POST)
  if form.is_valid() :
    comment =form.save(commit=False)
    comment.post=post
    comment.save()

  return render(request,'blog/comment.html',
              {'comment':comment})    