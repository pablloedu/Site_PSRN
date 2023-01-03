from django.contrib import admin
from .models import Post, Attachment, Tag, Visualized, Contact


admin.site.register(Post)
admin.site.register(Attachment)
admin.site.register(Tag)
admin.site.register(Visualized)
admin.site.register(Contact)
