from django.contrib import admin
from .models import Contact 
from .models import Team
from .models import CustomUser,Blog,List_Blog,Form

# Register your models here.
admin.site.register(Contact)
admin.site.register(Team)
admin.site.register(CustomUser)
admin.site.register(Blog)
admin.site.register(List_Blog)
admin.site.register(Form)