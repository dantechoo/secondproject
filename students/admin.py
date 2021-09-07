from django.contrib import admin
from students.models import stud_info

# Register your models here.
# 1st type ,havent add to modelAdmin type
# admin.site.register(stud_info)

# 2nd type : is add modeladmin type and define the display data
#class studentAdmin(admin.ModelAdmin):
#    list_display = ('id','cName','cSex', 'cDob', 'cEmail', 'cPhone', 'cAddr')
#admin.site.register(stud_info, studentAdmin)

# 3rd type : is add modeladmin type and search & view model
class studentAdmin2(admin.ModelAdmin):
    list_display = ('id','cName','cSex', 'cDob', 'cEmail', 'cPhone', 'cAddr')
    list_filter = ('cName', 'cSex')
    search_fields = ('cName',)
    ordering = ('id',)
admin.site.register(stud_info,studentAdmin2)