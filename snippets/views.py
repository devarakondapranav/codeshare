from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


from .models import Code

def home(request):
	a = Code.objects.order_by('-pub_date')[:16]
	context = {"codes_list": a}
	return render(request, 'snippets/home.html', context)


#manages infinite scrolling
def samplereq(request, start):
	articles = Code.objects.order_by('-pub_date').filter(id__lt = start)[:6]
	temp = []
	for yo in articles:
		temp.append((yo.id, yo.pub_date,yo.author, yo.title, yo.code_snippet))

	return JsonResponse({'articles':temp})


def register(request):
	if(request.user.is_authenticated):
		return HttpResponseRedirect('/snippets')
	else:
		context = {'errors': ''}
		return render(request, 'snippets/register.html', context)

def redirectToHome(request):
	return HttpResponseRedirect('/snippets')

def redirectToCode(request, codeid):
	return HttpResponseRedirect('/snippets/' + str(codeid))


def createuser(request):
	if(request.method == "POST"):
		if(request.user.is_authenticated):
		
			return HttpResponseRedirect('/snippets')
		else:
			email = request.POST["email"]
			username = request.POST["username"]
			if User.objects.filter(username=username).exists():
				return render(request, 'snippets/errorPage.html', {'errorMessage': 'A user with this username is already registered with us'})



			password = request.POST["password"]
			user = User.objects.create_user(username, email, password)
			user.save()


			new_user = authenticate(username=username, password=password)
			login(request, new_user)

			return HttpResponseRedirect('/snippets')
	else:
		return HttpResponse("Po ra kuyya.")

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
	if(request.user.is_authenticated and (c.author == request.user.username)):
		c.title = request.POST["title"]
		c.code_snippet = request.POST["code_snippet"]
		c.save()
		context = {"code_object":c}

		return render(request, 'snippets/changeSuccess.html', context)
	else:
		context = {}
		if(request.user.is_authenticated):
			context["errorMessage"] = "You do not have permission to edit this article :( Contact " + c.author + " to make changes to this code."
		else:
			context["errorMessage"] = "Please login	 to add new code."
		return render(request, 'snippets/errorPage.html', context)

def showProfile(request, username):

	articles = Code.objects.filter(author= username)
	context = {'articles':articles, 'username':username, 'no_of_articles':len(articles)}

	return render(request, 'snippets/showProfile.html', context)

def search(request):

	search_term = request.POST['search_term'].lower()

	all_articles = Code.objects.order_by('-pub_date')
	results = []

	for article in all_articles:
		if((search_term in article.code_snippet.lower()) or (search_term in article.title.lower()) or (search_term in article.author.lower())):
			results.append(article)

	context = {'results':results}

	return render(request, 'snippets/searchResults.html', context)



