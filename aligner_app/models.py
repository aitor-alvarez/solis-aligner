# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Transcript(models.Model):
	transcript_name = models.CharField(max_length=250)
	transcript_directory = models.FileField(upload_to='uploads')
	corpus = models.ForeignKey('Corpus',  on_delete=models.CASCADE)
	uploaded_at = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return str(self.transcript_name)

class Corpus(models.Model):
	name = models.CharField(max_length=150)
	language = models.ForeignKey('Language',  on_delete=models.CASCADE)
	description = models.TextField()
	def __str__(self):
		return str(self.name)

class Language(models.Model):
	language = models.CharField(max_length=150)
	acoustic_model = models.ForeignKey('AcousticModel',  on_delete=models.CASCADE)
	def __str__(self):
		return str(self.language)

class AcousticModel(models.Model):
	name = models.CharField(max_length=150)
	model_path = models.FilePathField(path="/Users/cltit-aitor/solis/aligner/acoustic_models")
	dictionary_path = models.FilePathField(path="/Users/cltit-aitor/solis/aligner/dicts")
	def __str__(self):
		return self.name

class Dictionary(models.Model):
	language = models.ForeignKey('Language',  on_delete=models.CASCADE)
	word = models.CharField(max_length=150)
	phoneme = models.CharField(max_length=150)
	def __str__(self):
		return str(self.language)

