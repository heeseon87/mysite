from django.contrib import admin
from semis.models import User_info, Team_info, Dept_info, Level_info, Rank_info, Spend, Cost_type_info, Project_info, Pay_info

admin.site.register(User_info)
admin.site.register(Team_info)
admin.site.register(Dept_info)
admin.site.register(Level_info)
admin.site.register(Rank_info)
admin.site.register(Spend)
admin.site.register(Cost_type_info)
admin.site.register(Project_info)
admin.site.register(Pay_info)