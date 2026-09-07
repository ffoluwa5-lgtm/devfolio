from django.contrib import admin

from .models import (
    ContactMessage,
    Experience,
    Profile,
    Project,
    Service,
    Skill,
    SocialLink,
)

admin.site.site_header = "Portfolio Admin"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Manage your site content"


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "title", "email")

    def has_add_permission(self, request):
        # Keep this a singleton — edit the one row instead of creating more.
        return not Profile.objects.exists()


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "proficiency", "order")
    list_editable = ("category", "proficiency", "order")
    list_filter = ("category",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "featured", "year", "order")
    list_editable = ("featured", "order")
    prepopulated_fields = {"slug": ("title",)}
    fieldsets = (
        (None, {"fields": ("title", "slug", "summary", "description", "image")}),
        ("Details", {"fields": ("tech_stack", "features", "year")}),
        ("Links", {"fields": ("github_url", "live_url")}),
        ("Display", {"fields": ("featured", "order")}),
    )


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("role", "organisation", "start_date", "end_date", "order")
    list_editable = ("order",)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "order")
    list_editable = ("order",)


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ("label", "platform", "url", "order")
    list_editable = ("platform", "url", "order")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created", "read")
    list_editable = ("read",)
    list_filter = ("read",)
    readonly_fields = ("name", "email", "message", "created")
