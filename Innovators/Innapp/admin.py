from django.contrib import admin
from .models import President, Bloodonate, Members, Secretary
# Register your models here.
admin.site.register(President)
admin.site.register(Secretary)
admin.site.register(Members)
admin.site.register(Bloodonate)