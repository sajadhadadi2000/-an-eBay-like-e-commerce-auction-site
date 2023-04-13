from django.contrib import admin
from .models import User, List, Bid, Coments, Watchlist
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(List)
admin.site.register(Bid)
admin.site.register(Coments)
admin.site.register(Watchlist)