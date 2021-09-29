import functions
import pandas as pd

program_db = pd.read_csv('Overview of program courses.csv')
program_courses = program_db['CourseID'].unique()


def normal_edx_pre(course_id, db, audit, verified, resource_queue, name_queue):
    # Program expectations block
    # -----------------------------------------
    if course_id in program_courses:
        if len(db['Q179'][2:].dropna()) >= 5:
            functions.program_expectations(db, resource_queue, name_queue)
        else:
            functions.no_results_file(resource_queue, name_queue)

    # Reasons & motivation block
    # -----------------------------------------
    # Q2.1 - How did you discover this course?
    functions.bar_chart(db, 'Q2.1', resource_queue, name_queue, 'Q2.1 - How did you discover this course?')
    functions.standard_table(db, audit, verified, 'Q2.1', resource_queue, name_queue, 'Table')
    # Q2.1_7 - Social media part
    if len(db['Q2.1_7_TEXT'][2:].dropna()) >= 5:
        functions.bar_chart(db, 'Q2.1_7_TEXT', resource_queue, name_queue, 'Which social media')
        functions.standard_table(db, audit, verified, 'Q2.1_7_TEXT', resource_queue, name_queue, 'Table')
    # Q2.1_8 - Other
    functions.other_list(audit, verified, 'Q2.1_8_TEXT', resource_queue, name_queue, 'Other')

    # Q2.2 - Were you actively looking for a course before enrolling in this course?
    functions.bar_chart(db, 'Q2.2', resource_queue, name_queue, 'Q2.2 - Were you actively looking for a course before enrolling in this course?')
    functions.standard_table(db, audit, verified, 'Q2.2', resource_queue, name_queue, 'Table')

    # Q2.2.1 - What type of course were you initially looking for?
    functions.bar_chart(db, 'Q2.2.1', resource_queue, name_queue, 'Q2.2.1 - What type of course were you initially looking for?')
    functions.standard_table(db, audit, verified, 'Q2.2.1', resource_queue, name_queue, 'Table')

    # Q186 - Which of the following options best describes your experience with online courses?
    functions.bar_chart(db, 'Q186', resource_queue, name_queue, 'Q186 - Which of the following options best describes your experience with online courses?')
    functions.standard_table(db, audit, verified, 'Q186', resource_queue, name_queue, 'Table')

    # Q2.3 - What best describes your motivation for enrolling in this course? My motivation is
    functions.bar_chart(db, 'Q2.3', resource_queue, name_queue, 'Q2.3 - What best describes your motivation for enrolling in this course? My motivation is')
    functions.standard_table(db, audit, verified, 'Q2.3', resource_queue, name_queue, 'Table')
    functions.other_list(audit, verified, 'Q2.3_5_TEXT', resource_queue, name_queue, 'Other')

    # Q2.3.1 - Could you elaborate on your reasons for taking this course?
    functions.other_list(audit, verified, 'Q2.3.1', resource_queue, name_queue, 'Q2.3.1 - Could you elaborate on your reasons for taking this course?')

    # Q2.3.2 - What is your current type of enrollment in the course?
    functions.bar_chart(db, 'Q2.3.2', resource_queue, name_queue, 'Q2.3.2 - What is your current type of enrollment in the course?')
    functions.count(db, 'Q2.3.2', resource_queue, name_queue, 'Table')

    # Q178 - Why did you enroll in the verified track?
    functions.normal_list(db, 'Q178', resource_queue, name_queue, 'Q178 - Why did you enroll in the verified track?')

    # Q2.4 - How important were the following factors in your decision to enrol in this course?
    functions.stacked_bar_pre(db, 'Q2.4', 'Q2.4_1', 'Q2.4_7', resource_queue, name_queue,
                              'Q2.4 - How important were the following factors in your decision to enrol in this course?')
    functions.categories(db, audit, verified, 'Q2.4', 'Q2.4_1', 'Q2.4_21', ['Uniqueness of this course', 'Potential usefulness of this course', 'Interesting topic of this course',
                                                                            'Lecturer(s) involved with this course', 'University(ies) involved with this course',
                                                                            'That the course is offered online', 'The possibility to receive a certificate or credentials',
                                                                            'Time and effort required to complete the course', 'Price of the certificate',
                                                                            'The level of content suits me', 'The opportunity to interact with likeminded people'],
                         resource_queue, name_queue, 'Table')

    # Expectations block
    # -----------------------------------------
    # Q3.1 - What do you think might be the biggest challenge in completing this course for you?
    functions.bar_chart(db, 'Q3.1', resource_queue, name_queue, 'Q3.1 - What do you think might be the biggest challenge in completing this course for you?')
    functions.standard_table(db, audit, verified, 'Q3.1', resource_queue, name_queue, 'Table')
    functions.other_list(audit, verified, 'Q3.1_5_TEXT', resource_queue, name_queue, 'Other')

    # Q3.2 - How important are the following elements for you in this course?
    functions.stacked_bar_pre(db, 'Q3.2', 'Q108_1', 'Q108_4', resource_queue, name_queue, 'Q3.2 - How important are the following elements for you in this course?')
    functions.categories(db, audit, verified, 'Q3.2', 'Q108_1', 'Q108_4', ['Uniqueness of this course',
                                                                           'Potential usefulness of this course',
                                                                           'Interesting topic of this course',
                                                                           'Lecturer(s) involved with this course'], resource_queue, name_queue, 'Table')

    # Q3.2.2 - How important are the following elements for you in this course?
    functions.stacked_bar_pre(db, 'Q3.2.2', 'Q3.2_5', 'Q3.2_7', resource_queue, name_queue, 'Q3.2.2 - How important are the following elements for you in this course?')
    functions.categories(db, audit, verified, 'Q3.2.2', 'Q3.2_5', 'Q3.2_7', ['Group work (if applicable)',
                                                                             'Feedback by instructors (if applicable)',
                                                                             'Possibility to work on your own project (if applicable)'], resource_queue, name_queue, 'Table')

    # Q3.3 - On average, how many hours per week can you dedicate to this course?
    functions.standard_statistics_mooc(db, audit, verified, 'Q3.3_1', resource_queue, name_queue, 'Q3.3 - On average, how many hours per week can you dedicate to this course?')

    # Demographics block
    # -----------------------------------------
    # Q4.1 - Which of the following options best describes your familiarity with the organization?
    if 'AMS.URB' not in course_id:
        functions.bar_chart(db, 'Q4.1', resource_queue, name_queue, 'Q4.1 - Which best describes your familiarity with TU Delft (Delft University of Technology)?')
        functions.standard_table(db, audit, verified, 'Q4.1', resource_queue, name_queue, 'Table')
    else:
        functions.bar_chart(db, 'Q4.1_AMS_1', resource_queue, name_queue, 'Q4.1 - Which of the following options best describes your familiarity with the following '
                                                                          'organisations? - Delft University of Technology')
        functions.standard_table(db, audit, verified, 'Q4.1_AMS_1', resource_queue, name_queue, 'Table')
        functions.bar_chart(db, 'Q4.1_AMS_2', resource_queue, name_queue, 'Q4.1 - Which of the following options best describes your familiarity with the following '
                                                                          'organisations? - Wageningen University & Research')
        functions.standard_table(db, audit, verified, 'Q4.1_AMS_2', resource_queue, name_queue, 'Table')
        functions.bar_chart(db, 'Q4.1_AMS_3', resource_queue, name_queue, 'Q4.1 - Which of the following options best describes your familiarity with the following '
                                                                          'organisations? - AMS Institute')
        functions.standard_table(db, audit, verified, 'Q4.1_AMS_3', resource_queue, name_queue, 'Table')

    # Q4.2 - Which of the following best describes your current situation?
    functions.bar_chart(db, 'Q4.2', resource_queue, name_queue, 'Q4.2 - Which of the following best describes your current situation?')
    functions.standard_table(db, audit, verified, 'Q4.2', resource_queue, name_queue, 'Q4.2 - Which of the following best describes your current situation?')
    functions.other_list(audit, verified, 'Q4.2_7_TEXT', resource_queue, name_queue, 'Other')

    # Q4.2.1 - Which of the following best describes your job field?
    functions.bar_chart(db, 'Q4.2.1', resource_queue, name_queue, 'Q4.2.1 - Which of the following best describes your job field?')
    functions.standard_table(db, audit, verified, 'Q4.2.1', resource_queue, name_queue, 'Table')

    # Q4.2.2 - What is your current job title?
    functions.normal_list(db, 'Q4.2.2', resource_queue, name_queue, 'Q4.2.2 - What is your current job title?')

    # Q4.2.3 - What is your educational background? (e.g. I have a Bachelor's degree in ... / MSc in ... / training on ...)
    functions.split_education(db, 'Q4.2.3', resource_queue, name_queue,
                              'Q4.2.3 - What is your educational background? (e.g. I have a Bachelors degree in ... / MSc in ... / training on ...)')

    # Q4.2.4 - In which industry do you currently work?
    functions.standard_table(db, audit, verified, 'Q4.2.4_1', resource_queue, name_queue, 'Q4.2.4 - In which industry do you currently work? - Sector')
    functions.standard_table(db, audit, verified, 'Q4.2.4_2', resource_queue, name_queue, 'Q4.2.4 - In which industry do you currently work? - Industry')

    # Q4.3 - What is your age?
    functions.standard_statistics_mooc(db, audit, verified, 'Q4.3_1', resource_queue, name_queue, 'Q4.3 - What is your age?')

    # Q4.4 - What is your gender?
    functions.bar_chart(db, 'Q4.4', resource_queue, name_queue, 'Q4.4 - What is your gender?')
    functions.standard_table(db, audit, verified, 'Q4.4', resource_queue, name_queue, 'Table')

    # Q4.5 - What is your (first) nationality? Please select the corresponding country.
    functions.standard_table(db, audit, verified, 'Q4.5_1', resource_queue, name_queue, 'Q4.5 - What is your (first) nationality? Please select the corresponding country. - '
                                                                                        'Continent')
    functions.standard_table(db, audit, verified, 'Q4.5_2', resource_queue, name_queue, 'Q4.5 - What is your (first) nationality? Please select the corresponding country. - '
                                                                                        'Country')

    # Q4.6 - What is the highest degree or level of education you have completed?
    functions.bar_chart(db, 'Q4.6', resource_queue, name_queue, 'Q4.6 - What is the highest degree or level of education you have completed?')
    functions.standard_table(db, audit, verified, 'Q4.6', resource_queue, name_queue, 'Table')
    functions.other_list(audit, verified, 'Q4.6_9_TEXT', resource_queue, name_queue, 'Other')

    # Course specific blocks are displayed below block
    # -----------------------------------------
    # ScratchTENGx course specific
    if 'ScratchTENGx' in course_id:
        # Q165 - What do you intend students to learn about Scratch programming?
        functions.normal_list(db, 'Q165', resource_queue, name_queue, 'Q165 - What do you intend students to learn about Scratch programming?')

        # Q166 - Why is it important for the students to learn this?
        functions.normal_list(db, 'Q166', resource_queue, name_queue, 'Q166 - Why is it important for the students to learn this?')

        # Q167 - What do you know about students’ thinking (prior knowledge, learning difficulties) that influences your teaching of Scratch programming?
        functions.normal_list(db, 'Q167', resource_queue, name_queue, 'Q167 - What do you know about students’ thinking (prior knowledge, '
                                                                      'learning difficulties) that influences your teaching of Scratch programming?')

        # Q168 - What do you think is a suitable method for teaching Scratch programming?
        functions.normal_list(db, 'Q168', resource_queue, name_queue, 'Q168 - What do you think is a suitable method for teaching Scratch programming?')

        # Q169 - What are your particular reasons for choosing this method?
        functions.normal_list(db, 'Q169', resource_queue, name_queue, 'Q169 - What are your particular reasons for choosing this method?')

        # Q170 - What would be a suitable way of assessing students’ understanding or confusion around Scratch programming?
        functions.normal_list(db, 'Q170', resource_queue, name_queue, 'Q170 - What would be a suitable way of assessing students’ '
                                                                      'understanding or confusion around Scratch programming?')

        # Q171 - What are your reasons for choosing this particular way of assessment?
        functions.normal_list(db, 'Q171', resource_queue, name_queue, 'Q171 - What are your reasons for choosing this particular way of assessment?')


def low_results_edx_pre(course_id, db, audit, verified, resource_queue, name_queue):
    # Program expectations block
    # -----------------------------------------
    if course_id in program_courses:
        if len(db['Q179'][2:].dropna()) >= 10:
            functions.program_expectations(db, resource_queue, name_queue)
        else:
            functions.no_results_file(resource_queue, name_queue)

    # Reasons & motivation block
    # -----------------------------------------
    # Q2.1 - How did you discover this course?
    functions.standard_table(db, audit, verified, 'Q2.1', resource_queue, name_queue, 'Q2.1 - How did you discover this course?')
    # Q2.1_7 - Social media part
    functions.standard_table(db, audit, verified, 'Q2.1_7_TEXT', resource_queue, name_queue, 'Which social media?')
    # Q2.1_8 - Other
    functions.other_list(audit, verified, 'Q2.1_8_TEXT', resource_queue, name_queue, 'Other')

    # Q2.2 - Were you actively looking for a course before enrolling in this course?
    functions.standard_table(db, audit, verified, 'Q2.2', resource_queue, name_queue, 'Q2.2 - Were you actively looking for a course before enrolling in this course?')

    # Q2.2.1 - What type of course were you initially looking for?
    functions.standard_table(db, audit, verified, 'Q2.2.1', resource_queue, name_queue, 'Q2.2.1 - What type of course were you initially looking for?')

    # Q186 - Which of the following options best describes your experience with online courses?
    functions.standard_table(db, audit, verified, 'Q186', resource_queue, name_queue, 'Q186 - Which of the following options best describes your experience with online courses?')

    # Q2.3 - What best describes your motivation for enrolling in this course? My motivation is
    functions.standard_table(db, audit, verified, 'Q2.3', resource_queue, name_queue, 'Q2.3 - What best describes your motivation for enrolling in this course? My motivation is')
    functions.other_list(audit, verified, 'Q2.3_5_TEXT', resource_queue, name_queue, 'Other')

    # Q2.3.1 - Could you elaborate on your reasons for taking this course?
    functions.other_list(audit, verified, 'Q2.3.1', resource_queue, name_queue, 'Q2.3.1 - Could you elaborate on your reasons for taking this course?')

    # Q2.3.2 - What is your current type of enrollment in the course?
    functions.count(db, 'Q2.3.2', resource_queue, name_queue, 'Q2.3.2 - What is your current type of enrollment in the course?')

    # Q178 - Why did you enroll in the verified track?
    functions.normal_list(db, 'Q178', resource_queue, name_queue, 'Q178 - Why did you enroll in the verified track?')

    # Q2.4 - How important were the following factors in your decision to enrol in this course?
    # functions.categories(db, audit, verified, 'Q2.4', 'Q2.4_1', 'Q2.4_21', ['Uniqueness of this course', 'Potential usefulness of this course', 'Interesting topic of this course',
    #                                                                         'Lecturer(s) involved with this course', 'University(ies) involved with this course',
    #                                                                         'That the course is offered online', 'The possibility to receive a certificate or credentials',
    #                                                                         'Time and effort required to complete the course', 'Price of the certificate',
    #                                                                         'The level of content suits me', 'The opportunity to interact with likeminded people'],
    #                      resource_queue, name_queue, 'Q2.4 - How important were the following factors in your decision to enrol in this course?')

    # Expectations block
    # -----------------------------------------
    # Q3.1 - What do you think might be the biggest challenge in completing this course for you?
    functions.standard_table(db, audit, verified, 'Q3.1', resource_queue, name_queue, 'Q3.1 - What do you think might be the biggest challenge in completing this course for you?')
    functions.other_list(audit, verified, 'Q3.1_5_TEXT', resource_queue, name_queue, 'Other')

    # Q3.2 - How important are the following elements for you in this course?
    # functions.categories(db, audit, verified, 'Q3.2', 'Q108_1', 'Q108_4', ['Uniqueness of this course',
    #                                                                        'Potential usefulness of this course',
    #                                                                        'Interesting topic of this course',
    #                                                                        'Lecturer(s) involved with this course'], resource_queue, name_queue,
    #                      'Q3.2 - How important are the following elements for you in this course?')

    # Q3.2.2 - How important are the following elements for you in this course?
    # functions.categories(db, audit, verified, 'Q3.2', 'Q3.2_5', 'Q3.2_7', ['Group work (if applicable)',
    #                                                                        'Feedback by instructors (if applicable)',
    #                                                                        'Possibility to work on your own project (if applicable)'], resource_queue, name_queue,
    #                      'Q3.2.2 - How important are the following elements for you in this course?')

    # Q3.3 - On average, how many hours per week can you dedicate to this course?
    functions.standard_statistics_mooc(db, audit, verified, 'Q3.3_1', resource_queue, name_queue, 'Q3.3 - On average, how many hours per week can you dedicate to this course?')

    # Demographics block
    # -----------------------------------------
    # Q4.1 - Which of the following options best describes your familiarity with the organization?
    if 'AMS.URB' not in course_id:
        functions.standard_table(db, audit, verified, 'Q4.1', resource_queue, name_queue, 'Q4.1 - Which best describes your familiarity with TU Delft (Delft University of '
                                                                                          'Technology)?')
    else:
        functions.standard_table(db, audit, verified, 'Q4.1 AMS_1', resource_queue, name_queue, 'Q4.1 - Which of the following options best describes your familiarity with the '
                                                                                                'following organisations? - Delft University of Technology')
        functions.standard_table(db, audit, verified, 'Q4.1 AMS_2', resource_queue, name_queue, 'Q4.1 - Which of the following options best describes your familiarity with the '
                                                                                                'following organisations? - Wageningen University & Research')
        functions.standard_table(db, audit, verified, 'Q4.1 AMS_3', resource_queue, name_queue, 'Q4.1 - Which of the following options best describes your familiarity with the '
                                                                                                'following organisations? - AMS Institute')

    # Q4.2 - Which of the following best describes your current situation?
    functions.standard_table(db, audit, verified, 'Q4.2', resource_queue, name_queue, 'Q4.2 - Which of the following best describes your current situation?')
    functions.other_list(audit, verified, 'Q4.2_7_TEXT', resource_queue, name_queue, 'Other')

    # Q4.2.1 - Which of the following best describes your job field?
    functions.standard_table(db, audit, verified, 'Q4.2.1', resource_queue, name_queue, 'Q4.2.1 - Which of the following best describes your job field?')

    # Q4.2.2 - What is your current job title?
    functions.normal_list(db, 'Q4.2.2', resource_queue, name_queue, 'Q4.2.2 - What is your current job title?')

    # Q4.2.3 - What is your educational background? (e.g. I have a Bachelor's degree in ... / MSc in ... / training on ...)
    functions.split_education(db, 'Q4.2.3', resource_queue, name_queue,
                              'Q4.2.3 - What is your educational background? (e.g. I have a Bachelors degree in ... / MSc in ... / training on ...)')

    # Q4.2.4 - In which industry do you currently work?
    functions.standard_table(db, audit, verified, 'Q4.2.4_1', resource_queue, name_queue, 'Q4.2.4 - In which industry do you currently work? - Sector')
    functions.standard_table(db, audit, verified, 'Q4.2.4_2', resource_queue, name_queue, 'Q4.2.4 - In which industry do you currently work? - Industry')

    # Q4.3 - What is your age?
    functions.standard_statistics_mooc(db, audit, verified, 'Q4.3_1', resource_queue, name_queue, 'Q4.3 - What is your age?')

    # Q4.4 - What is your gender?
    functions.standard_table(db, audit, verified, 'Q4.4', resource_queue, name_queue, 'Q4.4 - What is your gender?')

    # Q4.5 - What is your (first) nationality? Please select the corresponding country.
    functions.standard_table(db, audit, verified, 'Q4.5_1', resource_queue, name_queue, 'Q4.5 - What is your (first) nationality? Please select the corresponding country. - '
                                                                                        'Continent')
    functions.standard_table(db, audit, verified, 'Q4.5_2', resource_queue, name_queue, 'Q4.5 - What is your (first) nationality? Please select the corresponding country. - '
                                                                                        'Country')

    # Q4.6 - What is the highest degree or level of education you have completed?
    functions.standard_table(db, audit, verified, 'Q4.6', resource_queue, name_queue, 'Q4.6 - What is the highest degree or level of education you have completed?')
    functions.other_list(audit, verified, 'Q4.6_9_TEXT', resource_queue, name_queue, 'Other')


def normal_edx_post(course_id, db, audit, verified, resource_queue, name_queue):
    # Start with the NPS score
    functions.nps_score(db, resource_queue, name_queue)

    if course_id in program_courses:
        functions.program_questions(db, resource_queue, name_queue)

    # Q2.1 - Since the start of the course, how would you describe your participation level?
    functions.bar_chart(db, 'Q2.1', resource_queue, name_queue, 'Q2.1 - Since the start of the course, how would you describe your participation level?')
    functions.standard_table(db, audit, verified, 'Q2.1', resource_queue, name_queue, 'Table')

    # Q2.2.1 - Could you please describe the reason(s) why you did not start the course?
    functions.normal_list(db, 'Q2.2.1', resource_queue, name_queue, 'Q2.2.1 - Could you please describe the reason(s) why you did not start the course?')

    # Q2.2.2 - Could you please describe which specific parts of the course you were interested in and why?
    functions.normal_list(db, 'Q2.2.2', resource_queue, name_queue, 'Q2.2.2 - Could you please describe which specific parts of the course you were interested in and why?')

    # Q3.1 - On a scale from 1 to 10, what overall grade would you give this course? (1: very poor, 10: excellent)
    functions.standard_statistics_mooc(db, audit, verified, 'Q3.1_1', resource_queue, name_queue, 'Q3.1 - On a scale from 1 to 10, '
                                                                                                  'what overall grade would you give this course? (1: very poor, 10: excellent)')

    # Q3.3 - What was the most valuable in this course for you?
    functions.normal_list(db, 'Q3.3', resource_queue, name_queue, 'Q3.3 - What was the most valuable in this course for you?')

    # Q4.4 - Which aspects of this course would you like us to improve?
    functions.normal_list(db, 'Q4.4', resource_queue, name_queue, 'Q4.4 - Which aspects of this course would you like us to improve?')

    # Q202 - What is your current type of enrollment in the course?
    functions.bar_chart(db, 'Q202', resource_queue, name_queue, 'Q202 - What is your current type of enrollment in the course?')
    functions.count(db, 'Q202', resource_queue, name_queue, 'Table')

    # Q204 - What additional value did you get from the verified track?
    functions.normal_list(db, 'Q204', resource_queue, name_queue, 'Q204 - What additional value did you get from the verified track?')

    # Q4.5 - How would you rate the following aspects of the course? The course was ...
    functions.stacked_bar_post(db, 'Q4.5', 'Q4.5_1.1', 'Q4.5_3.1', resource_queue, name_queue, 'Q4.5 - How would you rate the following aspects of the course? The course was ...')
    functions.standard_table(db, audit, verified, 'Q4.5_1.1', resource_queue, name_queue, 'Unique')
    functions.standard_table(db, audit, verified, 'Q4.5_2.1', resource_queue, name_queue, 'Useful')
    functions.standard_table(db, audit, verified, 'Q4.5_3.1', resource_queue, name_queue, 'Interesting')

    # Q4.6 - How would you rate the difficulty level of the course?
    functions.describing_the_course(db, 'Q4.6', resource_queue, name_queue, 'Q4.6 - How would you rate the difficulty level of the course?')
    functions.standard_table(db, audit, verified, 'Q4.6', resource_queue, name_queue, 'Table')

    # Q4.7 - How would you describe the amount of work required for the course?
    functions.describing_the_course(db, 'Q4.7', resource_queue, name_queue, 'Q4.7 - How would you describe the amount of work required for the course?')
    functions.standard_table(db, audit, verified, 'Q4.7', resource_queue, name_queue, 'Table')

    # Q4.8 - How would you describe the breadth of topics covered in this course?
    functions.describing_the_course(db, 'Q4.8', resource_queue, name_queue, 'Q4.8 - How would you describe the breadth of topics covered in this course?')
    functions.standard_table(db, audit, verified, 'Q4.8', resource_queue, name_queue, 'Table')

    # Q4.9 - How would you describe the length of the course (i.e. number of weeks)?
    functions.describing_the_course(db, 'Q4.9', resource_queue, name_queue, 'Q4.9 - How would you describe the length of the course (i.e. number of weeks)?')
    functions.standard_table(db, audit, verified, 'Q4.9', resource_queue, name_queue, 'Table')

    # Q5.1 - On average, how many hours did you work on this course per week?
    functions.standard_statistics_mooc(db, audit, verified, 'Q5.1_1', resource_queue, name_queue, 'Q5.1 - On average, how many hours did you work on this course per week?')

    # Q4.2 - Which elements of the course did you use or participate in?
    functions.split_choose_all_that_apply_mooc(db, audit, verified, 'Q4.2', resource_queue, name_queue, 'Q4.2 - Which elements of the course did you use or participate in?')

    # Q4.2.1 - How satisfied were you with the following elements of this course?
    functions.stacked_bar_post_split(audit, verified, 'Q5.2.1_x1', resource_queue, name_queue, 'Q4.2.1 - How satisfied were you with the following elements of this course? - '
                                                                                               'Videos')
    functions.standard_table(db, audit, verified, 'Q5.2.1_x1', resource_queue, name_queue, 'Table')
    functions.stacked_bar_post_split(audit, verified, 'Q5.2.1_x2', resource_queue, name_queue, 'Q4.2.1 - How satisfied were you with the following elements of this course? - '
                                                                                               'Reading materials')
    functions.standard_table(db, audit, verified, 'Q5.2.1_x2', resource_queue, name_queue, 'Table')
    functions.stacked_bar_post_split(audit, verified, 'Q5.2.1_x3', resource_queue, name_queue, 'Q4.2.1 - How satisfied were you with the following elements of this course? - '
                                                                                               'Forums')
    functions.standard_table(db, audit, verified, 'Q5.2.1_x3', resource_queue, name_queue, 'Table')
    functions.stacked_bar_post_split(audit, verified, 'Q5.2.1_x4', resource_queue, name_queue, 'Q4.2.1 - How satisfied were you with the following elements of this course? - '
                                                                                               'Exercises, quizzes, assignments')
    functions.standard_table(db, audit, verified, 'Q5.2.1_x4', resource_queue, name_queue, 'Table')
    functions.stacked_bar_post_split(audit, verified, 'Q4.2.1_x5', resource_queue, name_queue, 'Q4.2.1 - How satisfied were you with the following elements of this course? - '
                                                                                               'Group work')
    functions.standard_table(db, audit, verified, 'Q4.2.1_x5', resource_queue, name_queue, 'Table')
    functions.stacked_bar_post_split(audit, verified, 'Q4.2.1_x6', resource_queue, name_queue, 'Q4.2.1 - How satisfied were you with the following elements of this course? - '
                                                                                               'Feedback by instructors')
    functions.standard_table(db, audit, verified, 'Q4.2.1_x6', resource_queue, name_queue, 'Table')
    functions.stacked_bar_post_split(audit, verified, 'Q4.2.1_x7', resource_queue, name_queue, 'Q4.2.1 - How satisfied were you with the following elements of this course? - '
                                                                                               'Possibility to work on your own project')
    functions.standard_table(db, audit, verified, 'Q4.2.1_x7', resource_queue, name_queue, 'Table')

    # Q4.2.2 - How valuable do you feel were the following elements of this course?
    functions.stacked_bar_post_split(audit, verified, 'Q5.2.2_x1', resource_queue, name_queue, 'Q4.2.2 - How valuable do you feel were the following elements of this course? - '
                                                                                               'Videos')
    functions.standard_table(db, audit, verified, 'Q5.2.2_x1', resource_queue, name_queue, 'Table')
    functions.stacked_bar_post_split(audit, verified, 'Q5.2.2_x2', resource_queue, name_queue, 'Q4.2.2 - How valuable do you feel were the following elements of this course? - '
                                                                                               'Reading materials')
    functions.standard_table(db, audit, verified, 'Q5.2.2_x2', resource_queue, name_queue, 'Table')
    functions.stacked_bar_post_split(audit, verified, 'Q5.2.2_x3', resource_queue, name_queue, 'Q4.2.2 - How valuable do you feel were the following elements of this course? - '
                                                                                               'Forums')
    functions.standard_table(db, audit, verified, 'Q5.2.2_x3', resource_queue, name_queue, 'Table')
    functions.stacked_bar_post_split(audit, verified, 'Q5.2.2_x4', resource_queue, name_queue, 'Q4.2.2 - How valuable do you feel were the following elements of this course? - '
                                                                                               'Exercises, quizzes, assignments')
    functions.standard_table(db, audit, verified, 'Q5.2.2_x4', resource_queue, name_queue, 'Table')
    functions.stacked_bar_post_split(audit, verified, 'Q4.2.2_x5', resource_queue, name_queue, 'Q4.2.2 - How valuable do you feel were the following elements of this course? - '
                                                                                               'Group work')
    functions.standard_table(db, audit, verified, 'Q4.2.2_x5', resource_queue, name_queue, 'Table')
    functions.stacked_bar_post_split(audit, verified, 'Q4.2.2_x6', resource_queue, name_queue, 'Q4.2.2 - How valuable do you feel were the following elements of this course? - '
                                                                                               'Feedback by instructors')
    functions.standard_table(db, audit, verified, 'Q4.2.2_x6', resource_queue, name_queue, 'Table')
    functions.stacked_bar_post_split(audit, verified, 'Q4.2.2_x7', resource_queue, name_queue, 'Q4.2.2 - How valuable do you feel were the following elements of this course? - '
                                                                                               'Possibility to work on your own project')
    functions.standard_table(db, audit, verified, 'Q4.2.2_x7', resource_queue, name_queue, 'Table')

    # Q4.2.3 - Why didn't you use or participate in [QID117-ChoiceGroup-UnselectedChoices]?
    functions.normal_list(db, 'Q4.2.3', resource_queue, name_queue, 'Q4.2.3 - Why didnt you use or participate')

    # Q4.3 - What was the biggest challenge in completing this course?
    functions.bar_chart(db, 'Q4.3', resource_queue, name_queue, 'Q4.3 - What was the biggest challenge in completing this course?')
    functions.standard_table(db, audit, verified, 'Q4.3', resource_queue, name_queue, 'Table')
    functions.other_total(db, 'Q4.3_5_TEXT', resource_queue, name_queue, 'Other')

    # Q4.3.1 - At the beginning of the survey you said that you participated in the course, but stopped
    # participating along the way. Why did you not participate in the course until the end?
    # Choose the answer that applies the most.
    functions.bar_chart(db, 'Q4.3.1', resource_queue, name_queue, 'Q4.3.1 - At the beginning of the survey you said that you participated in the course, '
                                                                  'but stopped participating along the way. Why did you not participate in the course until the end?')
    functions.standard_table(db, audit, verified, 'Q4.3.1', resource_queue, name_queue, 'Table')
    functions.other_total(db, 'Q4.3.1_6_TEXT', resource_queue, name_queue, 'Other')

    # Course specific blocks are displayed below block
    # -----------------------------------------
    # ScratchTENGx course specific
    if 'ScratchTENGx' in course_id:
        # Q184 - What do you intend students to learn about Scratch programming?
        functions.normal_list(db, 'Q184', resource_queue, name_queue, 'Q184 - What do you intend students to learn about Scratch programming?')

        # Q186 - Why is it important for the students to learn this?
        functions.normal_list(db, 'Q186', resource_queue, name_queue, 'Q186 - Why is it important for the students to learn this?')

        # Q188 - What do you know about students’ thinking (prior knowledge, learning difficulties) that influences your teaching of Scratch programming?
        functions.normal_list(db, 'Q188', resource_queue, name_queue, 'Q188 - What do you know about students’ thinking (prior knowledge, '
                                                                      'learning difficulties) that influences your teaching of Scratch programming?')

        # Q190 - What do you think is a suitable method for teaching Scratch programming?
        functions.normal_list(db, 'Q190', resource_queue, name_queue, 'Q190 - What do you think is a suitable method for teaching Scratch programming?')

        # Q192 - What are your particular reasons for choosing this method?
        functions.normal_list(db, 'Q192', resource_queue, name_queue, 'Q192 - What are your particular reasons for choosing this method?')

        # Q194 - What would be a suitable way of assessing students’ understanding or confusion around Scratch programming?
        functions.normal_list(db, 'Q194', resource_queue, name_queue, 'Q194 - What would be a suitable way of assessing students’ '
                                                                      'understanding or confusion around Scratch programming?')

        # Q196 - What are your reasons for choosing this particular way of assessment?
        functions.normal_list(db, 'Q196', resource_queue, name_queue, 'Q196 - What are your reasons for choosing this particular way of assessment?')

        # Q197 - Have you implemented the content of this MOOC in your classrooms?
        functions.bar_chart(db, 'Q!97', resource_queue, name_queue, 'Q197 - Have you implemented the content of this MOOC in your classrooms?')
        functions.standard_table_profed(db, 'Q!97', resource_queue, name_queue, 'Q197 - Have you implemented the content of this MOOC in your classrooms?')

        # Q198 - Please explain how have you done it
        functions.normal_list(db, 'Q198', resource_queue, name_queue, 'Q198 - Please explain how have you done it')

    # IB01x course specific
    if 'IB01x' in course_id:
        # Q251 - Rank the prizes from the best to least
        functions.stacked_bar_ib_questions(db, 'Q251', 'Q251_1', 'Q251_4', resource_queue, name_queue, 'Q251 - Rank the prizes from the best to least')

        # Q252 - Do you have any other prize suggestions?
        functions.normal_list(db, 'Q252', resource_queue, name_queue, 'Q252 - Do you have any other prize suggestions?')

        # Q247 - Did you look on the Buddy up! forum?
        functions.bar_chart(db, 'Q247', resource_queue, name_queue, 'Q247 - Did you look on the Buddy up! forum?')
        functions.standard_table_profed(db, 'Q247', resource_queue, name_queue, 'Table')

        # Q248 - Did you buddy up?
        functions.bar_chart(db, 'Q248', resource_queue, name_queue, 'Q248 - Did you buddy up?')
        functions.standard_table_profed(db, 'Q248', resource_queue, name_queue, 'Table')

        # Q249 - Did it help you?
        functions.bar_chart(db, 'Q249', resource_queue, name_queue, 'Q249 - Did it help you?')
        functions.standard_table_profed(db, 'Q249', resource_queue, name_queue, 'Table')

        # Q250 - How can we improve the Buddy up forum?
        functions.normal_list(db, 'Q250', resource_queue, name_queue, 'Q250 - How can we improve the Buddy up forum?')


def low_results_edx_post(course_id, db, audit, verified, resource_queue, name_queue):
    # Start with the NPS score
    functions.nps_score(db, resource_queue, name_queue)

    if course_id in program_courses:
        functions.program_questions(db, resource_queue, name_queue)

    # Q2.1 - Since the start of the course, how would you describe your participation level?
    functions.standard_table(db, audit, verified, 'Q2.1', resource_queue, name_queue, 'Q2.1 - Since the start of the course, how would you describe your participation level?')

    # Q2.2.1 - Could you please describe the reason(s) why you did not start the course?
    functions.normal_list(db, 'Q2.2.1', resource_queue, name_queue, 'Q2.2.1 - Could you please describe the reason(s) why you did not start the course?')

    # Q2.2.2 - Could you please describe which specific parts of the course you were interested in and why?
    functions.normal_list(db, 'Q2.2.2', resource_queue, name_queue, 'Q2.2.2 - Could you please describe which specific parts of the course you were interested in and why?')

    # Q3.1 - On a scale from 1 to 10, what overall grade would you give this course? (1: very poor, 10: excellent)
    functions.standard_statistics_mooc(db, audit, verified, 'Q3.1_1', resource_queue, name_queue, 'Q3.1 - On a scale from 1 to 10, '
                                                                                                  'what overall grade would you give this course? (1: very poor, 10: excellent)')

    # Q3.3 - What was the most valuable in this course for you?
    functions.normal_list(db, 'Q3.3', resource_queue, name_queue, 'Q3.3 - What was the most valuable in this course for you?')

    # Q4.4 - Which aspects of this course would you like us to improve?
    functions.normal_list(db, 'Q4.4', resource_queue, name_queue, 'Q4.4 - Which aspects of this course would you like us to improve?')

    # Q202 - What is your current type of enrollment in the course?
    functions.count(db, 'Q202', resource_queue, name_queue, 'Q202 - What is your current type of enrollment in the course?')

    # Q204 - What additional value did you get from the verified track?
    functions.normal_list(db, 'Q204', resource_queue, name_queue, 'Q204 - What additional value did you get from the verified track?')

    # Q4.5 - How would you rate the following aspects of the course? The course was ...
    functions.standard_table(db, audit, verified, 'Q4.5_1.1', resource_queue, name_queue, 'Q4.5 - How would you rate the following aspects of the course? The course was: Unique')
    functions.standard_table(db, audit, verified, 'Q4.5_2.1', resource_queue, name_queue, 'Q4.5 - How would you rate the following aspects of the course? The course was: Useful')
    functions.standard_table(db, audit, verified, 'Q4.5_3.1', resource_queue, name_queue, 'Q4.5 - How would you rate the following aspects of the course? The course was: '
                                                                                          'Interesting')

    # Q4.6 - How would you rate the difficulty level of the course?
    functions.standard_table(db, audit, verified, 'Q4.6', resource_queue, name_queue, 'Q4.6 - How would you rate the difficulty level of the course?')

    # Q4.7 - How would you describe the amount of work required for the course?
    functions.standard_table(db, audit, verified, 'Q4.7', resource_queue, name_queue, 'Q4.7 - How would you describe the amount of work required for the course?')

    # Q4.8 - How would you describe the breadth of topics covered in this course?
    functions.standard_table(db, audit, verified, 'Q4.8', resource_queue, name_queue, 'Q4.8 - How would you describe the breadth of topics covered in this course?')

    # Q4.9 - How would you describe the length of the course (i.e. number of weeks)?
    functions.standard_table(db, audit, verified, 'Q4.9', resource_queue, name_queue, 'Q4.9 - How would you describe the length of the course (i.e. number of weeks)?')

    # Q5.1 - On average, how many hours did you work on this course per week?
    functions.standard_statistics_mooc(db, audit, verified, 'Q5.1_1', resource_queue, name_queue, 'Q5.1 - On average, how many hours did you work on this course per week?')

    # Q4.2 - Which elements of the course did you use or participate in?
    functions.split_choose_all_that_apply_mooc(db, audit, verified, 'Q4.2', resource_queue, name_queue, 'Q4.2 - Which elements of the course did you use or participate in?')

    # Q4.2.1 - How satisfied were you with the following elements of this course?
    functions.standard_table(db, audit, verified, 'Q5.2.1_x1', resource_queue, name_queue, 'Q4.2.1 - How satisfied were you with the following elements of this course? - Videos')
    functions.standard_table(db, audit, verified, 'Q5.2.1_x2', resource_queue, name_queue, 'Q4.2.1 - How satisfied were you with the following elements of this course? - '
                                                                                           'Reading materials')
    functions.standard_table(db, audit, verified, 'Q5.2.1_x3', resource_queue, name_queue, 'Q4.2.1 - How satisfied were you with the following elements of this course? - Forums')
    functions.standard_table(db, audit, verified, 'Q5.2.1_x4', resource_queue, name_queue, 'Q4.2.1 - How satisfied were you with the following elements of this course? - '
                                                                                           'Exercises, quizzes, assignments')
    functions.standard_table(db, audit, verified, 'Q4.2.1_x5', resource_queue, name_queue, 'Q4.2.1 - How satisfied were you with the following elements of this course? - '
                                                                                           'Group work')
    functions.standard_table(db, audit, verified, 'Q4.2.1_x6', resource_queue, name_queue, 'Q4.2.1 - How satisfied were you with the following elements of this course? - '
                                                                                           'Feedback by instructors')
    functions.standard_table(db, audit, verified, 'Q4.2.1_x7', resource_queue, name_queue, 'Q4.2.1 - How satisfied were you with the following elements of this course? - '
                                                                                           'Possibility to work on your own project')

    # Q4.2.2 - How valuable do you feel were the following elements of this course?
    functions.standard_table(db, audit, verified, 'Q5.2.2_x1', resource_queue, name_queue, 'Q4.2.2 - How valuable do you feel were the following elements of this course? - '
                                                                                           'Videos')
    functions.standard_table(db, audit, verified, 'Q5.2.2_x2', resource_queue, name_queue, 'Q4.2.2 - How valuable do you feel were the following elements of this course? - '
                                                                                           'Reading materials')
    functions.standard_table(db, audit, verified, 'Q5.2.2_x3', resource_queue, name_queue, 'Q4.2.2 - How valuable do you feel were the following elements of this course? - '
                                                                                           'Forums')
    functions.other_total(db, 'Q4.3.1_6_TEXT', resource_queue, name_queue, 'Other')
    functions.standard_table(db, audit, verified, 'Q5.2.2_x4', resource_queue, name_queue, 'Q4.2.2 - How valuable do you feel were the following elements of this course? - '
                                                                                           'Exercises, quizzes, assignments')
    functions.standard_table(db, audit, verified, 'Q4.2.2_x5', resource_queue, name_queue, 'Q4.2.2 - How valuable do you feel were the following elements of this course? - '
                                                                                           'Group work')
    functions.standard_table(db, audit, verified, 'Q4.2.2_x6', resource_queue, name_queue, 'Q4.2.2 - How valuable do you feel were the following elements of this course? - '
                                                                                           'Feedback by instructors')
    functions.standard_table(db, audit, verified, 'Q4.2.2_x7', resource_queue, name_queue, 'Q4.2.2 - How valuable do you feel were the following elements of this course? - '
                                                                                           'Possibility to work on your own project')

    # Q4.2.3 - Why didn't you use or participate in [QID117-ChoiceGroup-UnselectedChoices]?
    functions.normal_list(db, 'Q4.2.3', resource_queue, name_queue, 'Q4.2.3 - Why didnt you use or participate')

    # Q4.3 - What was the biggest challenge in completing this course?
    functions.standard_table(db, audit, verified, 'Q4.3', resource_queue, name_queue, 'Q4.3 - What was the biggest challenge in completing this course?')
    functions.other_total(db, 'Q4.3_5_TEXT', resource_queue, name_queue, 'Other')

    # Q4.3.1 - At the beginning of the survey you said that you participated in the course, but stopped
    # participating along the way. Why did you not participate in the course until the end?
    # Choose the answer that applies the most.
    functions.standard_table(db, audit, verified, 'Q4.3.1', resource_queue, name_queue, 'Q4.3.1 - At the beginning of the survey you said that you participated in the course, '
                                                                                        'but stopped participating along the way. Why did you not participate in the course '
                                                                                        'until the end?')

    # Course specific blocks are displayed below block
    # -----------------------------------------
    # ScratchTENGx course specific
    if 'ScratchTENGx' in course_id:
        # Q184 - What do you intend students to learn about Scratch programming?
        functions.normal_list(db, 'Q184', resource_queue, name_queue, 'Q184 - What do you intend students to learn about Scratch programming?')

        # Q186 - Why is it important for the students to learn this?
        functions.normal_list(db, 'Q186', resource_queue, name_queue, 'Q186 - Why is it important for the students to learn this?')

        # Q188 - What do you know about students’ thinking (prior knowledge, learning difficulties) that influences your teaching of Scratch programming?
        functions.normal_list(db, 'Q188', resource_queue, name_queue, 'Q188 - What do you know about students’ thinking (prior knowledge, '
                                                                      'learning difficulties) that influences your teaching of Scratch programming?')

        # Q190 - What do you think is a suitable method for teaching Scratch programming?
        functions.normal_list(db, 'Q190', resource_queue, name_queue, 'Q190 - What do you think is a suitable method for teaching Scratch programming?')

        # Q192 - What are your particular reasons for choosing this method?
        functions.normal_list(db, 'Q192', resource_queue, name_queue, 'Q192 - What are your particular reasons for choosing this method?')

        # Q194 - What would be a suitable way of assessing students’ understanding or confusion around Scratch programming?
        functions.normal_list(db, 'Q194', resource_queue, name_queue, 'Q194 - What would be a suitable way of assessing students’ '
                                                                      'understanding or confusion around Scratch programming?')

        # Q196 - What are your reasons for choosing this particular way of assessment?
        functions.normal_list(db, 'Q196', resource_queue, name_queue, 'Q196 - What are your reasons for choosing this particular way of assessment?')

        # Q197 - Have you implemented the content of this MOOC in your classrooms?
        functions.standard_table_profed(db, 'Q!97', resource_queue, name_queue, 'Q197 - Have you implemented the content of this MOOC in your classrooms?')

        # Q198 - Please explain how have you done it
        functions.normal_list(db, 'Q198', resource_queue, name_queue, 'Q198 - Please explain how have you done it')

    # IB01x course specific
    if 'IB01x' in course_id:
        # Q251 - Rank the prizes from the best to least
        functions.stacked_bar_ib_questions(db, 'Q251', 'Q251_1', 'Q251_4', resource_queue, name_queue, 'Q251 - Rank the prizes from the best to least')

        # Q252 - Do you have any other prize suggestions?
        functions.normal_list(db, 'Q252', resource_queue, name_queue, 'Q252 - Do you have any other prize suggestions?')

        # Q247 - Did you look on the Buddy up! forum?
        functions.standard_table_profed(db, 'Q247', resource_queue, name_queue, 'Q247 - Did you look on the Buddy up! forum?')

        # Q248 - Did you buddy up?
        functions.standard_table_profed(db, 'Q248', resource_queue, name_queue, 'Q248 - Did you buddy up?')

        # Q249 - Did it help you?
        functions.standard_table_profed(db, 'Q249', resource_queue, name_queue, 'Q249 - Did it help you?')

        # Q250 - How can we improve the Buddy up forum?
        functions.normal_list(db, 'Q250', resource_queue, name_queue, 'Q250 - How can we improve the Buddy up forum?')


def normal_profed_pre(course_id, db, resource_queue, name_queue):
    # Program expectations block
    # -----------------------------------------
    if course_id in program_courses:
        if len(db['Q179'][2:].dropna()) >= 5:
            functions.program_expectations(db, resource_queue, name_queue)
        else:
            functions.no_results_file(resource_queue, name_queue)

    # Reasons & motivation block
    # -----------------------------------------
    # Q2.1 - How did you discover this course?
    functions.bar_chart(db, 'Q2.1', resource_queue, name_queue, 'Q2.1 - How did you discover this course?')
    functions.standard_table_profed(db, 'Q2.1', resource_queue, name_queue, 'Table')
    # Q2.1_7 - Social media part
    if len(db['Q2.1_7_TEXT'][2:].dropna()) >= 5:
        functions.bar_chart(db, 'Q2.1_7_TEXT', resource_queue, name_queue, 'Which social media')
        functions.standard_table_profed(db, 'Q2.1_7_TEXT', resource_queue, name_queue, 'Table')
    # Q2.1_8 - Other
    functions.other_total(db, 'Q2.1_8_TEXT', resource_queue, name_queue, 'Other')

    # Q2.2 - Were you actively looking for a course before enrolling in this course?
    functions.bar_chart(db, 'Q2.2', resource_queue, name_queue, 'Q2.2 - Were you actively looking for a course before enrolling in this course?')
    functions.standard_table_profed(db, 'Q2.2', resource_queue, name_queue, 'Table')

    # Q2.2.1 - What type of course were you initially looking for?
    functions.bar_chart(db, 'Q2.2.1', resource_queue, name_queue, 'Q2.2.1 - What type of course were you initially looking for?')
    functions.standard_table_profed(db, 'Q2.2.1', resource_queue, name_queue, 'Table')

    # Q186 - Which of the following options best describes your experience with online courses?
    functions.bar_chart(db, 'Q186', resource_queue, name_queue, 'Q186 - Which of the following options best describes your experience with online courses?')
    functions.standard_table_profed(db, 'Q186', resource_queue, name_queue, 'Table')

    # Q2.3 - What best describes your motivation for enrolling in this course? My motivation is
    functions.bar_chart(db, 'Q2.3', resource_queue, name_queue, 'Q2.3 - What best describes your motivation for enrolling in this course? My motivation is')
    functions.standard_table_profed(db, 'Q2.3', resource_queue, name_queue, 'Table')
    functions.other_total(db, 'Q2.3_5_TEXT', resource_queue, name_queue, 'Other')

    # Q2.3.1 - Could you elaborate on your reasons for taking this course?
    functions.other_total(db, 'Q2.3.1', resource_queue, name_queue, 'Q2.3.1 - Could you elaborate on your reasons for taking this course?')

    # Q2.4 - How important were the following factors in your decision to enrol in this course?
    functions.stacked_bar_pre(db, 'Q2.4', 'Q2.4_1', 'Q2.4_21', resource_queue, name_queue,
                              'Q2.4 - How important were the following factors in your decision to enrol in this course?')
    functions.categories_total_profed(db, 'Q2.4', 'Q2.4_1', 'Q2.4_21', ['Uniqueness of this course', 'Potential usefulness of this course', 'Interesting topic of this course',
                                                                        'Lecturer(s) involved with this course', 'University(ies) involved with this course',
                                                                        'That the course is offered online', 'The possibility to receive a certificate or credentials',
                                                                        'Time and effort required to complete the course', 'Price of the certificate',
                                                                        'The level of content suits me', 'The opportunity to interact with likeminded people'],
                                      resource_queue, name_queue, 'Table')

    # Expectations block
    # -----------------------------------------
    # Q3.1 - What do you think might be the biggest challenge in completing this course for you?
    functions.bar_chart(db, 'Q3.1', resource_queue, name_queue, 'Q3.1 - What do you think might be the biggest challenge in completing this course for you?')
    functions.standard_table_profed(db, 'Q3.1', resource_queue, name_queue, 'Table')
    functions.other_total(db, 'Q3.1_5_TEXT', resource_queue, name_queue, 'Other')

    # Q3.2 - How important are the following elements for you in this course?
    functions.stacked_bar_pre(db, 'Q3.2', 'Q108_1', 'Q108_4', resource_queue, name_queue, 'Q3.2 - How important are the following elements for you in this course?')
    functions.categories_total_profed(db, 'Q3.2', 'Q108_1', 'Q108_4', ['Videos',
                                                                       'Reading materials',
                                                                       'Forums',
                                                                       'Exercises, quizzes, assignments'], resource_queue, name_queue, 'Table')

    # Q3.2.2 - How important are the following elements for you in this course?
    functions.stacked_bar_pre(db, 'Q3.2.2', 'Q3.2_5', 'Q3.2_7', resource_queue, name_queue, 'Q3.2.2 - How important are the following elements for you in this course?')
    functions.categories_total_profed(db, 'Q3.2.2', 'Q3.2_5', 'Q3.2_7', ['Group work (if applicable)',
                                                                         'Feedback by instructors (if applicable)',
                                                                         'Possibility to work on your own project (if applicable)'], resource_queue, name_queue, 'Table')

    # Q3.3 - On average, how many hours per week can you dedicate to this course?
    functions.standard_statistics_profed(db, 'Q3.3_1', resource_queue, name_queue, 'Q3.3 - On average, how many hours per week can you dedicate to this course?')

    # Demographics block
    # -----------------------------------------
    # Q4.1 - Which of the following options best describes your familiarity with the organization?
    functions.bar_chart(db, 'Q4.1', resource_queue, name_queue, 'Q4.1 - Which best describes your familiarity with TU Delft (Delft University of Technology)?')
    functions.standard_table_profed(db, 'Q4.1', resource_queue, name_queue, 'Table')

    # Q4.2 - Which of the following best describes your current situation?
    functions.bar_chart(db, 'Q4.2', resource_queue, name_queue, 'Q4.2 - Which of the following best describes your current situation?')
    functions.standard_table_profed(db, 'Q4.2', resource_queue, name_queue, 'Table')
    functions.other_total(db, 'Q4.2_7_TEXT', resource_queue, name_queue, 'Other')

    # Q4.2.1 - Which of the following best describes your job field?
    functions.bar_chart(db, 'Q4.2.1', resource_queue, name_queue, 'Q4.2.1 - Which of the following best describes your job field?')
    functions.standard_table_profed(db, 'Q4.2.1', resource_queue, name_queue, 'Table')

    # Q4.2.2 - What is your current job title?
    functions.normal_list(db, 'Q4.2.2', resource_queue, name_queue, 'Q4.2.2 - What is your current job title?')

    # Q4.2.3 - What is your educational background? (e.g. I have a Bachelor's degree in ... / MSc in ... / training on ...)
    functions.split_education(db, 'Q4.2.3', resource_queue, name_queue,
                              'Q4.2.3 - What is your educational background? (e.g. I have a Bachelors degree in ... / MSc in ... / training on ...)')

    # Q4.2.4 - In which industry do you currently work?
    functions.standard_table_profed(db, 'Q4.2.4_1', resource_queue, name_queue, 'Q4.2.4 - In which industry do you currently work? - Sector')
    functions.standard_table_profed(db, 'Q4.2.4_2', resource_queue, name_queue, 'Q4.2.4 - In which industry do you currently work? - Industry')

    # Q4.3 - What is your age?
    functions.standard_statistics_profed(db, 'Q4.3_1', resource_queue, name_queue, 'Q4.3 - What is your age?')

    # Q4.4 - What is your gender?
    functions.bar_chart(db, 'Q4.4', resource_queue, name_queue, 'Q4.4 - What is your gender?')
    functions.standard_table_profed(db, 'Q4.4', resource_queue, name_queue, 'Table')

    # Q4.5 - What is your (first) nationality? Please select the corresponding country.
    functions.standard_table_profed(db, 'Q4.5_1', resource_queue, name_queue, 'Q4.5 - What is your (first) nationality? Please select the corresponding country. - Continent')
    functions.standard_table_profed(db, 'Q4.5_2', resource_queue, name_queue, 'Q4.5 - What is your (first) nationality? Please select the corresponding country. - Country')

    # Q4.6 - What is the highest degree or level of education you have completed?
    functions.bar_chart(db, 'Q4.6', resource_queue, name_queue, 'Q4.6 - What is the highest degree or level of education you have completed?')
    functions.standard_table_profed(db, 'Q4.6', resource_queue, name_queue, 'Table')
    functions.other_total(db, 'Q4.6_9_TEXT', resource_queue, name_queue, 'Other')

    # Course specific blocks are displayed below block
    # -----------------------------------------
    # RAIL_01P course specific
    if 'RAIL_01P' in course_id:
        # Q145 - I have enrolled in:
        functions.bar_chart(db, 'Q145', resource_queue, name_queue, 'Q145 - I have enrolled in:')
        functions.standard_table_profed(db, 'Q145', resource_queue, name_queue, 'Table')

        # Q146 - Why did you choose to enroll in just the single course rather than the whole program or series (select all that apply)
        functions.split_rail(db, 'Q146', resource_queue, name_queue, 'Q146 - Why did you choose to enroll in just the single course '
                                                                     'rather than the whole program or series (select all that apply)')
        functions.other_total(db, 'Q146_5_TEXT', resource_queue, name_queue, 'Other')

        # Q147 - Why did you choose to enroll in the whole program or series? (select all that apply)
        functions.split_rail_two(db, 'Q147', resource_queue, name_queue, 'Q147 - Why did you choose to enroll in the whole program or series? (select all that apply)')
        functions.other_total(db, 'Q147_5_TEXT', resource_queue, name_queue, 'Other')

        # Q149 - Of the three courses in the railway series/program (excluding the capstone project), which is closest to your current or prospective job?
        functions.bar_chart(db, 'Q149', resource_queue, name_queue, 'Q149 - Of the three courses in the railway series/program (excluding the capstone project), '
                                                                    'which is closest to your current or prospective job?')
        functions.standard_table_profed(db, 'Q149', resource_queue, name_queue, 'Table')
        functions.normal_list(db, 'Q149_4_TEXT', resource_queue, name_queue, 'None, my professional area of prospective area is:')

        # Q150 - How interested are you in the courses in this railway program/series?
        functions.stacked_bar_rail_pre(db, 'Q150', 'Q149_1', 'Q149_3', resource_queue, name_queue, 'Q150 - How interested are you in the courses in this railway program/series?')
        functions.categories_total_profed(db, 'Q150', 'Q149_1', 'Q149_3', ['Track and Train Interaction', 'Real Time Traffic Management', 'Performance over Time'],
                                          resource_queue, name_queue, 'Table')


def low_results_profed_pre(course_id, db, resource_queue, name_queue):
    # Program expectations block
    # -----------------------------------------
    if course_id in program_courses:
        if len(db['Q179'][2:].dropna()) >= 5:
            functions.program_expectations(db, resource_queue, name_queue)
        else:
            functions.no_results_file(resource_queue, name_queue)

    # Reasons & motivation block
    # -----------------------------------------
    # Q2.1 - How did you discover this course?
    functions.standard_table_profed(db, 'Q2.1', resource_queue, name_queue, 'Q2.1 - How did you discover this course?')
    # Q2.1_7 - Social media part
    functions.standard_table_profed(db, 'Q2.1_7_TEXT', resource_queue, name_queue, 'Which social media')
    # Q2.1_8 - Other
    functions.other_total(db, 'Q2.1_8_TEXT', resource_queue, name_queue, 'Other')

    # Q2.2 - Were you actively looking for a course before enrolling in this course?
    functions.standard_table_profed(db, 'Q2.2', resource_queue, name_queue, 'Q2.2 - Were you actively looking for a course before enrolling in this course?')

    # Q2.2.1 - What type of course were you initially looking for?
    functions.standard_table_profed(db, 'Q2.2.1', resource_queue, name_queue, 'Q2.2.1 - What type of course were you initially looking for?')

    # Q186 - Which of the following options best describes your experience with online courses?
    functions.standard_table_profed(db, 'Q186', resource_queue, name_queue, 'Q186 - Which of the following options best describes your experience with online courses?')

    # Q2.3 - What best describes your motivation for enrolling in this course? My motivation is
    functions.standard_table_profed(db, 'Q2.3', resource_queue, name_queue, 'Q2.3 - What best describes your motivation for enrolling in this course? My motivation is')
    functions.other_total(db, 'Q2.3_5_TEXT', resource_queue, name_queue, 'Other')

    # Q2.3.1 - Could you elaborate on your reasons for taking this course?
    functions.other_total(db, 'Q2.3.1', resource_queue, name_queue, 'Q2.3.1 - Could you elaborate on your reasons for taking this course?')

    # # Q2.4 - How important were the following factors in your decision to enrol in this course?
    # functions.categories_total_profed(db, 'Q2.4', 'Q2.4_1', 'Q2.4_21', ['Uniqueness of this course', 'Potential usefulness of this course', 'Interesting topic of this course',
    #                                                                     'Lecturer(s) involved with this course', 'University(ies) involved with this course',
    #                                                                     'That the course is offered online', 'The possibility to receive a certificate or credentials',
    #                                                                     'Time and effort required to complete the course', 'Price of the certificate',
    #                                                                     'The level of content suits me', 'The opportunity to interact with likeminded people'],
    #                                   resource_queue, name_queue, 'Q2.4 - How important were the following factors in your decision to enrol in this course?')

    # Expectations block
    # -----------------------------------------
    # Q3.1 - What do you think might be the biggest challenge in completing this course for you?
    functions.standard_table_profed(db, 'Q3.1', resource_queue, name_queue, 'Q3.1 - What do you think might be the biggest challenge in completing this course for you?')
    functions.other_total(db, 'Q3.1_5_TEXT', resource_queue, name_queue, 'Other')

    # # Q3.2 - How important are the following elements for you in this course?
    # functions.categories_total_profed(db, 'Q3.2', 'Q108_1', 'Q108_4', ['Uniqueness of this course',
    #                                                                    'Potential usefulness of this course',
    #                                                                    'Interesting topic of this course',
    #                                                                    'Lecturer(s) involved with this course'], resource_queue, name_queue,
    #                                   'Q3.2 - How important are the following elements for you in this course?')

    # Q3.2.2 - How important are the following elements for you in this course?
    # functions.categories_total_profed(db, 'Q3.2', 'Q3.2_5', 'Q3.2_7', ['Group work (if applicable)',
    #                                                                    'Feedback by instructors (if applicable)',
    #                                                                    'Possibility to work on your own project (if applicable)'], resource_queue, name_queue,
    #                                   'Q3.2.2 - How important are the following elements for you in this course?')

    # Q3.3 - On average, how many hours per week can you dedicate to this course?
    functions.standard_statistics_profed(db, 'Q3.3_1', resource_queue, name_queue, 'Q3.3 - On average, how many hours per week can you dedicate to this course?')

    # Demographics block
    # -----------------------------------------
    # Q4.1 - Which of the following options best describes your familiarity with the organization?
    functions.standard_table_profed(db, 'Q4.1', resource_queue, name_queue, 'Q4.1 - Which best describes your familiarity with TU Delft (Delft University of Technology)?')

    # Q4.2 - Which of the following best describes your current situation?
    functions.standard_table_profed(db, 'Q4.2', resource_queue, name_queue, 'Q4.2 - Which of the following best describes your current situation?')
    functions.other_total(db, 'Q4.2_7_TEXT', resource_queue, name_queue, 'Other')

    # Q4.2.1 - Which of the following best describes your job field?
    functions.standard_table_profed(db, 'Q4.2.1', resource_queue, name_queue, 'Q4.2.1 - Which of the following best describes your job field?')

    # Q4.2.2 - What is your current job title?
    functions.normal_list(db, 'Q4.2.2', resource_queue, name_queue, 'Q4.2.2 - What is your current job title?')

    # Q4.2.3 - What is your educational background? (e.g. I have a Bachelor's degree in ... / MSc in ... / training on ...)
    functions.split_education(db, 'Q4.2.3', resource_queue, name_queue,
                              'Q4.2.3 - What is your educational background? (e.g. I have a Bachelors degree in ... / MSc in ... / training on ...)')

    # Q4.2.4 - In which industry do you currently work?
    functions.standard_table_profed(db, 'Q4.2.4_1', resource_queue, name_queue, 'Q4.2.4 - In which industry do you currently work? - Sector')
    functions.standard_table_profed(db, 'Q4.2.4_2', resource_queue, name_queue, 'Q4.2.4 - In which industry do you currently work? - Industry')

    # Q4.3 - What is your age?
    functions.standard_statistics_profed(db, 'Q4.3_1', resource_queue, name_queue, 'Q4.3 - What is your age?')

    # Q4.4 - What is your gender?
    functions.standard_table_profed(db, 'Q4.4', resource_queue, name_queue, 'Q4.4 - What is your gender?')

    # Q4.5 - What is your (first) nationality? Please select the corresponding country.
    functions.standard_table_profed(db, 'Q4.5_1', resource_queue, name_queue, 'Q4.5 - What is your (first) nationality? Please select the corresponding country. - Continent')
    functions.standard_table_profed(db, 'Q4.5_2', resource_queue, name_queue, 'Q4.5 - What is your (first) nationality? Please select the corresponding country. - Country')

    # Q4.6 - What is the highest degree or level of education you have completed?
    functions.standard_table_profed(db, 'Q4.6', resource_queue, name_queue, 'Q4.6 - What is the highest degree or level of education you have completed?')
    functions.other_total(db, 'Q4.6_9_TEXT', resource_queue, name_queue, 'Other')

    # Course specific blocks are displayed below block
    # -----------------------------------------
    # RAIL_01P course specific
    if 'RAIL_01P' in course_id:
        # Q145 - I have enrolled in:
        functions.standard_table_profed(db, 'Q145', resource_queue, name_queue, 'Q145 - I have enrolled in:')

        # Q146 - Why did you choose to enroll in just the single course rather than the whole program or series (select all that apply)
        functions.split_rail(db, 'Q146', resource_queue, name_queue, 'Q146 - Why did you choose to enroll in just the single course '
                                                                     'rather than the whole program or series (select all that apply)')
        functions.other_total(db, 'Q146_5_TEXT', resource_queue, name_queue, 'Other')

        # Q147 - Why did you choose to enroll in the whole program or series? (select all that apply)
        functions.split_rail_two(db, 'Q147', resource_queue, name_queue, 'Q147 - Why did you choose to enroll in the whole program or series? (select all that apply)')
        functions.other_total(db, 'Q147_5_TEXT', resource_queue, name_queue, 'Other')

        # Q149 - Of the three courses in the railway series/program (excluding the capstone project), which is closest to your current or prospective job?
        functions.standard_table_profed(db, 'Q149', resource_queue, name_queue, 'Q149 - Of the three courses in the railway series/program (excluding the capstone project), '
                                                                                'which is closest to your current or prospective job?')
        functions.normal_list(db, 'Q149_4_TEXT', resource_queue, name_queue, 'None, my professional area of prospective area is:')

        # Q150 - How interested are you in the courses in this railway program/series?
        functions.categories_total_profed(db, 'Q150', 'Q149_1', 'Q149_3', ['Track and Train Interaction', 'Real Time Traffic Management', 'Performance over Time'],
                                          resource_queue, name_queue, 'Q150 - How interested are you in the courses in this railway program/series?')


def normal_profed_post(course_id, db, resource_queue, name_queue):
    # Start with the NPS score
    functions.nps_score(db, resource_queue, name_queue)

    if course_id in program_courses:
        functions.program_questions(db, resource_queue, name_queue)

    # Q2.1 - Since the start of the course, how would you describe your participation level?
    functions.bar_chart(db, 'Q2.1', resource_queue, name_queue, 'Q2.1 - Since the start of the course, how would you describe your participation level?')
    functions.standard_table_profed(db, 'Q2.1', resource_queue, name_queue, 'Table')

    # Q2.2.1 - Could you please describe the reason(s) why you did not start the course?
    functions.normal_list(db, 'Q2.2.1', resource_queue, name_queue, 'Q2.2.1 - Could you please describe the reason(s) why you did not start the course?')

    # Q2.2.2 - Could you please describe which specific parts of the course you were interested in and why?
    functions.normal_list(db, 'Q2.2.2', resource_queue, name_queue, 'Q2.2.2 - Could you please describe which specific parts of the course you were interested in and why?')

    # Q3.1 - On a scale from 1 to 10, what overall grade would you give this course? (1: very poor, 10: excellent)
    functions.standard_statistics_profed(db, 'Q3.1_1', resource_queue, name_queue, 'Q3.1 - On a scale from 1 to 10, '
                                                                                   'what overall grade would you give this course? (1: very poor, 10: excellent)')

    # Q3.3 - What was the most valuable in this course for you?
    functions.normal_list(db, 'Q3.3', resource_queue, name_queue, 'Q3.3 - What was the most valuable in this course for you?')

    # Q4.4 - Which aspects of this course would you like us to improve?
    functions.normal_list(db, 'Q4.4', resource_queue, name_queue, 'Q4.4 - Which aspects of this course would you like us to improve?')

    # Q202 - What is your current type of enrollment in the course?
    functions.bar_chart(db, 'Q202', resource_queue, name_queue, 'Q202 - What is your current type of enrollment in the course?')
    functions.count(db, 'Q202', resource_queue, name_queue, 'Table')

    # Q204 - What additional value did you get from the verified track?
    functions.normal_list(db, 'Q204', resource_queue, name_queue, 'Q204 - What additional value did you get from the verified track?')

    # Q4.5 - How would you rate the following aspects of the course? The course was ...
    functions.stacked_bar_post(db, 'Q4.5', 'Q4.5_1.1', 'Q4.5_3.1', resource_queue, name_queue, 'Q4.5 - How would you rate the following aspects of the course? The course was ...')
    functions.standard_table_profed(db, 'Q4.5_1.1', resource_queue, name_queue, 'Unique')
    functions.standard_table_profed(db, 'Q4.5_2.1', resource_queue, name_queue, 'Useful')
    functions.standard_table_profed(db, 'Q4.5_3.1', resource_queue, name_queue, 'Interesting')

    # Q4.6 - How would you rate the difficulty level of the course?
    functions.describing_the_course(db, 'Q4.6', resource_queue, name_queue, 'Q4.6 - How would you rate the difficulty level of the course?')
    functions.standard_table_profed(db, 'Q4.6', resource_queue, name_queue, 'Table')

    # Q4.7 - How would you describe the amount of work required for the course?
    functions.describing_the_course(db, 'Q4.7', resource_queue, name_queue, 'Q4.7 - How would you describe the amount of work required for the course?')
    functions.standard_table_profed(db, 'Q4.7', resource_queue, name_queue, 'Table')

    # Q4.8 - How would you describe the breadth of topics covered in this course?
    functions.describing_the_course(db, 'Q4.8', resource_queue, name_queue, 'Q4.8 - How would you describe the breadth of topics covered in this course?')
    functions.standard_table_profed(db, 'Q4.8', resource_queue, name_queue, 'Table')

    # Q4.9 - How would you describe the length of the course (i.e. number of weeks)?
    functions.describing_the_course(db, 'Q4.9', resource_queue, name_queue, 'Q4.9 - How would you describe the length of the course (i.e. number of weeks)?')
    functions.standard_table_profed(db, 'Q4.9', resource_queue, name_queue, 'Table')

    # Q5.1 - On average, how many hours did you work on this course per week?
    functions.standard_statistics_profed(db, 'Q5.1_1', resource_queue, name_queue, 'Q5.1 - On average, how many hours did you work on this course per week?')

    # Q4.2 - Which elements of the course did you use or participate in?
    functions.split_choose_all_that_apply_profed(db, 'Q4.2', resource_queue, name_queue, 'Q4.2 - Which elements of the course did you use or participate in?')

    # Q4.2.1 - How satisfied were you with the following elements of this course?
    functions.stacked_bar_post_profed(db, 'Q4.2.1', 'Q5.2.1_x1', 'Q4.2.1_x7', resource_queue, name_queue, 'Q4.2.1 - How satisfied were you with the following elements of this '
                                                                                                          'course? - Videos')
    functions.categories_total_profed(db, 'Q4.2.1', 'Q5.2.1_x1', 'Q4.2.1_x7', ['Videos', 'Reading materials', 'Forums', 'Exercises, quizzes, assignments', 'Group work',
                                                                               'Feedback by instructors', 'Possibility to work on your own project'], resource_queue, name_queue,
                                      'Table')

    # Q4.2.2 - How valuable do you feel were the following elements of this course?
    functions.stacked_bar_post_profed(db, 'Q4.2.2', 'Q5.2.2_x1', 'Q4.2.2_x7', resource_queue, name_queue, 'Q4.2.2 - How valuable do you feel were the following elements of this '
                                                                                                          'course? - Videos')
    functions.categories_total_profed(db, 'Q4.2.2', 'Q5.2.2_x1', 'Q4.2.2_x7', ['Videos', 'Reading materials', 'Forums', 'Exercises, quizzes, assignments', 'Group work',
                                                                               'Feedback by instructors', 'Possibility to work on your own project'], resource_queue, name_queue,
                                      'Table')

    # Q4.2.3 - Why didn't you use or participate in [QID117-ChoiceGroup-UnselectedChoices]?
    functions.normal_list(db, 'Q4.2.3', resource_queue, name_queue, 'Q4.2.3 - Why didnt you use or participate')

    # Q4.3 - What was the biggest challenge in completing this course?
    functions.bar_chart(db, 'Q4.3', resource_queue, name_queue, 'Q4.3 - What was the biggest challenge in completing this course?')
    functions.standard_table_profed(db, 'Q4.3', resource_queue, name_queue, 'Table')
    functions.other_total(db, 'Q4.3_5_TEXT', resource_queue, name_queue, 'Other')

    # Q4.3.1 - At the beginning of the survey you said that you participated in the course, but stopped
    # participating along the way. Why did you not participate in the course until the end?
    # Choose the answer that applies the most.
    functions.bar_chart(db, 'Q4.3.1', resource_queue, name_queue, 'Q4.3.1 - At the beginning of the survey you said that you participated in the course, '
                                                                  'but stopped participating along the way. Why did you not participate in the course until the end?')
    functions.standard_table_profed(db, 'Q4.3.1', resource_queue, name_queue, 'Table')
    functions.other_total(db, 'Q4.3.1_6_TEXT', resource_queue, name_queue, 'Other')

    # Course specific blocks are displayed below block
    # -----------------------------------------
    # ScratchTENGx course specific
    if 'ScratchTENGx' in course_id:
        # Q184 - What do you intend students to learn about Scratch programming?
        functions.normal_list(db, 'Q184', resource_queue, name_queue, 'Q184 - What do you intend students to learn about Scratch programming?')

        # Q186 - Why is it important for the students to learn this?
        functions.normal_list(db, 'Q186', resource_queue, name_queue, 'Q186 - Why is it important for the students to learn this?')

        # Q188 - What do you know about students’ thinking (prior knowledge, learning difficulties) that influences your teaching of Scratch programming?
        functions.normal_list(db, 'Q188', resource_queue, name_queue, 'Q188 - What do you know about students’ thinking (prior knowledge, '
                                                                      'learning difficulties) that influences your teaching of Scratch programming?')

        # Q190 - What do you think is a suitable method for teaching Scratch programming?
        functions.normal_list(db, 'Q190', resource_queue, name_queue, 'Q190 - What do you think is a suitable method for teaching Scratch programming?')

        # Q192 - What are your particular reasons for choosing this method?
        functions.normal_list(db, 'Q192', resource_queue, name_queue, 'Q192 - What are your particular reasons for choosing this method?')

        # Q194 - What would be a suitable way of assessing students’ understanding or confusion around Scratch programming?
        functions.normal_list(db, 'Q194', resource_queue, name_queue, 'Q194 - What would be a suitable way of assessing students’ '
                                                                      'understanding or confusion around Scratch programming?')

        # Q196 - What are your reasons for choosing this particular way of assessment?
        functions.normal_list(db, 'Q196', resource_queue, name_queue, 'Q196 - What are your reasons for choosing this particular way of assessment?')

        # Q197 - Have you implemented the content of this MOOC in your classrooms?
        functions.bar_chart(db, 'Q!97', resource_queue, name_queue, 'Q197 - Have you implemented the content of this MOOC in your classrooms?')
        functions.standard_table_profed(db, 'Q!97', resource_queue, name_queue, 'Table')

        # Q198 - Please explain how have you done it
        functions.normal_list(db, 'Q198', resource_queue, name_queue, 'Q198 - Please explain how have you done it')


def low_results_profed_post(course_id, db, resource_queue, name_queue):
    # Start with the NPS score
    functions.nps_score(db, resource_queue, name_queue)

    if course_id in program_courses:
        functions.program_questions(db, resource_queue, name_queue)

    # Q2.1 - Since the start of the course, how would you describe your participation level?
    functions.standard_table_profed(db, 'Q2.1', resource_queue, name_queue, 'Q2.1 - Since the start of the course, how would you describe your participation level?')

    # Q2.2.1 - Could you please describe the reason(s) why you did not start the course?
    functions.normal_list(db, 'Q2.2.1', resource_queue, name_queue, 'Q2.2.1 - Could you please describe the reason(s) why you did not start the course?')

    # Q2.2.2 - Could you please describe which specific parts of the course you were interested in and why?
    functions.normal_list(db, 'Q2.2.2', resource_queue, name_queue, 'Q2.2.2 - Could you please describe which specific parts of the course you were interested in and why?')

    # Q3.1 - On a scale from 1 to 10, what overall grade would you give this course? (1: very poor, 10: excellent)
    functions.standard_statistics_profed(db, 'Q3.1_1', resource_queue, name_queue, 'Q3.1 - On a scale from 1 to 10, '
                                                                                   'what overall grade would you give this course? (1: very poor, 10: excellent)')

    # Q3.3 - What was the most valuable in this course for you?
    functions.normal_list(db, 'Q3.3', resource_queue, name_queue, 'Q3.3 - What was the most valuable in this course for you?')

    # Q4.4 - Which aspects of this course would you like us to improve?
    functions.normal_list(db, 'Q4.4', resource_queue, name_queue, 'Q4.4 - Which aspects of this course would you like us to improve?')

    # Q202 - What is your current type of enrollment in the course?
    functions.count(db, 'Q202', resource_queue, name_queue, 'Q202 - What is your current type of enrollment in the course?')

    # Q204 - What additional value did you get from the verified track?
    functions.normal_list(db, 'Q204', resource_queue, name_queue, 'Q204 - What additional value did you get from the verified track?')

    # Q4.5 - How would you rate the following aspects of the course? The course was ...
    functions.standard_table_profed(db, 'Q4.5_1.1', resource_queue, name_queue, 'Q4.5 - How would you rate the following aspects of the course? The course was: Unique')
    functions.standard_table_profed(db, 'Q4.5_2.1', resource_queue, name_queue, 'Q4.5 - How would you rate the following aspects of the course? The course was: Useful')
    functions.standard_table_profed(db, 'Q4.5_3.1', resource_queue, name_queue, 'Q4.5 - How would you rate the following aspects of the course? The course was: Interesting')

    # Q4.6 - How would you rate the difficulty level of the course?
    functions.standard_table_profed(db, 'Q4.6', resource_queue, name_queue, 'Q4.6 - How would you rate the difficulty level of the course?')

    # Q4.7 - How would you describe the amount of work required for the course?
    functions.standard_table_profed(db, 'Q4.7', resource_queue, name_queue, 'Q4.7 - How would you describe the amount of work required for the course?')

    # Q4.8 - How would you describe the breadth of topics covered in this course?
    functions.standard_table_profed(db, 'Q4.8', resource_queue, name_queue, 'Q4.8 - How would you describe the breadth of topics covered in this course?')

    # Q4.9 - How would you describe the length of the course (i.e. number of weeks)?
    functions.standard_table_profed(db, 'Q4.9', resource_queue, name_queue, 'Q4.9 - How would you describe the length of the course (i.e. number of weeks)?')

    # Q5.1 - On average, how many hours did you work on this course per week?
    functions.standard_statistics_profed(db, 'Q5.1_1', resource_queue, name_queue, 'Q5.1 - On average, how many hours did you work on this course per week?')

    # Q4.2 - Which elements of the course did you use or participate in?
    functions.split_choose_all_that_apply_profed(db, 'Q4.2', resource_queue, name_queue, 'Q4.2 - Which elements of the course did you use or participate in?')

    # Q4.2.1 - How satisfied were you with the following elements of this course?
    functions.stacked_bar_post_profed(db, 'Q4.2.1', 'Q5.2.1_x1', 'Q4.2.1_x7', resource_queue, name_queue, 'Q4.2.1 - How satisfied were you with the following elements of this '
                                                                                                          'course? - Videos')
    functions.categories_total_profed(db, 'Q4.2.1', 'Q5.2.1_x1', 'Q4.2.1_x7', ['Videos', 'Reading materials', 'Forums', 'Exercises, quizzes, assignments', 'Group work',
                                                                               'Feedback by instructors', 'Possibility to work on your own project'], resource_queue, name_queue,
                                      'Table')

    # Q4.2.2 - How valuable do you feel were the following elements of this course?
    functions.categories_total_profed(db, 'Q4.2.2', 'Q5.2.2_x1', 'Q4.2.2_x7', ['Videos', 'Reading materials', 'Forums', 'Exercises, quizzes, assignments', 'Group work',
                                                                               'Feedback by instructors', 'Possibility to work on your own project'], resource_queue, name_queue,
                                      'Q4.2.1 - How satisfied were you with the following elements of this course?')

    # Q4.2.3 - Why didn't you use or participate in [QID117-ChoiceGroup-UnselectedChoices]?
    functions.normal_list(db, 'Q4.2.3', resource_queue, name_queue, 'Q4.2.3 - Why didnt you use or participate')

    # Q4.3 - What was the biggest challenge in completing this course?
    functions.standard_table_profed(db, 'Q4.3', resource_queue, name_queue, 'Q4.3 - What was the biggest challenge in completing this course?')
    functions.other_total(db, 'Q4.3_5_TEXT', resource_queue, name_queue, 'Other')

    # Q4.3.1 - At the beginning of the survey you said that you participated in the course, but stopped
    # participating along the way. Why did you not participate in the course until the end?
    # Choose the answer that applies the most.
    functions.standard_table_profed(db, 'Q4.3.1', resource_queue, name_queue, 'Q4.3.1 - At the beginning of the survey you said that you participated in the course, '
                                                                              'but stopped participating along the way. Why did you not participate in the course until the end?')
    functions.other_total(db, 'Q4.3.1_6_TEXT', resource_queue, name_queue, 'Other')

    # Course specific blocks are displayed below block
    # -----------------------------------------
    # ScratchTENGx course specific
    if 'ScratchTENGx' in course_id:
        # Q184 - What do you intend students to learn about Scratch programming?
        functions.normal_list(db, 'Q184', resource_queue, name_queue, 'Q184 - What do you intend students to learn about Scratch programming?')

        # Q186 - Why is it important for the students to learn this?
        functions.normal_list(db, 'Q186', resource_queue, name_queue, 'Q186 - Why is it important for the students to learn this?')

        # Q188 - What do you know about students’ thinking (prior knowledge, learning difficulties) that influences your teaching of Scratch programming?
        functions.normal_list(db, 'Q188', resource_queue, name_queue, 'Q188 - What do you know about students’ thinking (prior knowledge, '
                                                                      'learning difficulties) that influences your teaching of Scratch programming?')

        # Q190 - What do you think is a suitable method for teaching Scratch programming?
        functions.normal_list(db, 'Q190', resource_queue, name_queue, 'Q190 - What do you think is a suitable method for teaching Scratch programming?')

        # Q192 - What are your particular reasons for choosing this method?
        functions.normal_list(db, 'Q192', resource_queue, name_queue, 'Q192 - What are your particular reasons for choosing this method?')

        # Q194 - What would be a suitable way of assessing students’ understanding or confusion around Scratch programming?
        functions.normal_list(db, 'Q194', resource_queue, name_queue, 'Q194 - What would be a suitable way of assessing students’ '
                                                                      'understanding or confusion around Scratch programming?')

        # Q196 - What are your reasons for choosing this particular way of assessment?
        functions.normal_list(db, 'Q196', resource_queue, name_queue, 'Q196 - What are your reasons for choosing this particular way of assessment?')

        # Q197 - Have you implemented the content of this MOOC in your classrooms?
        functions.normal_list(db, 'Q!97', resource_queue, name_queue, 'Q197 - Have you implemented the content of this MOOC in your classrooms?')

        # Q198 - Please explain how have you done it
        functions.normal_list(db, 'Q198', resource_queue, name_queue, 'Q198 - Please explain how have you done it')
