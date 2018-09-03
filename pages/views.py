from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.
#def homePageView(request):
#	return HttpResponse("Hello Agnes")
class HomePageView(TemplateView):

	template_name='pages/index.html'

class AboutPageView(TemplateView):

	template_name='pages/about.html'