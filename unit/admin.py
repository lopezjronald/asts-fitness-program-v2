from django.contrib import admin
from .models import Airman, Profile, Naughty, PhysicalTrainingLeader, UnitFitnessProgramManager

admin.site.site_header = '349 ASTS FITNESS PROGRAM'
admin.site.site_title = '349 ASTS Fitness Program'
admin.site.index_title = 'UFPM ADMIN TEAM'


class ProfileInline(admin.TabularInline):
    model = Profile
    show_change_link = True

    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 0
        else:
            return 1


class NaughtyInline(admin.TabularInline):
    model = Naughty
    show_change_link = True

    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 0
        else:
            return 1


class PhysicalTrainingLeaderInline(admin.TabularInline):
    model = PhysicalTrainingLeader
    show_change_link = True

    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 0
        else:
            return 1


class UnitFitnessProgramManagerInline(admin.TabularInline):
    model = UnitFitnessProgramManager
    show_change_link = True

    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 0
        else:
            return 1


# Register your models here.
# admin.site.register(Airman)
@admin.register(Airman)
class AirmanAdmin(admin.ModelAdmin):
    inlines = [
        ProfileInline,
        NaughtyInline,
        PhysicalTrainingLeaderInline,
        UnitFitnessProgramManagerInline,
    ]
    # fields = ('rank',
    #           ('first_name', 'middle_initial', 'last_name'), ('ssn', 'airman_slug'),
    #           ('fitness_level', 'test_date'),
    #           ('ptl', 'ufpm'),
    #           'active_status')

    save_on_top = True

    fieldsets = (
        ('AIRMAN INFORMATION', {
            'fields': ('rank', ('first_name', 'middle_initial', 'last_name'), 'ssn')
        }),
        ('FITNESS INFORMATION', {
            'fields': (('fitness_level', 'test_date'),),
            'description': 'Fitness Level & Test Date',
            'classes': ('wide',)
        }),
        ('FITNESS TEAM', {
            'fields': (('ptl', 'ufpm'),),
            'classes': ('collapse',)
        }),
        ('EXTRA', {
            'fields': ('airman_slug',),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('airman_id',)
    list_display = (
        'airman_id', 'ssn', 'rank', 'first_name', 'middle_initial', 'last_name', 'test_date', 'fitness_level',
        'active_status',)
    list_display_links = ('airman_id',)
    list_editable = (
        'ssn', 'rank', 'test_date', 'fitness_level', 'active_status',)
    list_filter = ('fitness_level',)
    search_fields = ('first_name', 'last_name', 'ssn')
    prepopulated_fields = {'airman_slug': ('ssn',)}
    date_hierarchy = 'test_date'
    ordering = ('last_name', 'first_name')
    actions_on_bottom = True
    actions_on_top = True


# @admin.register(Physical_Training_Leader)
@admin.register(PhysicalTrainingLeader)
class PhysicalTrainingLeaderAdmin(admin.ModelAdmin):
    inlines = [
        UnitFitnessProgramManagerInline,
    ]
    list_display = ('airman_id', 'ptl_certification_date', 'ptl_expiration_date', 'cpr_expiration_date')
    list_editable = ('ptl_certification_date', 'ptl_expiration_date', 'cpr_expiration_date',)
    list_filter = ('ptl_expiration_date', 'cpr_expiration_date')
    date_hierarchy = 'ptl_expiration_date'
    ordering = ('-ptl_expiration_date', '-cpr_expiration_date')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('airman_id', 'profile_start_date', 'profile_expiration_date',)
    list_editable = ('profile_start_date', 'profile_expiration_date',)
    list_filter = ('profile_expiration_date',)
    date_hierarchy = 'profile_expiration_date'
    ordering = ('-profile_expiration_date',)


@admin.register(Naughty)
class NaughtyAdmin(admin.ModelAdmin):
    list_display = ('airman_id', 'failure_date', 'be_well_completion_date', 'status_level')
    list_editable = ('failure_date', 'be_well_completion_date', 'status_level',)
    list_filter = ('failure_date',)
    search_fields = ('failure_date',)
    date_hierarchy = 'failure_date'
    ordering = ('-failure_date',)


@admin.register(UnitFitnessProgramManager)
class UnitFitnessProgramManagerAdmin(admin.ModelAdmin):
    list_display = ('airman_id', 'ptl_id', 'ufpm_certification_date', 'ufpm_expiration_date')
    list_editable = ('ptl_id', 'ufpm_certification_date', 'ufpm_expiration_date',)
    list_filter = ('ufpm_expiration_date',)
    date_hierarchy = 'ufpm_expiration_date'
    ordering = ('-ufpm_expiration_date',)
