from django.contrib import admin
from .models import Equipos, Fixture, Posiciones, Blogs, Avatar, UserProfile


admin.site.register(Equipos)
admin.site.register(Fixture)
admin.site.register(Posiciones)
admin.site.register(Blogs)
admin.site.register(Avatar)
admin.site.register(UserProfile)
