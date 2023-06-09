from flask import Flask, jsonify,request, render_template,send_from_directory
from flask_cors import CORS
from flask_mysqldb import MySQL
from datetime import date
from werkzeug.utils import secure_filename
import os 
from github import Github

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

today = date.today()

app = Flask(__name__)
CORS(app,origins='http://localhost:8080')

app.config['MYSQL_HOST']= 'db4free.net'
app.config['MYSQL_USER']= 'rooter001'
app.config['MYSQL_PASSWORD']= '71dfd607'
app.config['MYSQL_DB']= 'college_app_db'
app.config['UPLOAD_FOLDER'] = 'uploads'
mysql= MySQL(app)


app.config.from_object(__name__)
CORS(app, resources={r"/*":{'origins':"*"}})

students = []

# @app.route('/')
# def index():
#     cur = mysql.connection.cursor()
#     cur.execute("select * from student")
#     fetchdata = cur.fetchall()
#     cur.close()

#     return render_template('index.html')

############################################LOGIN$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
@app.route('/Teacherlogin', methods=['GET'])
def get_teacher_credentials():
    try:
        email = request.args.get('email')  # Get the email parameter from the GET request query string
        cur = mysql.connection.cursor()
        cur.execute("SELECT email, password FROM teacher WHERE email = %s", (email,))  
        data = cur.fetchone()
        cur.close()
        if data is None:
            data='garbagevalue' #so that server keeps running
        return jsonify(data)
    except Exception as e:
        print('Error fetching credentials:', e)
        return jsonify([])
    
@app.route('/Adminlogin', methods=['GET'])
def get_credentials():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT email,password FROM authorise")
        credentials = cur.fetchone()
        cur.close()
        return jsonify(credentials)
    except Exception as e:
        print('Error fetching credentials:', e)
        return jsonify([])

############################anOUNCEMNT####################################################################

@app.route('/getAnnouncements', methods=['GET'])
def get_Announcement():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT id,text,title,created_date FROM announcement where created_date=%s", (today,))
        cnt = cur.fetchall()
        cur.close()
        return jsonify(cnt)
    except Exception as e:
        print('Error fetching announcements:', e)
        return jsonify([])
    
@app.route('/addAnnouncement', methods=['POST'])
def create_announcement():
    data = request.get_json()
    text= data['announcement']
    title= data['title']
    cur = mysql.connection.cursor()
    
    sql="SELECT MAX(id) + 1 AS next_id FROM announcement"
    cur.execute(sql)
    result = cur.fetchone()
    next_id = result[0]
    
    if next_id is None:
        next_id=1  
 
    query = "INSERT INTO announcement (id,title,text,created_date) VALUES (%s,%s,%s,%s)"
    cur.execute(query, (next_id,title,text,today))
    
    mysql.connection.commit()
    cur.close()
    
    return jsonify({'message': 'Announcement created successfully'})

######################## student ######################################################
@app.route('/addStudent', methods=['POST'])
def create_student():
    try:
        data = request.get_json()
        fname= data['firstName']
        sname= data['surname']
        age=data['age']
        address=data['address']
        phone=data['phone']
        course=data['selectedCourse']
        cur = mysql.connection.cursor()
        
        sql="SELECT MAX(id) + 1 AS next_id FROM student"
        cur.execute(sql)
        result = cur.fetchone()
        next_id = result[0]
        
        if next_id is None:
            next_id=1  
    
        query = "INSERT INTO student (id,first_name,surname,dob,address,phone,created_date,course) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        cur.execute(query, (next_id,fname,sname,age,address,phone,today,course))
        
        mysql.connection.commit()
        cur.close()
        
        return jsonify({'message': 'Student created successfully'})
    except Exception as e:
            print('Error fetching student requests:', e)
            return jsonify([])

@app.route('/getStudents', methods=['GET'])
def get_students():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT id, first_name,surname,dob,address,phone FROM student where deleted=0")
        students = cur.fetchall()
        cur.close()
        return jsonify(students)
    except Exception as e:
        print('Error fetching students:', e)
        return jsonify([])


@app.route('/getStudent/<int:student_id>', methods=['GET'])
def get_student(student_id):
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT id, first_name, surname, dob, address, phone,course FROM student WHERE id = %s", (student_id,))
        student = cur.fetchone()
        cur.close()
        if student:
            return jsonify(student)
        else:
            return jsonify({'message': 'Student not found'})
    except Exception as e:
        print('Error fetching student:', e)
        return jsonify({'message': 'Error fetching student'})


@app.route('/updateStudent/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.get_json()
    fname = data['firstName']
    sname = data['lastName']
    age = data['age']
    address = data['address']
    phone = data['phone']
    cur = mysql.connection.cursor()

    query = "UPDATE student SET first_name=%s, surname=%s, dob=%s, address=%s, phone=%s WHERE id=%s"
    cur.execute(query, (fname, sname, age, address, phone, student_id))

    mysql.connection.commit()
    cur.close()

    return jsonify({'message': 'Student updated successfully'})


@app.route('/deleteStudent/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    try:
        cur = mysql.connection.cursor()
        cur.execute("UPDATE student SET deleted=1 WHERE id = %s", (student_id,))
        mysql.connection.commit()
        cur.close()
        return jsonify({'message': 'Student deleted successfully'})
    except Exception as e:
        print('Error deleting student:', e)
        return jsonify({'message': 'Error deleting student'})
########################################################################################################################

#########################################course############################################################################    
@app.route('/addCourse', methods=['POST'])
def create_course():
    data = request.get_json()
    cname= data['courseName']
    code= data['courseCode']
    desc=data['courseDescription']
    cred=data['courseCredits']
    pre_req=data['coursePrerequisite']
    fee=data['courseFee']
    cur = mysql.connection.cursor()
    
    sql="SELECT MAX(id) + 1 AS next_id FROM course"
    cur.execute(sql)
    result = cur.fetchone()
    next_id = result[0]
    
    if next_id is None:
        next_id=1    

    query = "INSERT INTO course (id,name,code,description,credits,prerequisite,fee) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    cur.execute(query, (next_id,cname,code,desc,cred,pre_req,fee))
    
    mysql.connection.commit()
    cur.close()
    
    return jsonify({'message': 'Course created successfully'})

@app.route('/getCourses', methods=['GET'])
def get_courses():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT id, name,code,description,credits,prerequisite,fee FROM course where deleted=0")
        course = cur.fetchall()
        cur.close()
        return jsonify(course)
    except Exception as e:
        print('Error fetching course:', e)
        return jsonify([])
########################################################################################################################

#############################################TEACHERS#################################################################
@app.route('/addTeacher', methods=['POST'])
def create_teacher():
    data = request.get_json()
    fname= data['firstName']
    sname= data['lastName']
    email=data['email']
    phone=data['phone']
    address=data['address']
    qualifications=data['qualifications']
    exp=data['experience']
    cur = mysql.connection.cursor()
    
    sql="SELECT MAX(id) + 1 AS next_id FROM teacher"
    cur.execute(sql)
    result = cur.fetchone()
    next_id = result[0]
    
    if next_id is None:
        next_id=1    

    query = "INSERT INTO teacher (id,first_name,surname,email,phone,address,qualifications,experience) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    cur.execute(query, (next_id,fname,sname,email,phone,address,qualifications,exp))
    
    mysql.connection.commit()
    cur.close()
    
    return jsonify({'message': 'Teacher created successfully'})

@app.route('/getTeachers', methods=['GET'])
def get_teachers():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT id, first_name,surname,course,address,phone FROM teacher where deleted=0")
        teachers= cur.fetchall()
        cur.close()
        return jsonify(teachers)
    except Exception as e:
        print('Error fetching teachers:', e)
        return jsonify([])

@app.route('/deleteTeacher/<int:teacher_id>', methods=['DELETE'])
def delete_teacher(teacher_id):
    try:
        cur = mysql.connection.cursor()
        cur.execute("UPDATE teacher SET deleted=1 WHERE id = %s", (teacher_id,))
        mysql.connection.commit()
        cur.close()
        return jsonify({'message': 'teacher deleted successfully'})
    except Exception as e:
        print('Error deleting teacher:', e)
        return jsonify({'message': 'Error deleting student'})

@app.route('/getTeacher/<int:teacher_id>', methods=['GET'])
def get_teacher(teacher_id):
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT id, first_name, surname, course, address, phone,course FROM teacher WHERE id = %s", (teacher_id,))
        teacher = cur.fetchone()
        cur.close()
        if teacher:
            return jsonify(teacher)
        else:
            return jsonify({'message': 'teacher not found'})
    except Exception as e:
        print('Error fetching student:', e)
        return jsonify({'message': 'Error fetching teacher'})

@app.route('/updateTeacher/<int:teacher_id>', methods=['PUT'])
def update_teacher(teacher_id):
    data = request.get_json()
    fname = data['firstName']
    sname = data['lastName']
    age = data['age']
    address = data['address']
    phone = data['phone']
    cur = mysql.connection.cursor()

    query = "UPDATE teacher SET first_name=%s, surname=%s, course=%s, address=%s, phone=%s WHERE id=%s"
    cur.execute(query, (fname, sname, age, address, phone, student_id))

    mysql.connection.commit()
    cur.close()

    return jsonify({'message': 'teacher updated successfully'})
########################################################################################################################

############################LEAVES####################################################################
@app.route('/requestLeave/<string:email>', methods=['POST'])
def request_leave(email):
    try:
        leave_data = request.get_json()
        leave_type = leave_data.get('leaveType')
        reason = leave_data.get('reason')
        from_date = leave_data.get('fromDate')
        to_date = leave_data.get('toDate')

        cur = mysql.connection.cursor()
        
        sql="SELECT MAX(id) + 1 AS next_id FROM leaves"
        cur.execute(sql)
        result = cur.fetchone()
        next_id = result[0]
    
        if next_id is None:
            next_id=1  
            
        cur.execute(
            "INSERT INTO leaves (id,email, leave_type, reason, from_date, to_date) VALUES (%s, %s, %s, %s, %s,%s)",
            (next_id,email, leave_type, reason, from_date, to_date)
        )
        mysql.connection.commit()
        cur.close()

        return jsonify({'message': 'Leave request has been sent'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/getLeaveRequests', methods=['GET'])
def get_LeaveRequests():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT concat(teacher.first_name,' ',teacher.surname) as name,leaves.* FROM leaves inner join teacher on teacher.email=leaves.email and leaves.approved=0 and leaves.rejected=0")
        leaves = cur.fetchall()
        cur.close()
        return jsonify(leaves)
    except Exception as e:
        print('Error fetching leave requests:', e)
        return jsonify([])
    
@app.route('/approveLeave/<int:leaveId>', methods=['DELETE'])
def approve_leave(leaveId):
    try:
        cur = mysql.connection.cursor()
        cur.execute("UPDATE leaves SET approved=1 WHERE id = %s", (leaveId,))
        mysql.connection.commit()
        cur.close()
        return jsonify({'message': 'leave approved succesfully'})
    except Exception as e:
        print('Error deleting student:', e)
        return jsonify({'message': 'Error approving leave'})
    
@app.route('/rejectLeave/<int:leaveId>', methods=['DELETE'])
def reject_leave(leaveId):
    try:
        reason = request.json.get('reason')
        cur = mysql.connection.cursor()
        cur.execute("UPDATE leaves SET rejected=1,reject_reason=%s WHERE id = %s", (reason, leaveId))
        mysql.connection.commit()
        cur.close()
        return jsonify({'message': 'leave rejected succesfully'})
    except Exception as e:
        print('Error deleting student:', e)
        return jsonify({'message': 'Error rejecting leave'})
#################################################################
############################ADmission####################################################################
@app.route('/EntranceForm_courses', methods=['GET'])
def EntranceForm_courses():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT name FROM course')
        courses = [course[0] for course in cursor.fetchall()]
        cursor.close()
        return jsonify(courses)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
# @app.route('/enteranceForm', methods=['POST'])
# def enterance_form():
#     try:
#         email = request.form.get('email')
#         fullname = request.form.get('fullName')
#         course = request.form.get('selectedCourse')
#         photo = request.files.get('photo')
#         marksheet = request.files.get('marksheet')

#         # Check if the required fields are present
#         if not fullname or not course or not photo or not marksheet:
#             return jsonify({'error': 'Incomplete form data'}), 400

#         # Check if the files have allowed extensions
#         allowed_extensions = {'jpg', 'jpeg', 'png', 'pdf'}
#         if not (photo.filename.endswith(tuple(allowed_extensions)) and
#                 marksheet.filename.endswith(tuple(allowed_extensions))):
#             return jsonify({'error': 'Invalid file extensions'}), 400

#         # Save the files to the server
#         # photo.filename =  eamil+'_'+photo.filename 
#         photo_filename = secure_filename(photo.filename)
#         marksheet_filename = secure_filename(marksheet.filename)
#         photo_path = os.path.join(app.config['UPLOAD_FOLDER'], photo_filename)
#         marksheet_path = os.path.join(app.config['UPLOAD_FOLDER'], marksheet_filename)
#         photo.save(photo_path)
#         marksheet.save(marksheet_path)

#         # Save the form data to the MySQL database
#         cursor = mysql.connection.cursor()
#         query = "INSERT INTO enterance_forms (email,fullname, course, photo, marksheet) VALUES (%s,%s, %s, %s, %s)"
#         cursor.execute(query, (email,fullname, course, photo_path, marksheet_path))
#         mysql.connection.commit()
#         cursor.close()

#         return 'Form submitted successfully!'
        
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500
# def get_b2_file_url(bucket_name, file_name):
#     b2_api = authenticate_b2()
#     file_info = b2_api.get_file_info_by_name(bucket_name, file_name)
#     download_url = b2_api.get_download_url_by_id(file_info.file_id)
#     return download_url
# @app.route('/getEnteranceForms', methods=['GET'])
# def getEnteranceForms():
#     try:
#         cur = mysql.connection.cursor()
#         cur.execute("SELECT * from enterance_forms where elligible not in (1,2)")
#         forms = cur.fetchall()
#         cur.close()
        
#         for form in forms:
#             print(form)
#             photo_url = get_b2_file_url('vue-uploads', form[4])
#             marksheet_url = get_b2_file_url('vue-uploads', form[5])
#             print(photo_url)
#             form[4] = photo_url
#             form[5] = marksheet_url
            
#         return jsonify(forms)
#     except Exception as e:
#         print('Error fetching leave requests:', e)
#         return jsonify([])

@app.route('/getElligibleApplicants', methods=['GET'])
def getElligibleApplicants():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT id,email,fullname,course from enterance_forms where elligible=1")
        forms = cur.fetchall()
        cur.close()
        return jsonify(forms)
    except Exception as e:
        print('Error fetching leave requests:', e)
        return jsonify([])
    
@app.route('/uploads/<filename>', methods=['GET'])
def serve_uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/verifyApplicant/<int:id>/<string:res>', methods=['PUT'])
def verify_applicant(id,res):
    try:
        if(res=='A'):
            cur = mysql.connection.cursor()
            cur.execute("UPDATE enterance_forms set elligible=1  where id=%s ",(id,))    
            mysql.connection.commit()
            cur.close()
        elif(res=='R'):
            cur = mysql.connection.cursor()
            cur.execute("UPDATE enterance_forms set elligible=2  where id=%s ",(id,))    
            mysql.connection.commit()
            cur.close()
        return jsonify('success')
    except Exception as e:
        print('Error updating request:', e)
        return jsonify([])
##########################################################################################
def send_email(recipient, subject, body):
    # SMTP server configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # or your SMTP server port
    username = 'bendias45@gmail.com'
    password = 'hjdhgadpsvnptrbr'

    # Create a multipart message
    message = MIMEMultipart()
    message['From'] = username
    message['To'] = recipient
    message['Subject'] = subject

    # Add body to the message
    message.attach(MIMEText(body, 'plain'))

    try:
        # Create a SMTP session
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(username, password)
            server.sendmail(username, recipient, message.as_string())

        return 'Email sent successfully'
    except Exception as e:
        return f'An error occurred: {str(e)}'
@app.route('/send-email', methods=['POST'])
def send_email_route():
    data = request.get_json()
    selectedCourse=data['selectedCourse']
    
    cur = mysql.connection.cursor()
    cur.execute("SELECT email from enterance_forms where elligible=1 and course=%s",(selectedCourse,))
    applicants = cur.fetchall()
    cur.close()
    
    print()
    for applicant in applicants:
        for email in applicant:
            recipient = email
            subject = 'Enterance Test Details'
            body = data['body']

    result = send_email(recipient, subject, body)
    return result
###########################
# Configuration for Backblaze B2
REPO_OWNER = 'renedias15'
REPO_NAME = 'college_management'
#GITHUB_TOKEN = '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'

@app.route('/enteranceForm', methods=['POST'])
def entrance_form():
    try:
        email = request.form.get('email')
        fullname = request.form.get('fullName')
        course = request.form.get('selectedCourse')
        photo = request.files.get('photo')
        marksheet = request.files.get('marksheet')
        
        # Check if the required fields are present
        if not fullname or not course or not photo or not marksheet:
            return jsonify({'error': 'Incomplete form data'}), 400

        # Check if the files have allowed extensions
        allowed_extensions = {'jpg', 'jpeg', 'png', 'pdf'}
        if not (photo.filename.endswith(tuple(allowed_extensions)) and
                marksheet.filename.endswith(tuple(allowed_extensions))):
            return jsonify({'error': 'Invalid file extensions'}), 400
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT name from token")
        result = cursor.fetchone()
        GITHUB_TOKEN=result[0]
        def upload_file_to_github(file, file_name):
            g = Github(GITHUB_TOKEN)
            repo = g.get_user(REPO_OWNER).get_repo(REPO_NAME)
            contents = file.read()
            path = f"{folder_name}/{file_name}"
            try:
                repo.create_file(path, f"Upload {file_name}", contents, branch='main')
                return 'File uploaded successfully!'
            except Exception as e:
                if 'sha' in str(e):
                    return 'File already exists.'
                else:
                    return f'Error uploading file: {str(e)}'

        # Save the files to Backblaze B2
        folder_name = "uploads"
        photo_filename = secure_filename(photo.filename)
        marksheet_filename = secure_filename(marksheet.filename)
        upload_file_to_github(photo, photo_filename)
        upload_file_to_github(marksheet, marksheet_filename)
        
        # Save the form data to the MySQL database
        cursor = mysql.connection.cursor()
        query = "INSERT INTO enterance_forms (email, fullname, course, photo, marksheet) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (email, fullname, course, photo_filename, marksheet_filename))
        mysql.connection.commit()
        cursor.close()

        return 'Form submitted successfully!'

    except Exception as e:
        return jsonify({'error': str(e)}), 500

def get_github_file_link(file_path):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT name from token")
    result = cursor.fetchone()
    GITHUB_TOKEN=result[0]
    g = Github(GITHUB_TOKEN)
    repo = g.get_repo(f"{REPO_OWNER}/{REPO_NAME}")
    file_contents = repo.get_contents(file_path)
    return file_contents.download_url
    
@app.route('/getEnteranceForms', methods=['GET'])
def getEnteranceForms():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * from enterance_forms where elligible not in (1,2)")
        forms = cur.fetchall()
        cur.close()

        updated_forms = []
        for form in forms:
            form_list = list(form)  # Convert tuple to list
            print(form_list)
            photo_file_path = f"uploads/{form[4]}"  # Assuming form[4] contains the photo file name
            marksheet_file_path = f"uploads/{form[5]}"  # Assuming form[5] contains the marksheet file name
            photo_url = get_github_file_link(photo_file_path)
            marksheet_url = get_github_file_link(marksheet_file_path)
            print(photo_url)
            form_list[4] = photo_url
            form_list[5] = marksheet_url
            updated_forms.append(tuple(form_list))  # Convert list back to tuple and add to updated forms list

        return jsonify(updated_forms)
    except Exception as e:
        print('Error fetching leave requests:', e)
        return jsonify([])
    
#################
@app.route('/uploadMeritList', methods=['POST'])
def create_meritList():
    try:
        course = request.form.get('course')
        file_attached = request.files.get('file')
        print(course)
        # Check if the required fields are present
        if not file_attached or not course:
            return jsonify({'error': 'Incomplete form data'}), 400

        # Check if the files have allowed extensions
        allowed_extensions = {'jpg', 'jpeg', 'png', 'pdf'}
        if not (file_attached.filename.endswith(tuple(allowed_extensions))):
            return jsonify({'error': 'Invalid file extensions'}), 400

        
        def upload_file_to_github(file, file_name):
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT name from token")
            result = cursor.fetchone()
            GITHUB_TOKEN=result[0]
            g = Github(GITHUB_TOKEN)
            repo = g.get_user(REPO_OWNER).get_repo(REPO_NAME)
            contents = file.read()
            path = f"{folder_name}/{file_name}"
            try:
                repo.create_file(path, f"Upload {file_name}", contents, branch='main')
                return 'File uploaded successfully!'
            except Exception as e:
                if 'sha' in str(e):
                    return 'File already exists.'
                else:
                    return f'Error uploading file: {str(e)}'

        # Save the files to Backblaze B2
        folder_name = "uploads"
        filename = secure_filename(file_attached.filename)
        upload_file_to_github(file_attached,filename)
        

        try:
            cursor = mysql.connection.cursor()
            query = "INSERT INTO merit_list (course,file) VALUES (%s, %s)"
            cursor.execute(query, (course, filename))
            mysql.connection.commit()
            cursor.close()
        except Exception as e:
            return jsonify({'error': str(e)}), 500

        return 'Form submitted successfully!'

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/merit-lists', methods=['GET'])
def get_merit_lists():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * from merit_list ")
        forms = cur.fetchall()
        cur.close()

        updated_forms = []
        for form in forms:
            form_list = list(form)  # Convert tuple to list
            print(form_list)
            photo_file_path = f"uploads/{form[2]}"  # Assuming form[4] contains the photo file name
            photo_url = get_github_file_link(photo_file_path)
            print(photo_url)
            form_list[2] = photo_url
            updated_forms.append(tuple(form_list))  # Convert list back to tuple and add to updated forms list

        return jsonify(updated_forms)
    except Exception as e:
        print('Error fetching leave requests:', e)
        return jsonify([])
#################
@app.route('/getSubjects/<string:course>', methods=['GET'])    ## this is to fetch subjects for particular course
def getSubjects(course):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT name FROM subject where course=%s',(course,))
        Subjects = [course[0] for course in cursor.fetchall()]
        cursor.close()
        return jsonify(Subjects)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/getTeacher-name', methods=['GET'])     ## fetches names and courses associated to teacher
def getTeacher_name():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT concat(first_name," ",surname),course,teacher.id,GROUP_CONCAT(subject) from teacher left JOIN teachersubjects on teacher.id=teachersubjects.teacher_id and teachersubjects.deleted=0 group by course')
        res= cursor.fetchall()
        cursor.close()
        return jsonify(res)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/saveSubject', methods=['POST'])
def save_subject():
    try:
        data = request.get_json()
        teacher_id= data['id']
        subject= data['subject']
        cur = mysql.connection.cursor()
        
        sql="SELECT MAX(id) + 1 AS next_id FROM teachersubjects"
        cur.execute(sql)
        result = cur.fetchone()
        next_id = result[0]
        
        if next_id is None:
            next_id=1  

        sql="SELECT teacher_id,subject FROM teachersubjects where teacher_id=%s and subject=%s"
        cur.execute(sql,(teacher_id,subject))
        res = cur.fetchone()
        
        if res is None:
        
            query = "INSERT INTO teachersubjects (id,teacher_id,subject) VALUES (%s,%s,%s)"
            cur.execute(query, (next_id,teacher_id,subject))
            
            mysql.connection.commit()
            cur.close()
            
            return jsonify({'message': 'added successfully'})
        return jsonify({'message':'already present'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
      
# @app.route('/getSubject/<int:id>', methods=['GET'])
# def get_subject(id):
#     try:
#         cursor = mysql.connection.cursor()
#         cursor.execute('SELECT subject from teachersubjects INNER JOIN teacher on teacher.id=teachersubjects.teacher_id where teacher_id=%s',(id,))
#         res= cursor.fetchall()
#         cursor.close()
#         return jsonify(res)
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500
##################
if __name__ == '__main__':
    app.run(debug=True)
