from django.contrib import admin
from .models import Film, Director, Genre, Review

class ReviewAdmin(admin.StackedInline):
    model = Review
    extra = 1

class FilmAdmin(admin.ModelAdmin):
    search_fields = ['name', 'text']
    list_filter = ['director', 'genres','is_active']
    list_display = ['name', 'kp_rating', 'is_active', 'created']
    list_editable = ['is_active']
    inlines = [ReviewAdmin]

admin.site.register(Film, FilmAdmin)
admin.site.register(Director)
admin.site.register(Genre)