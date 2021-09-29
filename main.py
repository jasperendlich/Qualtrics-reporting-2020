# Starting off with libraries
import pandas as pd
import numpy as np
import os
import warnings
from datetime import date
from datetime import datetime
import reporting
# import functions
import survey_versions


pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', None)

warnings.filterwarnings('ignore')

# Delete output map first, to create a clean slate
os.makedirs('output', exist_ok=True)

today = date.today()

date = today.strftime('%B+%d,+%Y')
other_date = today.strftime('%Y%m%d')


# Start defining the type of report we want to have
def edx_pre(course_id, course_run):
    os.makedirs('output', exist_ok=True)

    filename = '2021T1_General_survey_pre_' + date + '.csv'
    db = pd.read_csv(filename)
    course_code = course_id + ' ' + course_run

    db['course_code'] = db['course_code'].replace(np.nan, 'Unknown')
    db = db[db['course_code'].str.contains(course_code)]
    size = len(db)

    if db.empty is False:
        # Making the resource and name queue
        resource_queue = []
        name_queue = []

        # Split up verified and audit
        db = db[db['Q2.3.2'].notnull()]
        audit = db[db['Q2.3.2'].str.contains('Audit')]
        verified = db[db['Q2.3.2'].str.contains('Verified')]

        if size < 5:
            print(course_code + ' has < 5 results, so only specific results are printed')

            survey_versions.low_results_edx_pre(course_id, db, audit, verified, resource_queue, name_queue)

        elif 5 >= size < 20:
            print(course_code + ' has between 5 and 20 results, small data protocol should be applied \n')
            print('The small data protocol is still being created for Python, coming soon \n')

            print('Pre-survey of ', course_code + ' is being created \n')

            survey_versions.low_results_edx_pre(course_id, db, audit, verified, resource_queue, name_queue)

        else:
            print('Pre-survey of ', course_code + ' is being created \n')

            survey_versions.normal_edx_pre(course_id, db, audit, verified, resource_queue, name_queue)

        name_dict = dict(zip(resource_queue, name_queue))

        reporting.HTMLDocument(other_date + ' Pre-survey results ' + course_code, resource_queue, name_dict)

        db[['Progress', 'Duration (in seconds)']] = db[['Progress', 'Duration (in seconds)']].apply(pd.to_numeric)
        print('\n Progress check: We would lose ', db['Progress'][db['Progress'] < 50].count(), 'values out of ', len(db))
        print('Duration check: We would lose ', db['Duration (in seconds)'][db['Duration (in seconds)'] < 60].count(), 'values out of ', len(db))
        print('Enrollment check: We would lose ', (size - len(audit) - len(verified)), 'values out of', len(db), '\n')

    else:
        print('\n', course_code, 'has no responses (yet)!')

    print('------------------------------------- \n')


def profed_pre(course_id, course_run):
    os.makedirs('output', exist_ok=True)

    filename = '2021T1_General_survey_pre_' + date + '.csv'
    db = pd.read_csv(filename)
    course_code = course_id + ' ' + course_run

    db['course_code'] = db['course_code'].replace(np.nan, 'Unknown')
    db = db[db['course_code'].str.contains(course_code)]
    size = len(db)

    if db.empty is False:
        # Making the resource and name queue
        resource_queue = []
        name_queue = []

        if size < 5:
            print(course_code + ' has < 5 results, so only specific results are printed')

            survey_versions.low_results_profed_pre(course_id, db, resource_queue, name_queue)

        elif 5 >= size < 20:
            print(course_code + ' has between 5 and 20 results, small data protocol should be applied \n')
            print('The small data protocol is still being created for Python, coming soon \n')

            print('Pre-survey of ', course_code + ' is being created \n')

            survey_versions.low_results_profed_pre(course_id, db, resource_queue, name_queue)

        else:
            print('Pre-survey of ', course_code + ' is being created \n')

            survey_versions.normal_profed_pre(course_id, db, resource_queue, name_queue)

        name_dict = dict(zip(resource_queue, name_queue))

        reporting.HTMLDocument(other_date + ' Pre-survey results ' + course_code, resource_queue, name_dict)

        db[['Progress', 'Duration (in seconds)']] = db[['Progress', 'Duration (in seconds)']].apply(pd.to_numeric)
        print('\n Progress check: We would lose ', db['Progress'][db['Progress'] < 50].count(), 'values out of ', len(db))
        print('Duration check: We would lose ', db['Duration (in seconds)'][db['Duration (in seconds)'] < 60].count(), 'values out of ', len(db))

    else:
        print('\n', course_code, 'has no responses (yet)!')

    print('------------------------------------- \n')


def edx_post(course_id, course_run):
    os.makedirs('output', exist_ok=True)

    filename = '2021T1_General_survey_post_' + date + '.csv'
    db = pd.read_csv(filename)
    course_code = course_id + ' ' + course_run

    db['course_code'] = db['course_code'].replace(np.nan, 'Unknown')
    db = db[db['course_code'].str.contains(course_code)]
    size = len(db)

    if db.empty is False:
        # Making the resource and name queue
        resource_queue = []
        name_queue = []

        # Split up verified and audit
        db = db[db['Q202'].notnull()]
        audit = db[db['Q202'].str.contains('Audit')]
        verified = db[db['Q202'].str.contains('Verified')]

        if size < 5:
            print(course_code + ' has < 5 results, so only specific results are printed')

            survey_versions.low_results_edx_post(course_id, db, audit, verified, resource_queue, name_queue)

        elif 5 >= size < 20:
            print(course_code + ' has between 5 and 20 results, small data protocol should be applied \n')
            print('The small data protocol is still being created for Python, coming soon \n')

            print('Post-survey of ', course_code + ' is being created \n')

            survey_versions.low_results_edx_post(course_id, db, audit, verified, resource_queue, name_queue)

        else:
            print('Post-survey of ', course_code + ' is being created \n')

            survey_versions.normal_edx_post(course_id, db, audit, verified, resource_queue, name_queue)

        name_dict = dict(zip(resource_queue, name_queue))

        reporting.HTMLDocument(other_date + ' Post-survey results ' + course_code, resource_queue, name_dict)

        db[['Progress', 'Duration (in seconds)']] = db[['Progress', 'Duration (in seconds)']].apply(pd.to_numeric)
        print('\n Progress check: We would lose ', db['Progress'][db['Progress'] < 50].count(), 'values out of ', len(db))
        print('Duration check: We would lose ', db['Duration (in seconds)'][db['Duration (in seconds)'] < 60].count(), 'values out of ', len(db))
        print('Enrollment check: We would lose ', (size - len(audit) - len(verified)), 'values out of', len(db), '\n')

    else:
        print('\n', course_code, 'has no responses (yet)!')

    print('------------------------------------- \n')


def profed_post(course_id, course_run):
    os.makedirs('output', exist_ok=True)

    filename = '2021T1_General_survey_post_' + date + '.csv'
    db = pd.read_csv(filename)
    course_code = course_id + ' ' + course_run

    db['course_code'] = db['course_code'].replace(np.nan, 'Unknown')
    db = db[db['course_code'].str.contains(course_code)]
    size = len(db)

    if db.empty is False:
        # Making the resource and name queue
        resource_queue = []
        name_queue = []

        if size < 5:
            print(course_code + ' has < 5 results, so only specific results are printed')

            survey_versions.low_results_profed_post(course_id, db, resource_queue, name_queue)

        elif 5 >= size < 20:
            print(course_code + ' has between 5 and 20 results, small data protocol should be applied \n')
            print('The small data protocol is still being created for Python, coming soon \n')

            print('Post-survey of ', course_code + ' is being created \n')

            survey_versions.low_results_profed_post(course_id, db, resource_queue, name_queue)

        else:
            print('Post-survey of ', course_code + ' is being created \n')

            survey_versions.normal_profed_post(course_id, db, resource_queue, name_queue)

        name_dict = dict(zip(resource_queue, name_queue))

        reporting.HTMLDocument(other_date + ' Post-survey results ' + course_code, resource_queue, name_dict)

        db[['Progress', 'Duration (in seconds)']] = db[['Progress', 'Duration (in seconds)']].apply(pd.to_numeric)
        print('\n Progress check: We would lose ', db['Progress'][db['Progress'] < 50].count(), 'values out of ', len(db))
        print('Duration check: We would lose ', db['Duration (in seconds)'][db['Duration (in seconds)'] < 60].count(), 'values out of ', len(db))

    else:
        print('\n', course_code, 'has no responses (yet)!')

    print('------------------------------------- \n')


# To-do
survey_list = pd.read_excel('Survey links 2021.xlsx', header=1)
to_do_list = survey_list[['Course_code', 'Code', 'Start date', 'End date', 'Platform', 'Delivery method', 'Pre-survey course status', 'Post-survey course status']]

# Drop all the empty rows
to_do_list = to_do_list[to_do_list['Code'].notna()]
# Drop all the rows at TUD online courses
to_do_list = to_do_list[to_do_list['Platform'].isin(['edX', 'ProfEd'])]
# Drop rows where the course_code is missing
to_do_list = to_do_list[to_do_list['Course_code'].notna()]


def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return (d1 - d2).days


for index, row in to_do_list.iterrows():
    if 'Ready' in row['Pre-survey course status']:
        print(row['Code'], row['Course_code'].split('+')[-1], 'is being checked')
        print('Number of days after start: ', days_between(today.strftime('%Y-%m-%d'), row['Start date'].strftime('%Y-%m-%d')), '\n')
        if 'Instructor-paced' in row['Delivery method'] and days_between(today.strftime('%Y-%m-%d'), row['Start date'].strftime('%Y-%m-%d')) >= 14:
            if 'edX' in row['Platform']:
                edx_pre(row['Code'], row['Course_code'].split('+')[-1])
            if 'ProfEd' in row['Platform']:
                profed_pre(row['Code'], row['Course_code'].split('+')[-1])
            continue
        if 'Self-paced' in row['Delivery method'] and days_between(today.strftime('%Y-%m-%d'), row['Start date'].strftime('%Y-%m-%d')) >= 30:
            if 'edX' in row['Platform']:
                edx_pre(row['Code'], row['Course_code'].split('+')[-1])
            if 'ProfEd' in row['Platform']:
                profed_pre(row['Code'], row['Course_code'].split('+')[-1])
            else:
                print('Weird course type')
            continue
        else:
            print('Not long enough after start date to create the report')
            print('-------------------------------------------------- \n')


for index, row in to_do_list.iterrows():
    if 'Ready' in row['Post-survey course status']:
        print(row['Code'], row['Course_code'].split('+')[-1], 'is being checked')
        print('Number of days after end: ', days_between(today.strftime('%Y-%m-%d'), row['Start date'].strftime('%Y-%m-%d')), '\n')
        if 'Instructor-paced' in row['Delivery method'] and days_between(today.strftime('%Y-%m-%d'), row['End date'].strftime('%Y-%m-%d')) >= 14:
            if 'edX' in row['Platform']:
                edx_post(row['Code'], row['Course_code'].split('+')[-1])
            if 'ProfEd' in row['Platform']:
                profed_post(row['Code'], row['Course_code'].split('+')[-1])
            continue
        if 'Self-paced' in row['Delivery method'] and days_between(today.strftime('%Y-%m-%d'), row['End date'].strftime('%Y-%m-%d')) >= 14:
            if 'edX' in row['Platform']:
                edx_post(row['Code'], row['Course_code'].split('+')[-1])
            if 'ProfEd' in row['Platform']:
                profed_post(row['Code'], row['Course_code'].split('+')[-1])
            else:
                print('Weird course type')
            continue
        else:
            print('Not long enough after end date to create the report')
            print('------------------------------------------------ \n')

    else:
        print('Surveys are not yet deployed!')
