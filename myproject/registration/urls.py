from django.urls import path
from registration.views import PersonCreate, PersonDelete, Payment, JudoInfo, PaymentConfirmation, Waiver, PersonSort, CreateCompetitors, CreateJuniorDivisions, CreateSeniorDivisions, displayCompetitors, ShutDown
from django.conf.urls import url, include

app_name = 'registration'

urlpatterns = [
    path('person/add/', PersonCreate.as_view(), name='person-add'),
    #path('person/add/', ShutDown),
    path('person/<int:person_id>/payment/', Payment),
    path('person/<int:person_id>/waiver/', Waiver),
    path('person/<int:person_id>/judoinfo/', JudoInfo),
    path('person/<int:person_id>/payment_confirmation', PaymentConfirmation),
    path('stats/', PersonSort),
    path('createCompetitors/', CreateCompetitors),
    path('createJuniorDivisions/', CreateJuniorDivisions),
    path('createSeniorDivisions/', CreateSeniorDivisions),
    path('<slug:competitor_class>/<int:weight_class>/competitors/',displayCompetitors), 
]
