# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import *

# Create your views here.
def index(req):
	return HttpResponse("finish setup")

def actor_index(req):
	context = {
		"actors":Actor.objects.all()
	}
	return render(req, "main/actors/index.html", context)

def actor_create(req):
	print req.POST
	errors = Actor.objects.validate(req.POST)
	if len(errors) > 0:
		pass
	else:
		Actor.objects.create(first_name=req.POST["first_name"], last_name=req.POST["last_name"], dob=req.POST["dob"])
	print Actor.objects.all()
	return redirect("/actors")

def actor_show(req, actor_id):
	print actor_id
	context = {
		"actor":Actor.objects.get(id=actor_id),
		"features":Featured.objects.filter(actor=Actor.objects.get(id=actor_id)),
		"movies":Movie.objects.all()
	}
	return render(req, "main/actors/show.html", context)

def movie_index(req):
	context = {
		"movies":Movie.objects.all()
	}
	return render(req, "main/movies/index.html", context)

def movie_create(req):
	Movie.objects.create(title=req.POST["title"])
	return redirect("/movies")

def featured_create(req, actor_id):
	Featured.objects.create(actor=Actor.objects.get(id=actor_id), movie=Movie.objects.get(id=req.POST["movie"]))
	return redirect("/actors")


