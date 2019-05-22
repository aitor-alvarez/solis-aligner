# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import  *

admin.site.register(Transcript)
admin.site.register(Corpus)
admin.site.register(Language)
admin.site.register(AcousticModel)
admin.site.register(Dictionary)