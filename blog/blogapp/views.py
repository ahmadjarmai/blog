from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.views.decorators.http import require_POST
from django.db.models import Count
from taggit.models import Tag
from .models import Post
from .forms import CommentForm

def post_list(request, tag_slug=None) :
 post_list =Post.published.all()
 tag_list =Tag.objects.all()
 tag =None
 if tag_slug  :
    tag =get_object_or_404(Tag, slug=tag_slug)
    post_list =post_list.filter(tags__in=[tag])
 paginator = Paginator(post_list, 6)
 page_number = request.GET.get('page')
 try:
   posts = paginator.page(page_number)
 except PageNotAnInteger:
   posts = paginator.page(1)
 except EmptyPage:
   posts = paginator.page(paginator.num_pages)
   
 return render(request,'blog/list.html',
               {'posts': posts,
               'tag':tag,
               'tag_list':tag_list})

def post_detail(request, year,month,day,post):
 post = get_object_or_404(Post,
                          status=Post.Status.PUBLISHED,
                          publish__year=year,
                          publish__month=month,
                          publish__day=day,
                          slug=post)
 
 comments =post.comment.filter(active=True)
 form =CommentForm()

 post_tags_id =post.tags.value_list('id', flat=True)
 similar_posts =Post.published.filter(tags__in=post_tags_id)\
                                   .exclude(id=post.id)
 similar_posts = similar_posts.annotate(same_tags=Count('tags'))\
 .order_by('-same_tags','-publish')[:4]
 
 return render(request,'blog/detail.html',
               {'post': post,'comments':comments,
                'form':form, 'similar_post':similar_posts})

@require_POST
def comment(request,post_id) :
  post =get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
  comment =None
  form =CommentForm(data=request.POST)
  if form.is_valid() :
    comment =form.save(commit=False)
    comment.post=post
    comment.save()
  return render(request,'blog/comment.html', 
                {'post' : post,'comment':comment,'form':form}) 



