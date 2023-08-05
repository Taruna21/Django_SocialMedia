from django.contrib import admin
from .models import Profile , Post , LikePost , FollowersCount


admin.site.register(Profile)
# Register your models here.
admin.site.register(Post)


# Register your models here.
admin.site.register(LikePost)
admin.site.register(FollowersCount)