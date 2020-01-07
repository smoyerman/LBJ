from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.forms import ModelForm
from django.urls import reverse
from django.contrib.admin import widgets
from django.forms import TextInput

import django.forms as forms
import datetime
from django import forms

class Parameters(object):
    JM_AGES = {}
    JM_AGES[2000]='IJF'
    JM_AGES[2001]='IJF'
    JM_AGES[2002]='IJF'
    JM_AGES[2003]='Cadet'
    JM_AGES[2004]='Cadet'
    JM_AGES[2005]='Cadet'
    JM_AGES[2006]='Juvenile'
    JM_AGES[2007]='Juvenile'
    JM_AGES[2008]='Intermed.'
    JM_AGES[2009]='Intermed.'
    JM_AGES[2010]='Bantam 3'
    JM_AGES[2011]='Bantam 3'
    JM_AGES[2012]='Bantam 2'
    JM_AGES[2013]='Bantam 2'
    JM_WEIGHT = {}
    JM_WEIGHT['6-8'] = [19,21,23,26,31,35]
    JM_WEIGHT['9-10'] = [26,30,34,38,43]
    JM_WEIGHT['11-12'] = [28,31,34,38,42,47,52]
    JM_WEIGHT['13-14'] = [36,40,44,48,53,58,64]
    JM_WEIGHT['15-17'] = [50,55,60,66,73,81,90]
    JM_WEIGHT['18-20'] = [60,66,73,81,90,100] 

    JF_AGES = {}
    JF_AGES[2000]='IJF'
    JF_AGES[2001]='IJF'
    JF_AGES[2002]='IJF'
    JF_AGES[2003]='Cadet'
    JF_AGES[2004]='Cadet'
    JF_AGES[2005]='Cadet'
    JF_AGES[2006]='Juvenile'
    JF_AGES[2007]='Juvenile'
    JF_AGES[2008]='Intermed.'
    JF_AGES[2009]='Intermed.'
    JF_AGES[2010]='Bantam 3'
    JF_AGES[2011]='Bantam 3'
    JF_AGES[2012]='Bantam 2'
    JF_AGES[2013]='Bantam 2'
    JF_WEIGHT = {}
    JF_WEIGHT['6-8'] = [19,21,23,26,31,35]
    JF_WEIGHT['9-10'] = [26,30,34,38,43]
    JF_WEIGHT['11-12'] = [28,31,34,38,42,47,52]
    JF_WEIGHT['13-14'] = [36,40,44,48,53,58,64]
    JF_WEIGHT['15-17'] = [40,44,48,52,57,63,70]
    JF_WEIGHT['18-20'] = [48,52,57,63,70,78]

    NF_WEIGHTS = [57,70]
    EF_WEIGHTS = [48,52,57,63,70,78]

    NM_WEIGHT = {}
    NM_WEIGHT['Novice'] = [60,66,73,81,90,100]
    NM_WEIGHT['Brown'] = [60,66,73,81,90,100]
    EM_WEIGHTS = [60,66,73,81,90,100]

    VT_WEIGHT = {}
    VT_WEIGHT['M'] = [70,81,94]
    VT_WEIGHT['F'] = [55,70]

    JR_MATCH_TIMES = {}
    JR_MATCH_TIMES['6-8'] = 3
    JR_MATCH_TIMES['9-10'] = 3
    JR_MATCH_TIMES['11-12'] = 3
    JR_MATCH_TIMES['13-14'] = 3
    JR_MATCH_TIMES['15-17'] = 3
    JR_MATCH_TIMES['18-20'] = 4

############################# MODELS ######################################
class Person(models.Model):
    STATE_CHOICES = (("Alabama","Alabama"),("Alaska","Alaska"),("Arizona","Arizona"),("Arkansas","Arkansas"),("California","California"),("Colorado","Colorado"),("Connecticut","Connecticut"),("Delaware","Delaware"),("Florida","Florida"),("Georgia","Georgia"),("Hawaii","Hawaii"),("Idaho","Idaho"),("Illinois","Illinois"),("Indiana","Indiana"),("Iowa","Iowa"),("Kansas","Kansas"),("Kentucky","Kentucky"),("Louisiana","Louisiana"),("Maine","Maine"),("Maryland","Maryland"),("Massachusetts","Massachusetts"),("Michigan","Michigan"),("Minnesota","Minnesota"),("Mississippi","Mississippi"),("Missouri","Missouri"),("Montana","Montana"),("Nebraska","Nebraska"),("Nevada","Nevada"),("New Hampshire","New Hampshire"),("New Jersey","New Jersey"),("New Mexico","New Mexico"),("New York","New York"),("North Carolina","North Carolina"),("North Dakota","North Dakota"),("Ohio","Ohio"),("Oklahoma","Oklahoma"),("Oregon","Oregon"),("Pennsylvania","Pennsylvania"),("Rhode","Rhode"),("Island","Island"),("South Carolina","South Carolina"),("South Dakota","South Dakota"),("Tennessee","Tennessee"),("Texas","Texas"),("Utah","Utah"),("Vermont","Vermont"),("Virginia","Virginia"),("Washington","Washington"),("West Virginia","West Virginia"),("Wisconsin","Wisconsin"),("Wyoming","Wyoming"))
    SEX_CHOICES = (("M","Male"),("F","Female"))
    CARD_CHOICES = (("USJUDO", "USA Judo"), ("USJA","USJA"), ("USJF","USJF"), ("INTL","International"))
    YESNO_CHOICES = (("Y","Yes"),("N","No"))
    CATEGORY_CHOICES = (
        ("1Jr","One Youth Division ($70)"),
        ("2Jr_Wt","2 Youth Divisions - Up One Weight ($105)"),
        ("2Jr_Age", "2 Youth Divisions - Up One Age ($105)"),
        ("1Jr_1Nv", "1 Youth + 1 Senior Non-Elite ($105)"),
        ("1Jr_1Sr", "1 Youth + 1 Senior Elite Division ($125)"),
        ("1Nv", "1 Non-Elite Senior Division ($70)"),
        ("2Nv", "2 Non-Elite Senior Divisions ($105)"),
        ("1Nv_1Vt", "1 Novice and 1 Veteran ($105)"),
        ("1Nv_1Sr", "1 Non-Elite + 1 Elite Senior Division ($125)"),
        ("1Sr", "1 Senior Elite Division ($90)"),
        ("2Sr", "2 Senior Elite Divisions ($150)"),
        ("1Vt", "1 Veteran Division ($70)"),
        ("1Vt_1Nv", "1 Veteran and 1 Senior Non-Elite Division ($125)"),
        ("1Vt_1Sr", "1 Veteran and 1 Senior Elite Division ($125)"),
    ) 

    last_Name = models.CharField('Last Name', max_length=50)
    first_Name = models.CharField('First Name', max_length=50)
    date_of_Birth = models.DateTimeField('Date of Birth', blank=True, null=True)
    address = models.CharField('Address', max_length=100, null=True)
    city = models.CharField('City', max_length=50, null=True)
    state = models.CharField('State', blank=True, null=True, max_length=20)
    zip_code = models.IntegerField('Zip', blank=True, null=True)
    phone = models.CharField('Tel. #', max_length=22, blank=True, null=True)
    judo_club = models.CharField('Judo Club', max_length=100, null=True, blank=True)
    rank = models.CharField('Rank', max_length=20, null=True, blank=True)
    age = models.IntegerField('Age', null=True, blank=True)
    sex = models.CharField('Sex', max_length=1, choices=SEX_CHOICES, null=True, blank=True)
    judo_card = models.CharField(max_length=6, choices=CARD_CHOICES, null=True, blank=True)
    card_number = models.CharField(max_length=20, null=True, blank=True)
    us_citizen = models.CharField(max_length=1, null=True, choices=YESNO_CHOICES, blank=True)
    email = models.EmailField(null=True)
    date_added = models.DateField(auto_now_add=True, null=True)
    category = models.CharField('Divisions', max_length=10, blank=True, null=True, choices=CATEGORY_CHOICES)
    proposedweightclass = models.DecimalField("Proposed Weight Class (kgs)", decimal_places=1, max_digits=4, blank=True, null=True, help_text="Estimated weigh-in weight (e.g., 57)")
    waiver = models.BooleanField('Has Signed Waiver', default=False)
    has_paid = models.BooleanField('Has Paid', default=False)
    is_test = models.BooleanField('Is Test', default=False)

    def __str__(self):
        return self.last_Name + ", " + self.first_Name

    def get_absolute_url(self):
        return reverse('person-detail', kwargs={'pk': self.pk})


class JuniorMale(models.Model):
    AGE_CHOICES = (('Bantam 2','2012-2013 (Bantam 2)'), ('Bantam 3','2010-2011 (Bantam 3)'),('Intermed.','2008-2009 (Intermed.)'),
            ('Juvenile','2006-2007 (Juvenile)'), ('Cadet','2003-2005 (Cadet)'), ('IJF','2000-2002 (IJF)'))
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    age_group = models.CharField("Age Group", max_length=10, choices=AGE_CHOICES, null=True)
    weight_class = models.DecimalField("Weight Class (kgs)", decimal_places=1, max_digits=4, blank=True, null=True)
    actual_weight = models.DecimalField("Weigh In Weight", decimal_places=1, max_digits=4, blank=True, null=True)
    up_one_age = models.BooleanField('Second Division Weight', max_length=1, default=False)
    up_one_weight = models.BooleanField('Second Division Age', max_length=1, default=False)

    def __str__(self):
        return self.person.first_Name + " " + self.person.last_Name

    def save(self, *args, **kwargs):
        params = Parameters()
        AGES = params.JM_AGES
        WEIGHT = params.JM_WEIGHT
        try:
            yr = int(self.person.date_of_Birth.strftime('%Y'))
            self.age_group = AGES[yr]
        except:
            pass
        self.weight_class = self.person.proposedweightclass
        if self.person.category == "2Jr_Wt":
            self.up_one_age = True
        if self.person.category == "2Jr_Age":
            self.up_one_weight = True
        if (getattr(self, 'actual_weight') == None) or (getattr(self, 'age_group') == None):
            super(JuniorMale, self).save(*args, **kwargs)
            pass
        else:
            kgs = getattr(self, 'actual_weight')
            # Implement weight class info
            if kgs > WEIGHT[getattr(self, 'age_group')][-1]:
                self.weight_class = 0
            else:
                for w in WEIGHT[getattr(self, 'age_group')]:
                    if kgs <= w:
                        self.weight_class = w
                        break
            super(JuniorMale, self).save(*args, **kwargs)
            # Implement logic for second division
            SM = SeniorMale.objects.filter(person=self.person)
            if SM:
                for s in SM:
                    s.actual_weight = kgs
                    s.save()
            NM = NoviceMale.objects.filter(person=self.person)
            if NM:
                for n in NM:
                    n.actual_weight = kgs
                    n.save()


class JuniorFemale(models.Model):
    AGE_CHOICES = (('Bantam 2','2012-2013 (Bantam 2)'), ('Bantam 3','2010-2011 (Bantam 3)'),('Intermed.','2008-2009 (Intermed.)'),
            ('Juvenile','2006-2007 (Juvenile)'), ('Cadet','2003-2005 (Cadet)'), ('IJF','2000-2002 (IJF)'))
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    age_group = models.CharField("Age Group", max_length=10, choices=AGE_CHOICES, null=True)
    weight_class = models.DecimalField("Weight Class (kgs)", decimal_places=1, max_digits=4, blank=True, null=True)
    actual_weight = models.DecimalField("Weigh In Weight", decimal_places=1, max_digits=4, blank=True, null=True)
    up_one_age = models.BooleanField('Second Division Age', max_length=1, default=False)
    up_one_weight = models.BooleanField('Second Division Weight', max_length=1, default=False)
        
    def __str__(self):
        return self.person.first_Name + " " + self.person.last_Name

    def save(self, *args, **kwargs):
        params = Parameters()
        AGES = params.JF_AGES
        WEIGHT = params.JF_WEIGHT
        try:
            yr = int(self.person.date_of_Birth.strftime('%Y'))
            self.age_group = AGES[yr]
        except:
            pass        
        self.weight_class = self.person.proposedweightclass
        if self.person.category == "2Jr_Wt":
            self.up_one_age = True
        if self.person.category == "2Jr_Age":
            self.up_one_weight = True
        if (getattr(self, 'actual_weight') == None) or (getattr(self, 'age_group') == None):
            super(JuniorFemale, self).save(*args, **kwargs)
            pass
        else:
            kgs = getattr(self, 'actual_weight')
            # Implement logic for weight classes 
            if kgs > WEIGHT[getattr(self, 'age_group')][-1]:
                self.weight_class = 0
            else:
                for w in WEIGHT[getattr(self, 'age_group')]:
                    if kgs <= w:
                        self.weight_class = w
                        break
            super(JuniorFemale, self).save(*args, **kwargs)
            # Implement logic for second division
            SF = SeniorFemale.objects.filter(person=self.person)
            if SF:
                for s in SF:
                    s.actual_weight = kgs
                    s.save()
            NF = NoviceFemale.objects.filter(person=self.person)
            if NF:
                for n in NF:
                    n.actual_weight = kgs
                    n.save()


class NoviceFemale(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    weight = models.DecimalField("Weight (kgs)", decimal_places=1, max_digits=4, blank=True, null=True)
    actual_weight = models.DecimalField("Weigh In Weight (kgs)", decimal_places=1, max_digits=4, blank=True, null=True)
    up_one_weight = models.BooleanField('Second Division Weight', max_length=1, default=False)

    def __str__(self):
        return self.person.first_Name + " " + self.person.last_Name

    class Meta:
        verbose_name = 'Novice Female'

    def save(self, *args, **kwargs):
        params = Parameters()
        WEIGHTS = params.NF_WEIGHTS
        if self.person.category == "2Nv":
            self.up_one_weight = True
        self.weight = self.person.proposedweightclass
        if (getattr(self, 'actual_weight') == None): 
            super(NoviceFemale, self).save(*args, **kwargs)
            pass
        else:
            kgs = getattr(self, 'actual_weight')
            # Implement logic for weight classes
            if kgs > WEIGHTS[-1]:
                self.weight = 0
            else:
                for w in WEIGHTS:
                    if kgs <= w:
                        self.weight = w
                        break
            super(NoviceFemale, self).save(*args, **kwargs)
            # Implement logic for second division
            VT = Veteran.objects.filter(person=self.person)
            if VT:
                for v in VT:
                    if not v.actual_weight:
                        v.actual_weight = kgs
                        v.save()
            SF = SeniorFemale.objects.filter(person=self.person)
            if SF:
                for s in SF:
                    if not s.actual_weight:
                        s.actual_weight = kgs
                        s.save()


class SeniorFemale(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    weight = models.DecimalField("Weight (kgs)", decimal_places=1, max_digits=4, blank=True, null=True)
    actual_weight = models.DecimalField("Weigh In Weight (kgs)", decimal_places=1, max_digits=4, blank=True, null=True)
    up_one_weight = models.BooleanField('Second Division Weight', max_length=1, default=False)

    def __str__(self):
        return self.person.first_Name + " " + self.person.last_Name 

    class Meta:
        verbose_name = 'Elite Female'

    def save(self, *args, **kwargs):
        params = Parameters()
        WEIGHTS = params.EF_WEIGHTS
        if self.person.category == "2Sr":
            self.up_one_weight = True
        self.weight = self.person.proposedweightclass
        if (getattr(self, 'actual_weight') == None):
            super(SeniorFemale, self).save(*args, **kwargs)
            pass
        else:
            kgs = getattr(self, 'actual_weight')
            # Implement logic for weight classes
            if kgs > WEIGHTS[-1]:
                self.weight = 0
            else:
                for w in WEIGHTS:
                    if kgs <= w:
                        self.weight = w
                        break
            super(SeniorFemale, self).save(*args, **kwargs)
            # Implement logic for second division
            VT = Veteran.objects.filter(person=self.person)
            if VT:
                for v in VT:
                    if not v.actual_weight:
                        v.actual_weight = kgs
                        v.save()
            NF = NoviceFemale.objects.filter(person=self.person)
            if NF:
                for n in NF:
                    if not n.actual_weight:
                        n.actual_weight = kgs
                        n.save()


class NoviceMale(models.Model):
    CATEGORY_CHOICES = (('Novice','Novice'),
                        ('Brown','Brown'))
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    category = models.CharField('Competitor Category', max_length=6, choices=CATEGORY_CHOICES, null=True, blank=True)
    weight = models.DecimalField("Weight (kgs)", decimal_places=1, max_digits=4, blank=True, null=True)
    actual_weight = models.DecimalField("Weigh In Weight (kgs)", decimal_places=1, max_digits=4, blank=True, null=True)
    up_one_category = models.BooleanField('Second Division Novice/Elite', max_length=1, default=False)
    up_one_weight = models.BooleanField('Second Division Weight', max_length=1, default=False)

    def __str__(self):
        return self.person.first_Name + " " + self.person.last_Name

    class Meta:
        verbose_name = 'Novice Male'

    # Override save method
    def save(self, *args, **kwargs):
        params = Parameters()
        WEIGHT = params.NM_WEIGHT
        if self.person.category == "1Nv_1Sr":
            self.up_one_category = True
        if self.person.category in ("2Nv", "2Sr"):
            self.up_one_weight = True
        self.weight = self.person.proposedweightclass
        if (getattr(self, 'actual_weight') == None) or (getattr(self, 'category') == None):
            super(NoviceMale, self).save(*args, **kwargs)
            pass
        else:
            kgs = getattr(self, 'actual_weight')
            # Implement logic for weight classes
            if kgs > WEIGHT[getattr(self, 'category')][-1]:
                self.weight = 0
            else:
                for w in WEIGHT[getattr(self, 'category')]:
                    if kgs <= w:
                        self.weight = w
                        break
            super(NoviceMale, self).save(*args, **kwargs)
            # Implement logic for second division
            VT = Veteran.objects.filter(person=self.person)
            if VT:
                for v in VT:
                    if not v.actual_weight:
                        v.actual_weight = kgs
                        v.save()
            SM = SeniorMale.objects.filter(person=self.person)
            if SM:      
                for s in SM:
                    if not s.actual_weight:
                        s.actual_weight = kgs
                        s.save()


class SeniorMale(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    weight = models.DecimalField("Weight (kgs)", decimal_places=1, max_digits=4, blank=True, null=True)
    actual_weight = models.DecimalField("Weigh In Weight (kgs)", decimal_places=1, max_digits=4, blank=True, null=True)
    up_one_weight = models.BooleanField('Second Division Weight', max_length=1, default=False)

    def __str__(self):
        return self.person.first_Name + " " + self.person.last_Name 

    class Meta:
        verbose_name = 'Elite Male'

    # Override save method
    def save(self, *args, **kwargs):
        params = Parameters()
        WEIGHTS = params.EM_WEIGHTS
        if self.person.category == "2Sr":
            self.up_one_weight = True
        self.weight = self.person.proposedweightclass
        if (getattr(self, 'actual_weight') == None):
            super(SeniorMale, self).save(*args, **kwargs)
            pass
        else:    
            kgs = getattr(self, 'actual_weight')
            # Implement logic for weight classes
            if kgs > WEIGHTS[-1]:
                self.weight = 0
            else:
                for w in WEIGHTS:
                    if kgs <= w:
                        self.weight = w
                        break
            super(SeniorMale, self).save(*args, **kwargs)
            # Implement logic for second division
            VT = Veteran.objects.filter(person=self.person)
            if VT:
                for v in VT:
                    if not v.actual_weight:
                        v.actual_weight = kgs
                        v.save()
            NM = NoviceMale.objects.filter(person=self.person)
            if NM:      
                for n in NM:
                    if not n.actual_weight:
                        n.actual_weight = kgs
                        n.save()


class Veteran(models.Model):
    GENDER_CHOICES = (('M','Male'),
		      ('F','Female'))
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    gender = models.CharField('Gender', max_length=6, choices=GENDER_CHOICES, null=True, blank=True)
    weight = models.DecimalField("Weight (kgs)", decimal_places=1, max_digits=4, blank=True, null=True)
    actual_weight = models.DecimalField("Weigh In Weight (kgs)", decimal_places=1, max_digits=4, blank=True, null=True)

    def __str__(self):
        return self.person.first_Name + " " + self.person.last_Name 

    class Meta:
        verbose_name = 'Veteran'

    # Override save method
    def save(self, *args, **kwargs):
        params = Parameters()
        WEIGHT = params.VT_WEIGHT
        self.gender = self.person.sex
        self.weight = self.person.proposedweightclass
        if (getattr(self, 'actual_weight') == None) or (getattr(self, 'gender') == None):
            super(Veteran, self).save(*args, **kwargs) 
            pass
        else:
            kgs = getattr(self, 'actual_weight')
            # weight class determination
            if kgs > WEIGHT[getattr(self, 'gender')][-1]:
                self.weight = 0
            else:
                for w in WEIGHT[getattr(self, 'gender')]:
                    if kgs <= w:
                        self.weight = w
                        break
            super(Veteran, self).save(*args, **kwargs)
            # Implement logic for second division
            if getattr(self, 'gender') == 'F':
                NF = NoviceFemale.objects.filter(person=self.person)
                if NF:
                    for n in NF:
                        if not n.actual_weight:
                            n.actual_weight = kgs
                            n.save()
                SF = SeniorFemale.objects.filter(person=self.person)
                if SF:
                    for s in SF:
                        if not s.actual_weight:
                            s.actual_weight = kgs
                            s.save()
            elif getattr(self, 'gender') == 'M':
                NM = NoviceMale.objects.filter(person=self.person)
                if NM:
                    for n in NM:
                        if not n.actual_weight:
                            n.actual_weight = kgs
                            n.save()
                SM = SeniorMale.objects.filter(person=self.person)
                if SM:
                    for s in SM:
                        if not s.actual_weight:
                            s.actual_weight = kgs
                            s.save()


class WaiverForm(ModelForm):
    gaurdian_field = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.Meta.required:
            self.fields[field].required=True

    class Meta:
        model = Person
        fields = ('waiver',)
        required = ('waiver',)

class JudoInfoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
	
        for field in self.Meta.required:
            self.fields[field].required=True

    class Meta:
        model = Person
        fields = ['sex','date_of_Birth','us_citizen','judo_club','rank','judo_card','card_number', 'category','proposedweightclass']
        widgets = {
            'date_of_Birth': forms.SelectDateWidget(
               years = range(datetime.datetime.now().year-100,datetime.datetime.now().year),    
	    ),
            'proposedweightclass': TextInput(attrs={}),
        }
        required = ('sex','date_of_Birth','us_citizen','judo_club','rank','category', 'proposedweightclass')





