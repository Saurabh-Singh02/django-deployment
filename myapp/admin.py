from django.contrib import admin
from .models import Profile, Skill, Project, Experience, Education, ContactMessage

# Profile Admin
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'location')
    search_fields = ('name', 'email', 'location')

# Skill Admin
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'proficiency', 'profile')
    list_filter = ('profile',)
    search_fields = ('name',)

# Project Admin
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'profile')
    list_filter = ('created_at', 'profile')
    search_fields = ('title', 'description')
    date_hierarchy = 'created_at'

# Experience Admin
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('role', 'company_name', 'start_date', 'end_date', 'profile')
    list_filter = ('company_name', 'profile')
    search_fields = ('role', 'company_name')
    date_hierarchy = 'start_date'

# Education Admin
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution_name', 'start_date', 'end_date', 'profile')
    list_filter = ('institution_name', 'profile')
    search_fields = ('degree', 'institution_name')
    date_hierarchy = 'start_date'

# Contact Message Admin
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'sent_at')
    list_filter = ('sent_at',)
    search_fields = ('name', 'email', 'message')
    date_hierarchy = 'sent_at'
