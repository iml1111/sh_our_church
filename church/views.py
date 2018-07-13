from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.http import Http404

def index(request):
	try:
		list = Post.objects.order_by('-pub_date')[:]
	except Post.DoesNotExist:
		raise Http404("Post Not Found")
		
	context = {'list': list}
	return render(request, 'church/index.html', context)

def detail(request, question_id):
    return HttpResponse("You're looking at post %s." % question_id)

def comment(request, question_id):
    return HttpResponse("You're commenting on post %s." % question_id)
