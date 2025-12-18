from django.contrib import admin
from .models import ChaiVariety, ChaiReview, Store, ChaiCertificate


# Register your models here.
class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 2
    
class chaiVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [ChaiReviewInline]
    search_fields = ('name', 'type')
    list_filter = ('type', 'date_added')

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name', 'location')
    filter_horizontal = ('chai_varieties',)
    
class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('certificate_name', 'chai', 'issued_by', 'issue_date', 'valid_until')
    search_fields = ('certificate_name', 'chai__name', 'issued_by')
    
    
admin.site.register(ChaiVariety, chaiVarietyAdmin)
admin.site.register(ChaiReview)
admin.site.register(Store, StoreAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)