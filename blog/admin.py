from django.contrib import admin
from .models import Poem, Blog, About
# Register your models here.
admin.site.register(Poem)
admin.site.register(Blog)
admin.site.register(About)
