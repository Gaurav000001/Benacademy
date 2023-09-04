import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from enrollments.models import Enrollment
from students.models import Student
from courses.models import Course
from instructors.models import Instructor
from django.views.decorators.csrf import csrf_exempt

from departments.models import Department

# Create your views here.
@csrf_exempt
def create_course(request, department_id):
    if request.method == "POST":
        try:
            department = get_object_or_404(Department, pk=department_id)
            course_data = json.loads(request.body)
            instructor = get_object_or_404(Instructor, pk=course_data.get('instructor_id'))
            
            course_code = course_data.get('course_code')
            course_with_course_code = Course.objects.filter(course_code = course_code)
            if course_with_course_code:
                return JsonResponse({'message': 'course with course code already exists, choose another'}, status=400)
            
            course = Course.objects.create(
                course_code = course_data.get('course_code'),
                course_name = course_data.get('course_name'),
                credits = course_data.get('credits'),
                description = course_data.get('description'),
                instructor = instructor,
                department = department
            )
            
            created_course = {
                'course_id': course.course_id,
                'course_name': course.course_name,
                'course_code': course.course_code,
                'credits': course.credits,
                'department': {
                    'department_id' : department.department_id,
                    'department_name': department.name
                },
                'instructor': {
                    'instructor_id': instructor.instructor_id,
                    'instructor_name': instructor.name
                }
            }
            return JsonResponse({'message': 'course created successfully', 'data': created_course}, status=201)
            
            
        except Exception as e:
            return JsonResponse({"message": str(e)}, status=400)
        
    else:
        return JsonResponse({'message': "method should be POST"}, status=400)
    




@csrf_exempt
def get_all_courses(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        
        courses_data = [{
            'course_id': course.course_id,
            'course_name': course.course_name,
            'course_code': course.course_code,
            'credits': course.credits,
            'department': {
                'department_id' : course.department.department_id,
                'department_name': course.department.name
            },
            'instructor': {
                'instructor_id': course.instructor.instructor_id,
                'instructor_name': course.instructor.name
            }
        } for course in courses]
        
        return JsonResponse({'data': courses_data}, status=200)
    
    else:
        return JsonResponse({'message': "method should be GET"}, status=400)
    
    
    
    
    
@csrf_exempt
def change_course_instructor(request, course_id, instructor_id):
    if request.method == "PUT":
        try:
            course = Course.objects.get(course_id = course_id)
            if course is None:
                return JsonResponse({'message': 'Course Not Found'}, status=404)
            
            instructor = Instructor.objects.get(instructor_id=instructor_id)
            if instructor is None:
                return JsonResponse({'message': 'Instructor Not Found'}, status=404)
            
            course.instructor = instructor
            course.save()
            
            updated_course = {
                'course_id': course.course_id,
                'course_name': course.course_name,
                'course_code': course.course_code,
                'credits': course.credits,
                'department': {
                    'department_id' : course.department.department_id,
                    'department_name': course.department.name
                },
                'instructor': {
                    'instructor_id': course.instructor.instructor_id,
                    'instructor_name': course.instructor.name
                }
            }
            
            return JsonResponse({'message': 'Instructor changed successfully', 'data': updated_course}, status=200)

        
        except Exception as e:
            return JsonResponse({'message': 'something gone wrong'}, status=500)
    else:
        return JsonResponse({'message': "method should be PUT"}, status=400)
    
    
    
    
    
    


@csrf_exempt
def get_student_courses(request, student_id):
    if request.method == 'GET':
        try:
            student = get_object_or_404(Student, pk=student_id)
            student_enrollments = Enrollment.objects.filter(student=student)
            
            courses = [{
                'course_id': student_enrollment.course.course_id,
                'course_name': student_enrollment.course.course_name,
                'course_code': student_enrollment.course.course_code,
                'credits': student_enrollment.course.credits,
                'department': {
                    'department_id' : student_enrollment.course.department.department_id,
                    'department_name': student_enrollment.course.department.name
                },
                'instructor': {
                    'instructor_id': student_enrollment.course.instructor.instructor_id,
                    'instructor_name': student_enrollment.course.instructor.name
                }
            } for student_enrollment in student_enrollments]
            return JsonResponse({'data': courses}, status=200)
            
        except Exception as e:
            return JsonResponse({"message": str(e)}, status=400)
        
    else:
        return JsonResponse({'message': "method should be GET"}, status=400)
    
    


@csrf_exempt
def delete_course(request, course_id):
    if request.method == "DELETE":
        try:
            course = get_object_or_404(Course, pk=course_id)
            deleted_course = {
                'course_id': course.course_id,
                'course_name': course.course_name,
                'course_code': course.course_code,
                'credits': course.credits,
                'department': {
                    'department_id' : course.department.department_id,
                    'department_name': course.department.name
                },
                'instructor': {
                    'instructor_id': course.instructor.instructor_id,
                    'instructor_name': course.instructor.name
                }
            }
            return JsonResponse({'message': 'Course deleted successfully', 'data': deleted_course}, status=200)
            
        except Exception as e:
            return JsonResponse({'message': 'Course Not Found'}, status=404)
        
    else:
        return JsonResponse({'message': "method should be DELETE"}, status=400)