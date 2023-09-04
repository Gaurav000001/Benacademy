from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
import json
from instructors.models import Instructor
from courses.models import Course
from departments.models import Department

# Create your views here.
@csrf_exempt
def create_department(request):
    if request.method == "POST":
        try:
            
            department_data = json.loads(request.body)
            department_name = department_data.get('department_name')
            parent_department_id = department_data.get('parent_department_id', None)
            
            if parent_department_id is not None:
                parent_department = get_object_or_404(Department, pk=parent_department_id)
                department = Department.objects.create(name=department_name, parent_department=parent_department)
                
                created_department = {
                    'department_id': department.department_id,
                    'department_name': department.name,
                    'parent_department_id': parent_department_id
                }
                return JsonResponse({'message': 'department created successfully', 'data': created_department}, safe=False, status=200)
            else:
                department = Department.objects.create(name=department_name)
                
                created_department = {
                    'department_id': department.department_id,
                    'department_name': department.name
                }
                return JsonResponse({'message': 'department created successfully', 'data': created_department}, safe=False, status=200)
                
            
        except Exception as e:
            return JsonResponse({'message': 'Department not created'}, status=400)
        
        
    else:
        return JsonResponse({'message': "method should be POST"}, status=400)
    
    
    


# Get all departments having no parent i.e. all base departments
@csrf_exempt
def get_departments(request):
    if request.method=="GET":
        departments = Department.objects.filter(parent_department=None)
        departments_data = [{
            'department_id': department.department_id,
            'department_name': department.name
        } for department in departments]
        
        return JsonResponse({'data': departments_data}, status=200)
        
    else:
        return JsonResponse({'message': "method should be GET"}, status=400)
    
    
    
    
@csrf_exempt
def get_department(request, department_id):
    if request.method == "GET":
        try:
            department = get_object_or_404(Department, pk=department_id)
            sub_departments = Department.objects.filter(parent_department=department)
            courses = Course.objects.filter(department=department)
            instructors = Instructor.objects.filter(departments__department_id=department_id)
            
            department_data = {
                'department_id': department_id,
                'name': department.name,
                'sub_departments': [{
                    'sub_department_id': sub_department.department_id,
                    'sub_department_name': sub_department.name
                } for sub_department in sub_departments],
                'courses': [{
                    'course_id': course.course_id,
                    'course_code': course.course_code,
                    'course_name': course.course_name
                } for course in courses],
                'instructors': [{
                    'instructor_id': instructor.instructor_id,
                    'instructor_name': instructor.name
                } for instructor in instructors]
            }
            return JsonResponse({'data': department_data}, status=200)
            
            
        except Exception as e:
            return JsonResponse({'message': 'Department not found'}, status=404)
    else:
        return JsonResponse({'message': "method should be GET"}, status=400)
    
    




# used to update the department name
@csrf_exempt
def update_department(request, department_id):
    if request.method == "PUT":
        try:
            department = get_object_or_404(Department, pk=department_id)
            name = (json.loads(request.body)).get('name')
            
            if name:
                department.name = name
                department.save()
                sub_departments = Department.objects.filter(parent_department=department)
                courses = Course.objects.filter(department=department)
                instructors = Instructor.objects.filter(departments__department_id=department_id)
                
                department_data = {
                    'department_id': department_id,
                    'name': department.name,
                    'sub_departments': [{
                        'sub_department_id': sub_department.department_id,
                        'sub_department_name': sub_department.name
                    } for sub_department in sub_departments],
                    'courses': [{
                        'course_id': course.course_id,
                        'course_code': course.course_code,
                        'course_name': course.course_name
                    } for course in courses],
                    'instructors': [{
                        'instructor_id': instructor.instructor_id,
                        'instructor_name': instructor.name
                    } for instructor in instructors]
                }
                return JsonResponse({'message': 'department updated successfully', 'data': department_data}, status=200)
                
            
        except Exception as e:
            return JsonResponse({'message': 'Department not found'}, status=404)
    else:
        return JsonResponse({'message': "method should be PUT"}, status=400)
    
    
    
    


@csrf_exempt
def delete_department(request, department_id):
    if request.method == "DELETE":
        try:
            department = get_object_or_404(Department, pk=department_id)
            sub_departments = Department.objects.filter(parent_department=department)
            courses = Course.objects.filter(department=department)
            instructors = Instructor.objects.filter(departments__department_id=department_id)
            department_data = {
                'department_id': department_id,
                'name': department.name,
                'sub_departments': [{
                    'sub_department_id': sub_department.department_id,
                    'sub_department_name': sub_department.name
                } for sub_department in sub_departments],
                'courses': [{
                    'course_id': course.course_id,
                    'course_code': course.course_code,
                    'course_name': course.course_name
                } for course in courses],
                'instructors': [{
                    'instructor_id': instructor.instructor_id,
                    'instructor_name': instructor.name
                } for instructor in instructors]
            }
            department.delete()
            
            return JsonResponse({'message':'department deleted successfully', 'data': department_data}, status=200)
                
            
        except Exception as e:
            return JsonResponse({'message': 'Department not found'}, status=404)
    else:
        return JsonResponse({'message': "method should be DELETE"}, status=400)