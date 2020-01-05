from django.contrib import admin
from django.http import HttpResponse
import csv

from .models import * 
from django.contrib.admin import SimpleListFilter

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('last_Name', 'first_Name', 'category', 'phone', 'email', 'date_added',)

    fieldsets = (
        ('Competitor Info', {'fields': (('last_Name','first_Name'),('date_of_Birth','sex'),('category','proposedweightclass'),('waiver','has_paid'))}),
        ('Contact Info', {'fields': ('address', ('city','state','zip_code'), ('phone','email'))}),
        ('Other Judo Info', {'fields': (('judo_club','rank','us_citizen'), ('judo_card','card_number'))}),
    )

    search_fields = ('last_Name', 'first_Name', 'category')

    list_filter = ('has_paid','waiver','is_test','category',)

    ordering = ('last_Name',)

    readonly_fields = ('date_added',)

    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = ['last_Name', 'first_Name', 'category', 'phone', 'email', 'date_added']
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"

# Filter for those who haven't weighed in
class NoWeightFilter(SimpleListFilter):
    title = 'No Weigh In'
    parameter_name = 'actual_weight'

    def lookups(self, request, model_admin):
        return [('No Weight','No Weight')]

    def queryset(self, request, queryset):
        if self.value() == 'No Weight':
            return queryset.filter(actual_weight=None)


@admin.register(JuniorMale)
class JuniorMaleAdmin(admin.ModelAdmin):
    list_display = ('person','weight_class','actual_weight',)
    search_fields = ('person__last_Name', 'person__first_Name')
    ordering = ('person__last_Name',)
    list_filter = (NoWeightFilter,'age_group', 'person__category','person__has_paid','weight_class')


@admin.register(JuniorFemale)
class JuniorFemaleAdmin(admin.ModelAdmin):
    list_display = ('person','weight_class','actual_weight', )
    search_fields = ('person__last_Name', 'person__first_Name')
    ordering = ('person__last_Name',)
    list_filter = (NoWeightFilter,'age_group', 'person__category','person__has_paid','weight_class')


@admin.register(SeniorMale)
class SeniorMaleAdmin(admin.ModelAdmin):
    list_display = ('person','weight','actual_weight',)
    search_fields = ('person__last_Name', 'person__first_Name')
    ordering = ('person__last_Name',)
    list_filter = (NoWeightFilter,'person__category','person__has_paid','weight')


@admin.register(SeniorFemale)
class SeniorFemaleAdmin(admin.ModelAdmin):
    list_display = ('person','weight','actual_weight',)
    search_fields = ('person__last_Name', 'person__first_Name')
    ordering = ('person__last_Name',)
    list_filter = (NoWeightFilter,'person__category','person__has_paid','weight')


@admin.register(Veteran)
class VeteranAdmin(admin.ModelAdmin):
    list_display = ('person','weight','actual_weight',)
    search_fields = ('person__last_Name', 'person__first_Name')
    ordering = ('person__last_Name',)
    list_filter = (NoWeightFilter,'person__category','person__has_paid','weight')


@admin.register(NoviceMale)
class NoviceMaleAdmin(admin.ModelAdmin):
    list_display = ('person','weight','actual_weight','category')
    search_fields = ('person__last_Name', 'person__first_Name')
    ordering = ('person__last_Name',)
    list_filter = (NoWeightFilter,'person__category','person__has_paid','weight','category')


@admin.register(NoviceFemale)
class NoviceFemaleAdmin(admin.ModelAdmin):
    list_display = ('person','weight','actual_weight',)
    search_fields = ('person__last_Name', 'person__first_Name')
    ordering = ('person__last_Name',)
    list_filter = (NoWeightFilter,'person__category','person__has_paid','weight')
