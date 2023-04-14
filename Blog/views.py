from django.shortcuts import render, HttpResponse, redirect
from Blog.models import Post, BlogComment
from django.contrib import messages
from Blog.templatetags import extras
from django.contrib.auth.models import User
from django.contrib.auth import  authenticate
# Create your views here.

# superuse name - coder ,pass - man9 , email - rapx


def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'blog/blogHome.html', context)
  
def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post,parent=None)
    replies= BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)
        
    context = {'post': post, 'comments': comments,'user':request.user,'replyDict':replyDict}
    return render(request, 'blog/blogPost.html', context)

def postComment(request):
    if request.method == "POST":
        comment = request.POST.get('vichar')
        user = request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.get(sno=postSno)
        parentSno = request.POST.get('parentSno')

        
        if parentSno=='':
            comment = BlogComment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent = BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(comment=comment, user=user, post=post,parent=parent)
        # print(comment, user, postSno, post)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")

    return redirect(f"/blog/{post.slug}")
    # return redirect(f"/blog/{post.slug}")

def search(request):
    query = request.GET['query']
    if len(query) > 77:
        allPosts = []
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)

    if allPosts.count() == 0:
        messages.warning(request, 'No search results found ')

    params = {'allPosts': allPosts, 'query': query}
    return render(request, 'home/search.html', params)