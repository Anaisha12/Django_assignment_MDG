from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
import requests
from django.urls import reverse
# Create your views here.
def posts(request):
    #pull data from third party rest api
    response = requests.get('http://localhost:8000/api/posts')
    #convert reponse data into json
    post = response.json()
    print(post)
    return render(request, "posts.html",{'posts': post})
    pass
def delete(request, id):
  response = requests.get('http://localhost:8000/api/posts/id')
  response.delete()
  return HttpResponseRedirect(reverse('posts'))
