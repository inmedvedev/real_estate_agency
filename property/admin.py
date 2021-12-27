from django.contrib import admin
from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    raw_id_fields = ["owner"]
    model = Owner.flats_in_property.through


class FlatAdmin(admin.ModelAdmin):
    search_fields = ["town", "address", "owner"]
    readonly_fields = ["created_at"]
    list_display = [
        "address", "price", "new_building", "construction_year",
        "town", "owners_phonenumber", "owners_phonenumber_formatted"
    ]
    list_editable = ["new_building"]
    list_filter = ["new_building", "rooms_number", "has_balcony"]
    raw_id_fields = ["liked_by"]
    inlines = [OwnerInline]


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ["owner", "flat"]
    list_display = ["complaint"]


class OwnerAdmin(admin.ModelAdmin):
    search_fields = ["owner"]
    list_display = ["owner", "owners_phonenumber_formatted"]
    raw_id_fields = ["flats_in_property"]


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
