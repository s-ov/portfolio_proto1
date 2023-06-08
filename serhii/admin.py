from django.contrib import admin
from .models import Home, About, Category, Profile, Skills, Portfolio

admin.site.register(Home)


class ProfileInline(admin.TabularInline):
    """About"""
    model = Profile
    extra = 1


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [
        ProfileInline,
    ]


class SkillsInline(admin.TabularInline):
    """Skills"""
    model = Skills
    extra = 4


# Portfolio
admin.site.register(Portfolio)
admin.site.register(Category)
admin.site.register(Skills)

