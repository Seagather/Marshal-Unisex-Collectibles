from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'user',
        'title',
        'review',
        'timestamp',
    )


admin.site.register(Review, ReviewAdmin)
