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
    list_display = ['id','global_id','Tasks','DG_Serial_Number','DG_HMR_Status','DG_HMR_Reading','DG_PIU_Status','Current_DG_PIU_Reading',
    'Diesel_Filling_Done','Date_Of_Diesel_Filling','Diesel_Balance_Before_Filling','Fuel_Qty_Filled',
    'EB_Meter_Status','Current_EB_MTR_KWH','EB_PIU_Meter_Status','Current_EB_PIU_Reading', 'Total_DC_Load', 
    'Total_EB_KWH_Reading_from_all_Channels','Remarks','FT_ID','FT_name','FT_mobile_no','Receipt_No','Card_Number',
    'Vehicle_Plate','EB_Cumulative_KWH_Image','EB_Running_Hours_Cumulative_Image','DG_Running_Hours_Reading_Image',
    'DG_Running_Hours_as_per_piu_Reading_Image','Diesel_Bill_Number_Image','DG_Running_HRS','CPH_CPH_Comparison_With_Last_CPH',
    'CPH_as_par_HMR','CPH_as_par_PIU','EB_KWH']
    search_fields = ['id','global_id','Date_Of_Diesel_Filling']

    filter_horizontal = []
    list_filter = []
    fieldsets = []
admin.site.register(EnergyFuel, EnergyFuelAdmin)


class EnergyDieselFillingAdmin(admin.ModelAdmin):
    list_display = [
        'file','File_id','Global_ID','Circle','Site_Name','Cluster','Region','User_Name','Assign_Date','Status','Previous_Reading_Date_Time',
        'Current_Reading_Date_Time','Previous_EB_Cumulative_KWH_As_Per_EB_Meter','Current_EB_Cumulative_KWH_As_Per_EB_Meter',
        'Previous_EB_Running_Hours_Cumulative_Available_Not_Available','Current_EB_Running_Hours_Cumulative_Available_Not_Available',
        'Previous_EB_Running_Hours_Cumulative_As_per_PIU_I2PMS_AMF','Current_EB_Running_Hours_Cumulative_As_per_PIU_I2PMS_AMF',
        'Previous_Type_of_DG_Static_Mobile','Current_Type_of_DG_Static_Mobile','Previous_DG_Running_Hours_Reading_As_Per_HMR','Current_DG_Running_Hours_Reading_As_Per_HMR',
        'Previous_DG_Running_Hours_Reading_As_Per_PIU_I2PMS_AMF','Current_DG_Running_Hours_Reading_As_Per_PIU_I2PMS_AMF',
        'Previous_Opening_Diesel_stock_Before_Filling','Current_Opening_Diesel_stock_Before_Filling','Previous_Filled_Ltrs',
        'Current_Filled_Ltrs','Previous_Diesel_Bill_Number','Current_Diesel_Bill_Number','Previous_Remarks_If_any','Current_Remarks_If_any',
        'No_of_days_since_previous_filling','Calculated_CPH_HMR','Calculated_CPH_As_per_PIU_I2PMS_AMF','Calculated_DG_HR_HMR',
        'Calculated_DG_HR_As_per_PIU_I2PMS_AMF','Calculated_EB_KWH_As_per_Meter','Calculated_EB_HR_As_per_PIU_I2PMS_AMF','Deviation'
    ]
    search_fields = ['File_id','Global_ID']

    filter_horizontal = []
    list_filter = []
    fieldsets = []
admin.site.register(EnergyDieelFilling, EnergyDieselFillingAdmin)


class FuelDrawnAdmin(admin.ModelAdmin):
    list_display = [
        'id','FT_ID','FT_name','FT_mobile_no','Cluster_Name','Fuel_Drawn_Date','Card_No','City_Township_Fuel_Station',
        'Customer','Fuel_Station_Name','Diesel_Purchased_Qty','Diesel_Per_Ltr_Cost_Rs','Total_Diesel_Cost_Rs',
        'Receipt_No','Receipt_Image_Upload','Vehicle_Plate','Remarks'
    ]
    search_fields = ['id','FT_ID','FT_name','FT_mobile_no','Cluster_Name','Fuel_Drawn_Date','Card_No','Vehicle_Plate']

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




