from django.contrib import admin
from bets.models import BlogabetBets, BlogabetAuthor, Dyscipline, ZawodTyperBets, ZawodTyperAuthor

admin.site.register(BlogabetBets)
admin.site.register(BlogabetAuthor)
admin.site.register(Dyscipline)
admin.site.register(ZawodTyperBets)
admin.site.register(ZawodTyperAuthor)