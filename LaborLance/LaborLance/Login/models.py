from django.db import models
from LaborLance.InitialMigrations.models import CityState
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class JobSeeker(User):
   # user_id=models.ForeignKey(User,related_name='jobseeker_user_id')
   name = models.CharField(max_length=200,null=True)
   location = models.ManyToManyField(CityState)
   skills = models.CharField(max_length=500,null=True)
   notify = models.BooleanField(null=False)
   minpay=models.FloatField(validators=[MinValueValidator(0.99)],default=0.99)
   maxpay=models.FloatField(validators=[MinValueValidator(0.99)],default=0.99)
   CHOICES = [('hourly', 'Hourly'),
              ('monthly', 'Monthly')]
   paytype=models.CharField(
        choices=CHOICES,
        default='hourly', max_length=2)
   class Meta:
      db_table = "jobseeker"



class Business(User):
   # user_id=models.ForeignKey(User,related_name='business_user_id')
   name = models.CharField(max_length=200,null=False)
   locations = models.ForeignKey(CityState,related_name='locations')
   notify = models.BooleanField(null=False)
   contactname=models.CharField(max_length=200,null=False)
   employee_strength=models.IntegerField()
   industry_type=models.CharField(max_length=200)
   class Meta:
      db_table = "business"



#
#
# cookie: ab.storage.deviceId.e5ae6cfc-ff98-4431-8e2f-90df080380aa=%7B%22g%22%3A%22afc41374-8a59-b587-820d-b34ff170e7f2%22%2C%22c%22%3A1587969309369%2C%22l%22%3A1587969309369%7D; __cfduid=daa87a253305ec19694c894704a08c7521587969314;
# pm_sesh_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhaWQiOiJkOWI3M2NhYy05YzY5LTRkY2ItOGMwNS1hYThmMDcwZTIxNjciLCJjZmR1aWQiOm51bGwsImNzcmYiOm51bGwsImRpZCI6ImIyOWIzMWYxLTc5MzYtNDg3NC1hNTAyLWE1MGE4OGM2N2UyNiIsImlhdCI6MTU4Nzk2OTMxNCwic2Vzc2lvbiI6bnVsbCwic3J2IjoicHJvZCIsInVzZXIiOnt9fQ.KjpuyaIvMUfo-6Qpwyx1O6ENbkqaiVtGrLHqpi6GcJQ;
# bfe_session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhaWQiOiJkOWI3M2NhYy05YzY5LTRkY2ItOGMwNS1hYThmMDcwZTIxNjciLCJkaWQiOiJiMjliMzFmMS03OTM2LTQ4NzQtYTUwMi1hNTBhODhjNjdlMjYiLCJpYXQiOjE1ODc5NjkzMTQsInNydiI6InByb2QiLCJ1dG0iOnsic291cmNlIjoiVW5hdHRyaWJ1dGVkIn19.iy58EjevqGlp8506mAMrjNMtoszXaB-gw7kBEk-Hm0Y; _gcl_au=1.1.1369511717.1587969316;
# _uetsid=_uet27fa339d-9094-95e0-4c75-1d1d1f037410; rdt_uuid=82f3ea23-52b7-437c-8f50-c2eb1e127a37; _tq_id.TV-36450936-1.7ed0=264d2471cc01043f.1587969317.0.1587969317..; IR_gbd=postmates.com; IR_8626=1587969317035%7C0%7C1587969317035%7C%7C; __stripe_mid=c0185aee-4060-4cf5-a8a4-edb547fafb83; __stripe_sid=a2f42e3b-da65-4cac-9527-b5a7b196af48; _ga=GA1.2.1557690839.1587969318; _gid=GA1.2.2048328101.1587969318; _scid=6d1f2b3a-865a-4668-ace8-42b855a688f6; _sctr=1|1587960000000; _dc_gtm_UA-27673166-1=1; _gat_UA-27673166-1=1; _hjid=e3005496-da9e-41df-a981-868287d91289; _fbp=fb.1.1587969320095.1569846555; AF_BANNERS_SESSION_ID=1587969323115; ab.storage.sessionId.e5ae6cfc-ff98-4431-8e2f-90df080380aa=%7B%22g%22%3A%229ef6ab9f-5f8b-0f8f-70cb-f1635e7284e2%22%2C%22e%22%3A1587971161157%2C%22c%22%3A1587969316491%2C%22l%22%3A1587969361157%7D;
# amplitude_id_7e84d9276137a0f8bb83b6725331d5d9postmates.com=eyJkZXZpY2VJZCI6ImU4YjYwNGYyLTEwODktNDc0MC1iNDdmLTQ4YjVjZWMzNWQzMFIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTU4Nzk2OTMxODQwNiwibGFzdEV2ZW50VGltZSI6MTU4Nzk2OTM2MTE3NiwiZXZlbnRJZCI6OCwiaWRlbnRpZnlJZCI6MCwic2VxdWVuY2VOdW1iZXIiOjh9
#
#
# e: [{"device_id":"e8b604f2-1089-4740-b47f-48b5cec35d30R","user_id":null,"timestamp":1587969934362,"event_id":23,"session_id":1587969318406,"event_type":"Veriphone Number - Request Completed","version_name":null,"platform":"Web","os_name":"Chrome","os_version":"81","device_model":"Mac","language":"en-US","api_properties":{},"event_properties":{"Web Version":"3.0.0","Is Logged In":false,"Last Discovery Feature":"Link","Seconds Since Session Start":41,"variant_flag_enable_brand_address_picker":true,"variant_flag_enable_cart_service_web_experiment_override":false,"variant_flag_enable_feed_filters_web":false,"variant_flag_enable_geo_delivery_near_me":true,"variant_flag_enable_group_ordering_web":true,"variant_flag_enable_landing_authentication":true,"variant_flag_enable_markets_feed_page":false,"variant_flag_enable_pickup_web":true,"variant_flag_enable_postmates_for_work_web_experiment_override":false,"variant_flag_enable_related_merchants":true,"variant_flag_enable_toasts_web":true,"variant_flag_enable_veriphone_login":true,"variant_flag_enable_veriphone_signup":true,"variant_flag_enable_web_experiment_overrides":false,"variant_flag_require_verified_phone_number":true,"variant_enable_group_ordering_web":true,"result":"Success"},"user_properties":{},"uuid":"7a31cac5-d3f0-4108-896b-fc1f43492ea6","library":{"name":"amplitude-js","version":"4.2.1"},"sequence_number":28,"groups":{},"user_agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"}]
#
#
# user_id: "c2bd0ae1-6dfe-457e-b328-3db6271d7fc8"
#
