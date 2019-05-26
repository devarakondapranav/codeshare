from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone


from .models import Code

def home(request):
	a = Code.objects.order_by('-pub_date')
	context = {"codes_list": a}
	return render(request, 'snippets/home.html', context)
	

def viewCode(request, code_id):
	
	a = Code.objects.get(pk=code_id)
	if(True):
		context = {"code_object": a}
		return render(request, 'snippets/codeView.html', context)
	else:
		return None

def newCodeSnippet(request):
	if(request.user.is_authenticated):
		context = {}
		return render(request, 'snippets/newCodeSnippet.html', context)
	else:
		context = {"errorMessage" : "Please login to add new code."}
		return render(request, 'snippets/errorPage.html', context)

def submitNewCodeSnippet(request):
	c = Code(title=request.POST['title'], author = request.POST['username'], code_snippet = request.POST["code_snippet"], pub_date = timezone.now())
	c.save()
	context = {"code_object":c}
	return render(request, 'snippets/success.html', context)

def editCode(request, code_id):

	c = Code.objects.get(pk = code_id)
	if(request.user.is_authenticated and (c.author == request.user.username)):
		context = {"code_object":c}
		return render(request, 'snippets/editCode.html', context)
	else:
		context = {}
		if(request.user.is_authenticated):
			context["errorMessage"] = "You do not have permission to edit this article :( Contact " + c.author + " to make changes to this code."
		else:
			context["errorMessage"] = "Please login	 to add new code."
		return render(request, 'snippets/errorPage.html', context)

def makeChanges(request, code_id):
	c = Code.objects.get(pk=code_id)
	c.title = request.POST["title"]
	c.code_snippet = request.POST["code_snippet"]
	c.save()
	context = {"code_object":c}

	return render(request, 'snippets/changeSuccess.html', context)

def testing(request):

	pass