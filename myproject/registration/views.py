from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.forms import TextInput

from registration.models import Person, JudoInfoForm, WaiverForm, JuniorMale, JuniorFemale, SeniorMale, SeniorFemale, Veteran, NoviceFemale, NoviceMale, Parameters 
from django.contrib.admin import widgets

from django import forms
import datetime
from datetime import timezone
from django.core.mail import send_mail
from django.template.loader import render_to_string

from decimal import Decimal

Payment_Options = {
        "1Jr": 70,  #
        "2Jr_Wt": 105, #
        "2Jr_Age": 105, #
        "1Jr_1Nv": 105,
        "1Jr_1Sr": 125,
        "1Nv": 70, #
        "2Nv": 105,
        "1Nv_1Vt": 105, #
        "1Nv_1Sr": 125,
        "1Sr": 90, #
        "2Sr": 150, #
        "1Vt": 70, #
        "1Vt_1Nv": 125, 
        "1Vt_1Sr": 125, #
}

# Compute total matches
def computeMatches(g):
    n = len(g)
    if len(g) <= 5:
        total_matches = max(0,n*(n-1)/2)
    elif len(g) <= 8:
        total_matches = n + 3 + max(0,n-6)
    elif len(g) <= 16:
        total_matches = n + 7 + max(0,n-12)
    elif len(g) <= 32:
        total_matches = n + 15 + max(0,n-24)
    elif len(g) <= 32:
        total_matches = n + 31 + max(0,n-48)
    else:
        total_matches = 0
    return total_matches

# Function to generate divisions from competitors
def genJrDivisions():
    params = Parameters()
    # Junior Female Divisions
    JFDivisions = []
    for age, weight in params.JF_WEIGHT.items():
        weight.append(0)
        for w in weight:
            g = JuniorFemale.objects.filter(age_group=age, weight_class=w)
            total_matches = computeMatches(g)
            JFDivisions.append((age,w,g,total_matches,total_matches*params.JR_MATCH_TIMES[age]))
    # Junior Male Divisions
    JMDivisions = []
    for age, weight  in params.JM_WEIGHT.items():
        weight.append(0)
        for w in weight:
            g = JuniorMale.objects.filter(age_group=age, weight_class=w)
            total_matches = computeMatches(g)
            JMDivisions.append((age,w,g,total_matches,total_matches*params.JR_MATCH_TIMES[age]))
    return JMDivisions, JFDivisions

# Function to generate competitors from persons
def genComp(persons):
    for person in persons:
        if "Jr" in person.category:
            if person.sex == "M":
                comp = JuniorMale.objects.filter(person=person)
                if not comp:
                    comp = JuniorMale.objects.create(person=person)
                    comp.save()
            elif person.sex == "F":
                comp = JuniorFemale.objects.filter(person=person)
                if not comp:
                    comp = JuniorFemale.objects.create(person=person)
                    comp.save()
        if "Sr" in person.category:
            if person.sex == "M":
                comp = SeniorMale.objects.filter(person=person)
                if not comp:
                    comp = SeniorMale.objects.create(person=person)
                    comp.save()
            elif person.sex == "F":
                comp = SeniorFemale.objects.filter(person=person)
                if not comp:
                    comp = SeniorFemale.objects.create(person=person)
                    comp.save()
        if "Vt" in person.category:
            comp = Veteran.objects.filter(person=person)
            if not comp:
                comp = Veteran.objects.create(person=person)
                comp.save()
        if "Nv" in person.category:
            if person.sex == "M":
                comp = NoviceMale.objects.filter(person=person)
                if not comp:
                    comp = NoviceMale.objects.create(person=person)
                    comp.save()
            elif person.sex == "F":
                comp = NoviceFemale.objects.filter(person=person)
                if not comp:
                    comp = NoviceFemale.objects.create(person=person)
                    comp.save()

# Function to Create Competitors from the person list
def CreateCompetitors(request):
    today = datetime.date.today()
    persons = Person.objects.filter(category__isnull=False, date_added__year=today.year)
    context = {}
    if request.method == "POST":
        genComp(persons)
        return HttpResponseRedirect("/registration/createCompetitors/")
    return render(request, "create_competitors.html", context)


# Function to show who is in what division
def displayCompetitors(request, competitor_class, weight_class):
    context = {}
    return render(request, "create_competitors.html", context)

# Function to display closed registration
def ShutDown(request):
    return render(request, "shutdown.html")

########## Juniors first - day one ##############
def Create2DivJuniors():
    params = Parameters()
    unique_jr_males = Person.objects.filter(category__icontains="Jr", sex="M").count() 
    # If second division is age based
    for jm in JuniorMale.objects.filter(up_one_age=True):
        if len(JuniorMale.objects.filter(person=jm.person)) >= 2:
            pass
        else:
            yr = int(jm.person.date_of_Birth.strftime('%Y'))
            try:
                while params.JM_AGES[yr] == jm.age_group:
                    yr -= 1
                new_jm = jm
                new_jm.age_group = params.JM_AGES[yr]
                new_jm.pk = None
                new_jm.save()
            except:
                print(jm)
    # If second division is weight based
    for jm in JuniorMale.objects.filter(up_one_weight=True):
        if len(JuniorMale.objects.filter(person=jm.person)) >= 2:
            pass
        else:
            try:
                weight_ind = params.JM_WEIGHT[jm.age_group].index(jm.weight_class)
                new_jm = jm
                new_jm.weight_class = params.JM_WEIGHT[jm.age_group][weight_ind+1]
                new_jm.pk = None
                new_jm.save()
            except:
                print(jm)
    # Count again
    competing_jr_males = JuniorMale.objects.count() 

    unique_jr_females = Person.objects.filter(category__icontains="Jr", sex="F").count()
    # If second division is age based
    for jf in JuniorFemale.objects.filter(up_one_age=True):
        if len(JuniorFemale.objects.filter(person=jf.person)) >= 2:
            pass
        else:
            yr = int(jf.person.date_of_Birth.strftime('%Y'))
            try:
                while params.JF_AGES[yr] == jf.age_group:
                    yr -= 1
                new_jf = jf
                new_jf.age_group = params.JF_AGES[yr]
                new_jf.pk = None
                new_jf.save()
            except:
                print(jf)
    # If second division is weight based
    for jf in JuniorFemale.objects.filter(up_one_weight=True):
        if len(JuniorFemale.objects.filter(person=jf.person)) >= 2:
            pass
        else:
            try:
                weight_ind = params.JF_WEIGHT[jf.age_group].index(jf.weight_class)
                new_jf = jf
                new_jf.weight_class = params.JF_WEIGHT[jf.age_group][weight_ind+1]
                new_jf.pk = None
                new_jf.save()
            except:
                print(jf)
    # Count again 
    competing_jr_females = JuniorFemale.objects.count()
    return unique_jr_males, competing_jr_males, unique_jr_females, competing_jr_females

# Function to create the junior divisions
def CreateJuniorDivisions(request):
    params = Parameters()
    context = {}
    if request.method == "POST":
        unique_jr_males,competing_jr_males,unique_jr_females,competing_jr_females = Create2DivJuniors() # Generate those with 2 jr divisions
        JMDivisions, JFDivisions = genJrDivisions()
        # Figure out who's not in divisions!!!
        context = {'unique_jr_males':unique_jr_males,
               'competing_jr_males':competing_jr_males,
               'unique_jr_females':unique_jr_females,
               'competing_jr_females':competing_jr_females,
               'JMDivisions':JMDivisions, 'JFDivisions':JFDivisions}
    return render(request, "create_divisions.html", context)

# Function to create the senior divisions
def CreateSeniorDivisions(request):
    params = Parameters()
    context = {}
    """if request.method == "POST":
        unique_jr_males,competing_jr_males,unique_jr_females,competing_jr_females = Create2DivJuniors() # Generate those with 2 jr divisions
        JMDivisions, JFDivisions = genJrDivisions()
        # Figure out who's not in divisions!!!
        context = {'unique_jr_males':unique_jr_males,
               'competing_jr_males':competing_jr_males,
               'unique_jr_females':unique_jr_females,
               'competing_jr_females':competing_jr_females,
               'JMDivisions':JMDivisions, 'JFDivisions':JFDivisions}"""
    return render(request, "create_divisions.html", context)

def PersonSort(request):
    people = Person.objects.all()
    # Sort juniors and duplicate category juniors
    juniors = Person.objects.filter(category__contains='Jr')
    div2_juniors = juniors.filter(category__contains='2Jr')
    # Sort novice seniors and duplicte category seniors
    novice = Person.objects.filter(category__contains='Nv')
    div2_novice = novice.filter(category__contains='2Nv')
    # Sort elite seniors cause that's all anyone cares about anyway
    elite = Person.objects.filter(category__contains='Sr')
    div2_elite = elite.filter(category__contains='2Sr')
    # Sort veterans and duplicate category veterans 
    veterans = Person.objects.filter(category__contains='Vt')
    div2_veterans = veterans.filter(category__contains='Vt')
    # Tally all of this up
    no_unique_juniors = len(juniors) 
    no_competing_juniors = len(juniors) + len(div2_juniors)
    no_novice = len(novice)
    no_competing_novice = len(novice) + len(div2_novice)
    no_elite = len(elite)
    no_competing_elite = len(elite) + len(div2_elite)
    no_veterans = len(veterans)
    no_competing_veterans = len(veterans) + len(div2_veterans)
    context = {"no_unique_juniors": no_unique_juniors,
		"no_competing_juniors": no_competing_juniors,
		"no_novice": no_novice,
		"no_competing_novice": no_competing_novice,
		"no_elite": no_elite,
		"no_competing_elite": no_competing_elite,
		"no_veterans": no_veterans,
		"no_competing_veterans": no_competing_veterans}
    return render(request, "competitor_stats.html", context)

def JudoInfo(request, person_id):
    person = Person.objects.get(pk=int(person_id))
    form = JudoInfoForm(instance=person)
    if request.method == "POST":  
        form = JudoInfoForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/registration/person/"+str(person_id)+"/waiver/")
        else: 
            context = {'form':form, 'person':person}
            return render(request, "competitor_form.html", context) 
    context = {'form':form, 'person':person}
    return render(request, "competitor_form.html", context) 

def Payment(request, person_id):
    person = Person.objects.get(pk=int(person_id)) 
    amount = Payment_Options[person.category]
    context = {'person':person, 'amount':amount}
    return render(request, "payment_form.html", context)

def Waiver(request, person_id):
    person = Person.objects.get(pk=int(person_id)) 
    age = (datetime.datetime.now(timezone.utc) - person.date_of_Birth).days / 365.25
    form = WaiverForm(instance=person)
    if age<18:
        form.fields['gaurdian_field'].required=True
    if request.method == "POST":
        form = WaiverForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/registration/person/"+str(person_id)+"/payment/")
        else:
            return HttpResponseRedirect("/admin/")
    context = {'form':form, 'person':person, 'is_minor':(age<18)}
    return render(request, "waiver_form.html", context)

def PaymentConfirmation(request, person_id):
    person = Person.objects.get(pk=int(person_id))
    person.has_paid = True
    person.save()
    context = {'person':person}
    body = render_to_string('confirmation_email.txt', context)
    send_mail(
	'LBJ 2019 Registration Confirmation',
	'This is your confirmation email. Please see specifics in the info below.',
	'info@libertybellregistration.com',
	[person.email, 'libertybelljudo@gmail.com'],
	fail_silently=False,
	html_message=body,
    )
    return render(request, "success.html", context)

class PersonForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        self.fields['first_Name'].widget.attrs['style'] = 'width:150px;'
        self.fields['last_Name'].widget.attrs['style'] = 'width:150px;'
        self.fields['address'].widget.attrs['style'] = 'width:300px;'
        self.fields['city'].widget.attrs['style'] = 'width:120px;'
        self.fields['state'].widget.attrs['style'] = 'width:120px;'
        self.fields['zip_code'].widget.attrs['style'] = 'width:100px;'
        self.fields['phone'].widget.attrs['style'] = 'width:150px;'
        self.fields['email'].widget.attrs['style'] = 'width:150px;'

    class Meta:
        model = Person
        fields = ['first_Name','last_Name','address','city','state','zip_code','phone','email']
        widgets = {
            'zip_code': TextInput(attrs={})
        }

class PersonCreate(CreateView):
    form_class = PersonForm 
    model = Person 

    def get_success_url(self):
        return "/registration/person/%s/judoinfo/" % str(self.object.id)

class PersonUpdate(UpdateView):
    model = Person 
    fields = "__all__" 

class PersonDelete(DeleteView):
    model = Person
    success_url = reverse_lazy('person-list')
