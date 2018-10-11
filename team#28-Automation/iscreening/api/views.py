import pyrebase
from django.shortcuts import render
from rest_framework.response import Response
from cv_parser import cv_parser
from cv_scorer import get_cv_dict, get_cv_score

config = {
	'apiKey': "AIzaSyB0Il0NLQPxxDyMgoE0fOMd4pYUkbkZVvI",
	'authDomain': "cpanel-5e873.firebaseapp.com",
    'databaseURL': "https://cpanel-5e873.firebaseio.com",
    'projectId': "cpanel-5e873",
    'storageBucket': "cpanel-5e873.appspot.com",
    'messagingSenderId': "579985583952"
    }

firebase = pyrebase.initialize_app(config)
database = firebase.database()

def cv_score_getter(request, form_id, uid):
    static_fields = ['total_experience', 'highest_degree', 'resume_context', 'current_company_name', 'current_project_summary']
    dynamic_fields = ['skills_set', 'previous_company_name', 'previous_designation', 'previous_project_summmary', 'previous_degree', 'previous_education_description']
    university_dict = {"Carnegie Mellon University": '0.9', "Princeton University": '0.91',
                       "Harvard University": '0.92', "Yale University": '0.79', "Columbia University": '0.89',
                       "Stanford University": '0.85', "Massachusetts Institute of Technology": '0.89',
                       "University of Pennsylvania": '0.72', "California Institute of Technology": '0.81',
                       "Johns Hopkins University": '0.68', "Dartmouth College": '0.75', "Northwestern University": '0.64',
                       "Brown University": '0.52', "Cornell University": '0.79', "Georgetown University": '0.44',
                       "IIT Bombay": '0.42', "IIT Madras": '0.46', "IISC Bangalore": '0.69',
                       "IIIT Vadodara": '0.41', "ISI Kolkata": '0.65'}

    company_dict = {"Google": '0.95', "Facebook": '0.93', "Amazon": '0.90', "Intel": '0.85',
                "Goldman Sachs": '0.86', "IBM": '0.82', "Mathworks": '0.60', "Microsoft": '0.92',
                "Hapramp": '0.55', "Neurala": '0.45', "Soma Analytics": '0.42', "Innoplexus": '0.62',
                "CERN": '0.97', "NASA": '0.75', "ISRO": '0.83', "Fossasia": '0.72',
                "Haskell": '0.71', "Bash.ai": '0.66', "Chase": '0.35', "Tesla": '0.78'}
    degree_dict = {"Bachelor"}
    required_skills = request.tags
    form = database.reference('forms/{0}'.format(form_id)).get()
    cv =  form.reference('users/{0}'.format(uid)).get()
    cv_parser(cv)
    cv_dict = get_cv_dict(cv, static_fields, dynamic_fields)
    cv_score = get_cv_score(cv_dict, university_dict, company_dict, degree_dict, required_skills)
    return Response({'cv_score': cv_score}, status=200)

def get_behavior_score(request, form_id, uid):
    form = database.reference('forms/{0}'.format(form_id)).get()
    user_obj =  form.reference('users/{0}'.format(uid)).get()

    pass