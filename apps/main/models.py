# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models

# Create your models here.
class ActorManager(models.Manager):
	def validate(self, data):
		errors = []
		if data["first_name"] == "":
			errors.append("first_name cannot be empty")
		if data["last_name"] == "":
			errors.append("last_name cannot be empty")
		if data["dob"] == "":
			errors.append("dob cannot be empty")
		else:
			dob = datetime.datetime.strptime(data["dob"], "%Y-%m-%d")
			today = datetime.datetime.today()
			if dob > today:
				errors.append("date cannot be in the future")
		return errors
class Actor(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	dob = models.DateField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = ActorManager()

class Movie(models.Model):
	title = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Featured(models.Model):
	actor = models.ForeignKey(Actor, related_name="acted_in")
	movie = models.ForeignKey(Movie, related_name="featuring")