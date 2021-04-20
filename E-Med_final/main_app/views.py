from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from datetime import date

from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import patient, doctor, diseaseinfo, consultation, Hospital, remedies
from chats.models import Chat, Feedback

# Create your views here.


# loading trained_model
import joblib as jb
model = jb.load('trained_model')


def home(request):

    if request.method == 'GET':

        if request.user.is_authenticated:
            return render(request, 'homepage/index.html')

        else:
            return render(request, 'homepage/index.html')
    

def about(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'homepage/about.html')
        else:
            return render(request, 'homepage/about.html')


def mdoctor(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'homepage/doctor.html')

        else:
            return render(request, 'homepage/doctor.html')

def viewhospital(request):
    if request.method == 'GET':

        if request.user.is_authenticated:
            return render(request, 'homepage/viewhospital.html')

        else:
            return render(request, 'homepage/viewhospital.html')

def viewremedy(request):
    if request.method == 'GET':

        if request.user.is_authenticated:
            return render(request, 'homepage/viewremedy.html')

        else:
            return render(request, 'homepage/viewremedy.html')


"""def contact(request):
    if request.method == 'GET':

        if request.user.is_authenticated:
            return render(request, 'homepage/contact.html')

        else:
            return render(request, 'homepage/contact.html')"""





def patient_ui(request):

    if request.method == 'GET':

        if request.user.is_authenticated:

            patientusername = request.session['patientusername']
            puser = User.objects.get(username=patientusername)

            return render(request, 'patient/patient_ui/profile.html', {"puser": puser})

        else:
            return redirect('home')

    if request.method == 'POST':

        return render(request, 'patient/patient_ui/profile.html')


def pviewprofile(request, patientusername):

    if request.method == 'GET':

        puser = User.objects.get(username=patientusername)

        return render(request, 'patient/view_profile/view_profile.html', {"puser": puser})


def checkdisease(request):

    diseaselist = ['Fungal infection', 'Allergy', 'GERD', 'Chronic cholestasis', 'Drug Reaction', 'Peptic ulcer diseae', 'AIDS', 'Diabetes ',
                   'Gastroenteritis', 'Bronchial Asthma', 'Hypertension ', 'Migraine', 'Cervical spondylosis', 'Paralysis (brain hemorrhage)',
                   'Jaundice', 'Malaria', 'Chicken pox', 'Dengue', 'Typhoid', 'hepatitis A', 'Hepatitis B', 'Hepatitis C', 'Hepatitis D',
                   'Hepatitis E', 'Alcoholic hepatitis', 'Tuberculosis', 'Common Cold', 'Pneumonia', 'Dimorphic hemmorhoids(piles)',
                   'Heart attack', 'Varicose veins', 'Hypothyroidism', 'Hyperthyroidism', 'Hypoglycemia', 'Osteoarthristis',
                   'Arthritis', '(vertigo) Paroymsal  Positional Vertigo', 'Acne', 'Urinary tract infection', 'Psoriasis', 'Impetigo']

    symptomslist = ['itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills', 'joint_pain',
                    'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition', 'spotting_ urination',
                    'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness', 'lethargy',
                    'patches_in_throat', 'irregular_sugar_level', 'cough', 'high_fever', 'sunken_eyes', 'breathlessness', 'sweating',
                    'dehydration', 'indigestion', 'headache', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes',
                    'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine',
                    'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach',
                    'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation',
                    'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs',
                    'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool',
                    'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs',
                    'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails',
                    'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips',
                    'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints',
                    'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness',
                    'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine',
                    'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)',
                    'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain',
                    'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum',
                    'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion',
                    'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen',
                    'history_of_alcohol_consumption', 'fluid_overload', 'blood_in_sputum', 'prominent_veins_on_calf',
                    'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling',
                    'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose',
                    'yellow_crust_ooze']

    alphabaticsymptomslist = sorted(symptomslist)

    if request.method == 'GET':

        return render(request, 'patient/checkdisease/checkdisease.html', {"list2": alphabaticsymptomslist})

    elif request.method == 'POST':

        # access you data by playing around with the request.POST object

        inputno = int(request.POST["noofsym"])
        print(inputno)
        if (inputno == 0):
            return JsonResponse({'predicteddisease': "none", 'confidencescore': 0})

        else:

            psymptoms = []
            psymptoms = request.POST.getlist("symptoms[]")

            print(psymptoms)

            """      #main code start from here...
        """

            testingsymptoms = []
            # append zero in all coloumn fields...
            for x in range(0, len(symptomslist)):
                testingsymptoms.append(0)

            # update 1 where symptoms gets matched...
            for k in range(0, len(symptomslist)):

                for z in psymptoms:
                    if (z == symptomslist[k]):
                        testingsymptoms[k] = 1

            inputtest = [testingsymptoms]

            print(inputtest)

            predicted = model.predict(inputtest)
            print("predicted disease is : ")
            print(predicted)

            y_pred_2 = model.predict_proba(inputtest)
            confidencescore = y_pred_2.max() * 100
            print(" confidence score of : = {0} ".format(confidencescore))

            confidencescore = format(confidencescore, '.0f')
            predicted_disease = predicted[0]

       #consult_doctor codes----------

        Rheumatologist = [  'Osteoarthristis','Arthritis']
       
        Cardiologist = [ 'Heart attack','Bronchial Asthma','Hypertension ']
       
        ENT_specialist = ['(vertigo) Paroymsal  Positional Vertigo','Hypothyroidism' ]

        Orthopedist = []

        Neurologist = ['Varicose veins','Paralysis (brain hemorrhage)','Migraine','Cervical spondylosis']

        Allergist_Immunologist = ['Allergy','Pneumonia','AIDS','Common Cold','Tuberculosis','Malaria','Dengue','Typhoid']

        Urologist = [ 'Urinary tract infection','Dimorphic hemmorhoids(piles)']

        Dermatologist = [  'Acne','Chicken pox','Fungal infection','Psoriasis','Impetigo']

        Gastroenterologist = ['Peptic ulcer diseae', 'GERD','Chronic cholestasis','Drug Reaction','Gastroenteritis','Hepatitis E',
        'Alcoholic hepatitis','Jaundice','hepatitis A',
         'Hepatitis B', 'Hepatitis C', 'Hepatitis D','Diabetes ','Hypoglycemia']
         
        if predicted_disease in Rheumatologist :
           consultdoctor = "Rheumatologist"
           hospital = "Nepal_Orthopedic_Hospital"
           remedy = "Home Remedies"
           
        if predicted_disease in Cardiologist :
           consultdoctor = "Cardiologist"
           hospital = "Sahid_Gangalal_National_Heart_Center"
           remedy = "Home Remedies"
           

        elif predicted_disease in ENT_specialist :
           consultdoctor = "ENT specialist"
           hospital = "Kathmandu_ENT_Hospital"
           remedy = "Home Remedies"
     
        elif predicted_disease in Orthopedist :
           consultdoctor = "Orthopedist"
           hospital = "Nepal_Orthopedic_Hospital"
           remedy = "Home Remedies"
     
        elif predicted_disease in Neurologist :
           consultdoctor = "Neurologist"
           hospital = "Neuro_Hospital"
           remedy = "Home Remedies"
     
        elif predicted_disease in Allergist_Immunologist :
           consultdoctor = "Allergist/Immunologist"
           hospital = "Grande_International_Hospital"
           remedy = "Home Remedies"

     
        elif predicted_disease in Urologist :
           consultdoctor = "Urologist"
           hospital = "Iwamura_Memorial_Hospital"
           remedy = "Home Remedies"
     
        elif predicted_disease in Dermatologist :
           consultdoctor = "Dermatologist"
           hospital="Alka_Cosmetic_Dermatology"
           remedy = "Home Remedies"
     
        elif predicted_disease in Gastroenterologist :
           consultdoctor = "Gastroenterologist"
           hospital= "Norvic_International_Hospital"
           remedy = "Home Remedies"
     
        else :
           consultdoctor = "other"
           hospital = "Bir_Hospital"
           remedy = "Home Remedies"


        request.session['doctortype'] = consultdoctor
        request.session['hospitaltype'] = hospital
        request.session['remedytype'] = remedy

        patientusername = request.session['patientusername']
        puser = User.objects.get(username=patientusername)



        #saving to database.....................

        patient = puser.patient
        diseasename = predicted_disease
        no_of_symp = inputno
        symptomsname = psymptoms
        confidence = confidencescore
       
        

        diseaseinfo_new = diseaseinfo(patient=patient,diseasename=diseasename,no_of_symp=no_of_symp,symptomsname=symptomsname,confidence=confidence,consultdoctor=consultdoctor)
        diseaseinfo_new.save()
        

        request.session['diseaseinfo_id'] = diseaseinfo_new.id

        print("disease record saved sucessfully.............................")

        return JsonResponse({'predicteddisease': predicted_disease ,'confidencescore':confidencescore , "consultdoctor": consultdoctor, "hospital":hospital, "remedy":remedy})
   

def pconsultation_history(request):

    if request.method == 'GET':

        patientusername = request.session['patientusername']
        puser = User.objects.get(username=patientusername)
        patient_obj = puser.patient

        consultationnew = consultation.objects.filter(patient=patient_obj)

        return render(request, 'patient/consultation_history/consultation_history.html', {"consultation": consultationnew})


def dconsultation_history(request):

    if request.method == 'GET':

        doctorusername = request.session['doctorusername']
        duser = User.objects.get(username=doctorusername)
        doctor_obj = duser.doctor

        consultationnew = consultation.objects.filter(doctor=doctor_obj)

        return render(request, 'doctor/consultation_history/consultation_history.html', {"consultation": consultationnew})


def doctor_ui(request):

    if request.method == 'GET':

        doctorid = request.session['doctorusername']
        duser = User.objects.get(username=doctorid)

        return render(request, 'doctor/doctor_ui/profile.html', {"duser": duser})


def dviewprofile(request, doctorusername):

    if request.method == 'GET':

        duser = User.objects.get(username=doctorusername)

        return render(request, 'doctor/view_profile/view_profile.html', {"duser": duser})


def consult_a_doctor(request):

    if request.method == 'GET':

        doctortype = request.session['doctortype']
        print(doctortype)
        dobj = doctor.objects.all()

        return render(request, 'patient/consult_a_doctor/consult_a_doctor.html', {"dobj":dobj})


def related_hospital(request):

    if request.method == 'GET':

        hospitaltype = request.session['hospitaltype']
        print(hospitaltype)
        hobj = Hospital.objects.all()
        

        return render(request, 'patient/consult_a_doctor/related_hospital.html', {"hobj": hobj})

def home_remedy(request, ):

    if request.method == 'GET':

        remedytype = request.session['remedytype']
        print(remedytype)
        robj = remedies.objects.all()
        

        return render(request, 'patient/consult_a_doctor/remedies.html', {"robj": robj})



def hospital(request, id):
    post = Hospital.objects.filter(remedy_id=id)[0]
    print(post)
    return render(request, 'homepage/viewhospital.html', {'post': post})


def remedy(request, id):
    rpost = remedies.objects.filter(hospital_id=id)[0]
    print(rpost)
    return render(request, 'homepage/viewremedy.html', {'rpost': rpost})        


def make_consultation(request, doctorusername):

    if request.method == 'POST':

        patientusername = request.session['patientusername']
        puser = User.objects.get(username=patientusername)
        patient_obj = puser.patient

        #doctorusername = request.session['doctorusername']
        duser = User.objects.get(username=doctorusername)
        doctor_obj = duser.doctor
        request.session['doctorusername'] = doctorusername

        diseaseinfo_id = request.session['diseaseinfo_id']
        diseaseinfo_obj = diseaseinfo.objects.get(id=diseaseinfo_id)

        consultation_date = date.today()
        status = "active"

        consultation_new = consultation(patient=patient_obj, doctor=doctor_obj, diseaseinfo=diseaseinfo_obj, consultation_date=consultation_date, status=status)
        consultation_new.save()

        request.session['consultation_id'] = consultation_new.id

        print("consultation record is saved sucessfully.............................")

        return redirect('consultationview', consultation_new.id)


def consultationview(request, consultation_id):

    if request.method == 'GET':

        request.session['consultation_id'] = consultation_id
        consultation_obj = consultation.objects.get(id=consultation_id)

        return render(request, 'consultation/consultation.html', {"consultation": consultation_obj})





# -----------------------------chatting system ---------------------------------------------------


def post(request):
    if request.method == "POST":
        msg = request.POST.get('msgbox', None)

        consultation_id = request.session['consultation_id']
        consultation_obj = consultation.objects.get(id=consultation_id)

        c = Chat(consultation_id=consultation_obj, sender=request.user, message=msg)

        if msg != '':
            c.save()
            print("msg saved" + msg)
            return JsonResponse({'msg': msg})
    else:
        return HttpResponse('Request must be POST.')


def chat_messages(request):
    if request.method == "GET":

        consultation_id = request.session['consultation_id']

        c = Chat.objects.filter(consultation_id=consultation_id)
        return render(request, 'consultation/chat_body.html', {'chat': c})


# -----------------------------chatting system ---------------------------------------------------
from .forms import appointmentform
from .models import appointment
#--------------appointment/feedback---------
def contact(request):
    if request.method == 'POST': 
        
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('service') and request.POST.get('time') and request.POST.get('note'):
            post = appointment()
            post.name = request.POST.get('name')
            post.email = request.POST.get('email')
            post.service = request.POST.get('service')
            post.time = request.POST.get('time')
            post.note = request.POST.get('note')
            post.save()
            return render(request, 'homepage/contact.html', {'post' : post})

    else:
        return render(request, 'homepage/contact.html')
    return render(request, "homepage/contact.html")
    

