from django.contrib import admin

from Programmer.models import Refrence, Student , WeekPlan , DailyProgram , Day , Track , RefrenceSeri
class DailyProgramInline(admin.TabularInline):
    model = DailyProgram
    extra = 7  # Number of extra forms to display
class WeekPlanModelAdmin(admin.ModelAdmin):
    inlines = [DailyProgramInline]


class TracksInline(admin.TabularInline):
    model = Track
    extra = 10  # Number of extra forms to display
class RefrenceModelAdmin(admin.ModelAdmin):
    inlines = [TracksInline]
    filter_horizontal = ['related_references']

admin.site.register(Refrence,RefrenceModelAdmin)
admin.site.register(RefrenceSeri)
admin.site.register(Student)
admin.site.register(WeekPlan,WeekPlanModelAdmin)
admin.site.register(DailyProgram)
admin.site.register(Day)