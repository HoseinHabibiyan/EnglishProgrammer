from django.contrib import admin

from Programmer.models import Book, Student , WeekPlan , DailyProgram , Day
class DailyProgramInline(admin.TabularInline):
    model = DailyProgram
    extra = 7  # Number of extra forms to display
class WeekPlanModelAdmin(admin.ModelAdmin):
    inlines = [DailyProgramInline]


admin.site.register(Book)
admin.site.register(Student)
admin.site.register(WeekPlan,WeekPlanModelAdmin)
admin.site.register(DailyProgram)
admin.site.register(Day)