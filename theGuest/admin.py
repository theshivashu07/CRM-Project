from django.contrib import admin
from .models import WorksOnLanguage,RecruitDeveloper,RecruitHr,RecruitDeveloperAsProjectManager,AddClientsAndProjectsByMyadmin
from .models import AssignProjectToProjectManagerByMyadmin,AssignProjectToDeveloperByProjectManager
from .models import ActiveAdmin,ReportStatuses,Reports
admin.site.register(WorksOnLanguage)
admin.site.register(RecruitDeveloper)
admin.site.register(RecruitHr)
admin.site.register(RecruitDeveloperAsProjectManager)
admin.site.register(AddClientsAndProjectsByMyadmin)
admin.site.register(AssignProjectToProjectManagerByMyadmin)
admin.site.register(AssignProjectToDeveloperByProjectManager)
admin.site.register(ActiveAdmin)
admin.site.register(ReportStatuses)
admin.site.register(Reports)


