from django.contrib import admin
from score_prediction.models import team_data,venue_data,master_data

# Register your models here.
admin.site.register(team_data)
admin.site.register(venue_data)
admin.site.register(master_data)
