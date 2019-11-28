from django.test import TestCase
from django.urls import reverse
import datetime
from faker import Faker
import random
from dateutil.relativedelta import relativedelta

from .models import Person 

fake = Faker()

# Create your tests here.
class PersonTests(TestCase):
	def setUp(self):
		last_Name = "Moyerman"
		first_Name = "Stephanie" 
		date_of_Birth = datetime.date(1997, 10, 19)
		address = "9821 Ferndale St" 
		city = "Phila" 
		state = "Pennsylvania" 
		zip_code = 19115 
		phone = "215-485-6034" 
		judo_club = "Liberty Bell Judo" 
		#rank = models.CharField('Rank', max_length=20, null=True, blank=True)
		age = 17 
		sex = "M" 
		judo_card = "USJUDO" 
		card_number = "" 
		us_citizen = "Y" 
		email = "smoyerman@gmail.com"
		date_added = datetime.date(2019, 11, 26) 
		category = "1Jr" 
		proposedweightclass = 89.2 
		waiver = True 
		has_paid = True 
		is_test = True 
		Person.objects.create(last_Name=last_Name,first_Name=first_Name,date_of_Birth=date_of_Birth,
			address=address,city=city,state=state,zip_code=zip_code,phone=phone,judo_club=judo_club,
			age=age,sex=sex,judo_card=judo_card,card_number=card_number,us_citizen=us_citizen,
			email=email,date_added=date_added,category=category,proposedweightclass=proposedweightclass,
			waiver=waiver,has_paid=has_paid,is_test=is_test)

def CreatePerson():
	sex = random.choice(["M","M","M","F"])
	last_Name = fake.last_name()
	if sex=="M":
		first_Name = fake.first_name_male()
	else:
		first_Name = fake.first_name_female() 
	date_of_Birth = fake.date_time_between(start_date='-40y', end_date='-5y') #datetime.date(1997, 10, 19)
	address = fake.street_address() 
	city = fake.city() 
	state = fake.state()
	zip_code = int(fake.postalcode()) 
	phone = fake.phone_number()
	judo_club = fake.company()
	#rank = models.CharField('Rank', max_length=20, null=True, blank=True)
	today = datetime.date.today()
	age = today.year - date_of_Birth.year - ((today.month, today.day) < (date_of_Birth.month, date_of_Birth.day))
	judo_card = "USJUDO"
	card_number = ""
	us_citizen = random.choice(["Y","Y","Y","N"])
	email = fake.free_email() 
	date_added = datetime.datetime.now() #datetime.date(2019, 11, 26)
	if age < 17:
		category = random.choice(["1Jr","2Jr_Wt","2Jr_Age"])
	elif age < 20:
		category = random.choice(["1Jr","2Jr_Wt","2Jr_Age","1Jr_1Nv","1Jr_1Sr"])
	elif age < 30:
		category = random.choice(["1Nv","2Nv","1Nv_1Sr","1Sr","2Sr"])
	else:
		category = random.choice(["1Nv","2Nv","1Nv_1Vt","1Nv_1Sr","1Sr","2Sr","1Vt","1Vt_1Nv","1Vt_1Sr"])
	if age < 10:
		proposedweightclass = random.randint(20,50) 
	elif (age < 20) and (sex=="M"):
		proposedweightclass = random.randint(35,110) 
	elif (age < 20) and (sex=="F"):
		proposedweightclass = random.randint(32,80) 
	elif sex=="F":
		proposedweightclass = random.randint(42,85) 
	else:
		proposedweightclass = random.randint(50,110) 
	waiver = True
	has_paid = True
	is_test = True
	Person.objects.create(last_Name=last_Name,first_Name=first_Name,date_of_Birth=date_of_Birth,
		address=address,city=city,state=state,zip_code=zip_code,phone=phone,judo_club=judo_club,
		age=age,sex=sex,judo_card=judo_card,card_number=card_number,us_citizen=us_citizen,
		email=email,date_added=date_added,category=category,proposedweightclass=proposedweightclass,
		waiver=waiver,has_paid=has_paid,is_test=is_test)

