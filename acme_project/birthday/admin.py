from django.contrib import admin

from birthday.models import Birthday, Congratulation, Tag


admin.site.register(Birthday)
admin.site.register(Congratulation)
admin.site.register(Tag)
