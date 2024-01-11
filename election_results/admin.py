from django.contrib import admin

from election_results.models import LGA, Ward, AnnouncedPuResult, PollingUnit, State

# Register your models here.
admin.site.register(State)
admin.site.register(LGA)
admin.site.register(Ward)
admin.site.register(PollingUnit)
admin.site.register(AnnouncedPuResult)
