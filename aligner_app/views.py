# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import TranscriptForm
import sys, zipfile, os, os.path
from .models import Corpus, Transcript
import solis.settings as st
import json


def transcript_upload(request):
    if request.method == 'POST':
        form = TranscriptForm(request.POST, request.FILES)
        if form.is_valid():
            corpus = Corpus.objects.get(pk=int(request.POST['corpus']))
            if Transcript.objects.filter(transcript_name=request.POST['transcript_name']).exists():
                 json_data = json.dumps({"Response": "Transcript already exists!"})
                 return HttpResponse(json_data, content_type="application/json")
            else:
                files = request.FILES.getlist('transcript_directory')
                fullpath = str(st.MEDIA_ROOT)+'/uploads/'
                dirname = os.path.dirname(fullpath)
                transdir = os.path.join(dirname, str(request.POST['transcript_name']))
                os.mkdir(transdir)
                for f in files:
                    handle_uploaded_file(f, transdir)
                form.save()
                os.system('MFA/bin/mfa_align'+ transdir +' '+ str(corpus.language.acoustic_model.dictionary_path) + ' '+ str(corpus.language.acoustic_model.model_path) +' '+'transcripts/output/ -v')
            return HttpResponseRedirect('/')
    if request.method == 'GET':
        form = TranscriptForm()
    return render(request, 'transcript.html', {'form': form})


def handle_uploaded_file(filename, path):
    with open(path+'/'+filename.name, 'wb+') as destination:
        for chunk in filename.chunks():
            destination.write(chunk)