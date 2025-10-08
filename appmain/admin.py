from django.contrib import admin
from .models import User, Opinion, ReaderOpinion, Poll, video, bookmark

# Register your models here.
admin.site.register(User)
admin.site.register(Opinion)
admin.site.register(ReaderOpinion)
admin.site.register(Poll)
admin.site.register(video)
admin.site.register(bookmark)