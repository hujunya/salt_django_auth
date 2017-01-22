from django.contrib import admin

from .models import SaltExternalAuthModel


class SaltExternalAuthModelAdmin(admin.ModelAdmin):
    list_display = ('user_fk', 'minion_or_fn_matcher', 'minion_fn')
    search_fields = ('user_fk__username', 'minion_or_fn_matcher', 'minion_fn')

admin.site.register(SaltExternalAuthModel, SaltExternalAuthModelAdmin)
