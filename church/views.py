from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from django.http import Http404
from .forms import PostForm

def handle_uploaded_file(f):
    with open(f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def index(request):
	try:
		list = Post.objects.order_by('-pub_date')[:]
	except Post.DoesNotExist:
		raise Http404("Post Not Found")	
	context = {'list': list}
	return render(request, 'index.html', context)

def detail(request, question_id):
    return HttpResponse("You're looking at post %s." % question_id)

def comment(request, question_id):
    return HttpResponse("You're commenting on post %s." % question_id)

def create(request):
    if request.method=='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
        	#instance = Post(file_field=request.FILES['img'])
        	#instance.save()
        	form.save()
        	return HttpResponseRedirect('/')
    else:
        form = PostForm()
    return render(request, 'form.html', {'form': form})
