from django.test import TestCase
from django.urls import reverse
import datetime
from faker import Faker

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
	last_Name = fake.last_name()
	first_Name = fake.first_name() 
	date_of_Birth = fake.date_time_between(start_date='-40y', end_date='now') #datetime.date(1997, 10, 19)
	address = fake.street_address() 
	city = fake.city() 
	state = fake.state()
	zip_code = int(fake.postalcode()) 
	phone = fake.phone_number()
	judo_club = fake.company()
	#rank = models.CharField('Rank', max_length=20, null=True, blank=True)
	age = 17
	sex = "M"
	judo_card = "USJUDO"
	card_number = ""
	us_citizen = "Y"
	email = fake.free_email() 
	date_added = datetime.datetime.now() #datetime.date(2019, 11, 26)
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

