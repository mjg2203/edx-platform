"""
Instructor Dashboard API views

Non-html views which the instructor dashboard requests.

TODO add tracking
"""

import csv
import json
import logging
import os
import re
import requests
from django_future.csrf import ensure_csrf_cookie
from django.views.decorators.cache import cache_control
from mitxmako.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.utils.html import escape
from django.http import HttpResponse, HttpResponseBadRequest

from django.conf import settings
from courseware.access import has_access, get_access_group_name, course_beta_test_group_name
from courseware.courses import get_course_with_access
from django_comment_client.utils import has_forum_access
from instructor.offline_gradecalc import student_grades, offline_grades_available
from django_comment_common.models import Role, FORUM_ROLE_ADMINISTRATOR, FORUM_ROLE_MODERATOR, FORUM_ROLE_COMMUNITY_TA
from xmodule.modulestore.django import modulestore
from student.models import CourseEnrollment
from django.contrib.auth.models import User

import analytics.basic
import analytics.distributions


@ensure_csrf_cookie
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def grading_config(request, course_id):
    """
    Respond with json which contains a html formatted grade summary.

    TODO maybe this shouldn't be html already
    """
    course = get_course_with_access(request.user, course_id, 'staff', depth=None)
    grading_config_summary = analytics.basic.dump_grading_context(course)

    response_payload = {
        'course_id': course_id,
        'grading_config_summary': grading_config_summary,
    }
    response = HttpResponse(json.dumps(response_payload), content_type="application/json")
    return response


@ensure_csrf_cookie
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def enrolled_students_profiles(request, course_id):
    """
    Respond with json which contains a summary of all enrolled students profile information.

    Response {"students": [{-student-info-}, ...]}

    TODO respond to csv requests as well
    TODO accept requests for different attribute sets
    """

    # enrollments = CourseEnrollment.objects.filter(course_id=course_id)
    # students = [enrollment.user for enrollment in enrollments]
    students = User.objects.filter(courseenrollment__course_id=course_id)

    STUDENT_FEATURES = ['username', 'first_name', 'last_name', 'is_staff', 'email']
    PROFILE_FEATURES = ['year_of_birth', 'gender', 'level_of_education']

    def extract_student(student):
        student_dict = dict((feature, getattr(student, feature)) for feature in STUDENT_FEATURES)
        profile = student.profile
        profile_dict = dict((feature, getattr(profile, feature)) for feature in PROFILE_FEATURES)
        student_dict.update(profile_dict)
        return student_dict

    available_features = analytics.basic.AVAILABLE_STUDENT_FEATURES + analytics.basic.AVAILABLE_PROFILE_FEATURES

    response_payload = {
        'course_id':          course_id,
        'students':           analytics.basic.enrolled_students_profiles(course_id, available_features),
        'students_count':     students.count(),
        'available_features': available_features
    }
    response = HttpResponse(json.dumps(response_payload), content_type="application/json")
    return response


@ensure_csrf_cookie
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def profile_distribution(request, course_id):
    """
    Respond with json of the distribution of students over selected fields which have choices.

    Ask for features through the 'features' query parameter.
    The features query parameter can be either a single feature name, or a json string of feature names.
    e.g.
        http://localhost:8000/courses/MITx/6.002x/2013_Spring/instructor_dashboard/api/profile_distribution?features=level_of_education
        http://localhost:8000/courses/MITx/6.002x/2013_Spring/instructor_dashboard/api/profile_distribution?features=%5B%22year_of_birth%22%2C%22gender%22%5D

    Example js query:
    $.get("http://localhost:8000/courses/MITx/6.002x/2013_Spring/instructor_dashboard/api/profile_distribution",
          {'features': JSON.stringify(['year_of_birth', 'gender'])},
          function(){console.log(arguments[0])})

    TODO how should query parameter interpretation work?
    TODO respond to csv requests as well
    """

    try:
        features = json.loads(request.GET.get('features'))
    except Exception:
        features = [request.GET.get('features')]

    feature_results = {}

    for feature in features:
        try:
            feature_results[feature] = analytics.distributions.profile_distribution(course_id, feature)
        except Exception as e:
            feature_results[feature] = {'error': "can not find distribution for '%s'" % feature}
            raise e

    response_payload = {
        'course_id':          course_id,
        'queried_features':   features,
        'available_features': ['gender', 'level_of_education', 'year_of_birth'],
        'display_names':      {
            'gender': 'Gender',
            'level_of_education': 'Level of Education',
            'year_of_birth': 'Year Of Birth',
        },
        'feature_results':    feature_results,
    }
    response = HttpResponse(json.dumps(response_payload), content_type="application/json")
    return response
