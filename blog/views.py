from django.shortcuts import render,redirect
from .models import BlogPost,Comment,Topic
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    topics = Topic.objects.all()[0:4]
    blogPosts = BlogPost.objects.all()
    context = {'topics':topics,'blogposts':blogPosts}
    return render(request,'blog/home.html',context)

def userProfile(request,pk):
    return render(request,'blog/profile.html')
    
def blog(request,pk):

    blog = BlogPost.objects.get(id=pk)
    room_messages = blog.message_set.all()
    participants = blog.participants.all()

    if request.method == 'POST':
        message = Comment.objects.create(
            user=request.user,
            blog=blog,
            body=request.POST.get('body')
        )
        blog.participants.add(request.user)

        return redirect('room', pk=blog.id)

    context = {'room': blog, 'room_messages': room_messages,
               'participants': participants}
    return render(request, 'base/room.html', context)
    
@login_required(login_url='/login')
def createBlog(request):
    form = RoomForm(request.POST)
    topics = Topic.objects.all()
    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        Room.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description'),
        )
    # if request.method == 'POST':
    #     form = RoomForm(request.POST)
    #     if form.is_valid:
    #         room = form.save(commit=False)
    #         room.host= request.user
    #         form.save()
        return redirect('/')

    context = {'form': form, 'topics': topics}
    return render(request, 'base/room_form.html', context)
