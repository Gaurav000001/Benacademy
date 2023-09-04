from uuid import UUID
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Student
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def get_students(request):
    if request.method == "GET":
        
        students = Student.objects.all()
        data = [{
                'student_id': student.student_id, 
                'name': student.name, 
                'gender': student.gender,
                'date_of_birth': student.date_of_birth, 
                'major': student.major,
                'email': student.email, 
                'contact_number': student.contact_number
                } for student in students]
        
        return JsonResponse({'data': data}, safe=False, status=200)
        
    else:
        return JsonResponse({'message': "method should be GET"}, status=400)
        






@csrf_exempt
def register_student(request):
    if request.method == "POST":
        try:
            student_data = json.loads(request.body)
            
            # check if student with same email already exists
            email = student_data.get('email')
            student_with_email = Student.objects.filter(email = email)
            if student_with_email:
                return JsonResponse({'message': 'Student with email already exists, try another email or login'}, status=400)
            
            # check if student with same contact number already exists
            contact_number = student_data.get('contact_number')
            
            # check if contact_number is of 10 digit or not
            if len(contact_number) < 10 or len(contact_number) > 10:
                return JsonResponse({'message': 'contact number should be of 10 digists only'}, status=400)
            
            
            student_with_contact_number = Student.objects.filter(contact_number = contact_number)
            if student_with_contact_number:
                return JsonResponse({'message': 'Student with contact number already exists, try another contact number or login'}, status=400)
            
                
            # student = Student(**student_data)
            student = Student(
                name = student_data.get('name'),
                gender = student_data.get('gender'),
                date_of_birth = student_data.get('date_of_birth'),
                major = student_data.get('major'),
                email = student_data.get('email'),
                contact_number = student_data.get('contact_number')
            )
            student.save()
            
            created_student = {
                'student_id': student.student_id, 
                'name': student.name, 
                'gender': student.gender,
                'date_of_birth': student.date_of_birth, 
                'major': student.major,
                'email': student.email, 
                'contact_number': student.contact_number
            }
            return JsonResponse({'message': 'Student created successfully', 'data': created_student}, safe=False, status=201)
        
        except Exception as e:
            return JsonResponse({'message': 'Student not created'}, status=400)
    
    else:
        return JsonResponse({'message': "method should be POST"}, status=400)
        
        
        
        
        
        
        
@csrf_exempt
def get_student(request, student_id):
    if request.method == "GET":
        try:
            student = get_object_or_404(Student, pk=student_id)
            data = {
                'student_id': student.student_id, 
                'name': student.name, 
                'gender': student.gender,
                'date_of_birth': student.date_of_birth, 
                'major': student.major,
                'email': student.email, 
                'contact_number': student.contact_number
            }
            return JsonResponse({'data': data}, status=200)
        except Exception as e:
            return JsonResponse({'message': 'Student Not Found'}, status=404)

    else:
        return JsonResponse({'message': "method should be GET"}, status=400)







@csrf_exempt
def update_student(request, student_id):
    if request.method == 'PUT':
        try:
            # changing type of student_id from str to UUID for comparisons
            student_id = UUID(student_id)
            student = get_object_or_404(Student, pk=student_id)
            student_data = json.loads(request.body)
            
            # check if student with same email already exists
            email = student_data.get('email')
            student_with_email = Student.objects.filter(email = email)
            if student_with_email:
                if student_with_email[0].student_id is not student_id:
                    return JsonResponse({'message': 'Student with email already exists, try another email'}, status=400)
            
            # check if student with same contact number already exists
            contact_number = student_data.get('contact_number')
            
            # check if contact_number is of 10 digit or not
            if len(contact_number) < 10 or len(contact_number) > 10:
                return JsonResponse({'message': 'contact number should be of 10 digists only'}, status=400)
            
            
            student_with_contact_number = Student.objects.filter(contact_number = contact_number)
            if student_with_contact_number:
                if student_with_contact_number[0].student_id is not student_id:
                    return JsonResponse({'message': 'Student with contact number already exists, try another contact number'}, status=400)

            # extract data from request body to update student
            student_data_extracted = {
                "name" : student_data.get('name'),
                "gender" : student_data.get('gender'),
                "date_of_birth" : student_data.get('date_of_birth'),
                "major" : student_data.get('major'),
                "email" : student_data.get('email'),
                "contact_number" : student_data.get('contact_number')
            }

            # setting up the values to update student
            for key, value in student_data_extracted.items():
                setattr(student, key, value)

            student.save()
            
            updated_student = {
                'student_id': student.student_id, 
                'name': student.name, 
                'gender': student.gender,
                'date_of_birth': student.date_of_birth, 
                'major': student.major,
                'email': student.email, 
                'contact_number': student.contact_number
            }
            
            return JsonResponse({'message': 'Student updated successfully', 'data': updated_student}, status=200)
        except Exception as e:
            return JsonResponse({'message': 'Student Not Found'}, status=404)

    else:
        return JsonResponse({'message': "method should be PUT"}, status=400)







@csrf_exempt
def delete_student(request, student_id):
    if request.method == 'DELETE':
        try:
            student = get_object_or_404(Student, pk=student_id)
            
            deleted_student = {
                'student_id': student.student_id, 
                'name': student.name, 
                'gender': student.gender,
                'date_of_birth': student.date_of_birth, 
                'major': student.major,
                'email': student.email, 
                'contact_number': student.contact_number
            }
            student.delete()
            
            return JsonResponse({'message': 'Student deleted successfully', 'data': deleted_student}, status=200)
        except Exception as e:
            return JsonResponse({'message': 'Student Not Found'}, status=404)
    
    else:
        return JsonResponse({'message': "method should be DELETE"}, status=400)
