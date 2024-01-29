from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app.models import *

class UserAccountsAdmin(UserAdmin):
    list_display = ['id','username' ,'first_name' ,'last_name' ,'email' ,'department', 'date_joined', 'last_login','is_staff','is_admin','is_active','is_superuser']
    search_fields = ['id','username','first_name','last_name' ,'email' ,'department']
    readonly_fields = ['date_joined','last_login']

    filter_horizontal = []
    list_filter = []
    fieldsets = []
admin.site.register(Users, UserAccountsAdmin)


class EnergyFuelAdmin(admin.ModelAdmin):
    list_display = ['global_id','Tasks','DG_Serial_Number','DG_HMR_Status','DG_HMR_Reading','DG_PIU_Status','Current_DG_PIU_Reading',
    'Diesel_Filling_Done','Date_Of_Diesel_Filling','Diesel_Balance_Before_Filling','Fuel_Qty_Filled',
    'EB_Meter_Status','Current_EB_MTR_KWH','EB_PIU_Meter_Status','Current_EB_PIU_Reading', 'Total_DC_Load', 
    'Total_EB_KWH_Reading_from_all_Channels','Remarks','FT_ID','FT_name','FT_mobile_no','Receipt_No','Card_Number',
    'Vehicle_Plate','Before_Fuel_CM_Photo','After_Fuel_Filling_CM_Photo','DG_Running_HRS','CPH_CPH_Comparison_With_Last_CPH','CPH','EB_KWH'
    ]
    search_fields = ['global_id','Date_Of_Diesel_Filling']

    filter_horizontal = []
    list_filter = []
    fieldsets = []
admin.site.register(EnergyFuel, EnergyFuelAdmin)


class FuelDrawnAdmin(admin.ModelAdmin):
    list_display = [
        'FT_ID','FT_name','FT_mobile_no','Cluster_Name','Fuel_Drawn_Date','Card_No','City_Township_Fuel_Station',
        'Customer','Fuel_Station_Name','Diesel_Purchased_Qty','Diesel_Per_Ltr_Cost_Rs','Total_Diesel_Cost_Rs',
        'Receipt_No','Receipt_Image_Upload','Vehicle_Plate','Remarks'
    ]
    search_fields = ['FT_ID','FT_name','FT_mobile_no','Cluster_Name','Fuel_Drawn_Date','Card_No','Vehicle_Plate']

    filter_horizontal = []
    list_filter = []
    fieldsets = []
admin.site.register(FuelDrawn, FuelDrawnAdmin)


class SiteFixedAdmin(admin.ModelAdmin):
    list_display = [
        'global_id','site_name','site_address','cluster','CE','site_tenancy','DG_NON_DG','DG_capacity_kva',
        'EB_status','card_number','last_month_approved_CPH'
    ]
    search_fields = ['global_id','site_name','site_address','cluster','CE','site_tenancy','DG_NON_DG','DG_capacity_kva',
        'EB_status','card_number','last_month_approved_CPH']

    filter_horizontal = []
    list_filter = []
    fieldsets = []
admin.site.register(SiteFixed, SiteFixedAdmin)
