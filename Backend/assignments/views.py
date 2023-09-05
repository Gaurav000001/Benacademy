import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from submissions.models import Submission
from enrollments.models import Enrollment
from students.models import Student
from assignments.models import Assignment
from django.core.exceptions import ObjectDoesNotExist

from courses.models import Course

# Create your views here.
def create_assignment(request, course_id):
    if request.method == "POST":
        try:
            course = get_object_or_404(Course, pk=course_id)
            data = json.loads(request.body)
            
            title = data.get('title')
            description = data.get('description')
            start_at = data.get('start_at')
            end_at = data.get('end_at')
            
            assignment = Assignment.objects.create(
                title = title,
                description = description,
                start_at = start_at,
                end_at = end_at,
                course = course
            )
            
            created_assignment = {
                'assignment_id': assignment.assignment_id,
                'title': assignment.title,
                'description': assignment.description,
                'start_at': assignment.start_at,
                'end_at': assignment.end_at
            }
            return JsonResponse({'message': 'Assignment created successfully', 'data': created_assignment}, status=201)
        
        
        except Exception as e:
            return JsonResponse({"message": "Something went wrong"}, status=500)
    else:
        return JsonResponse({'message': "method should be POST"}, status=400)
    
    
    
    
    
def get_student_assignments(request, student_id):
    if request.method == "GET":
        try:
            try:
                student = Student.objects.get(student_id = student_id)
            except ObjectDoesNotExist:
                return JsonResponse({'message': 'Student Not Found'}, status=404)
            
            enrollments = Enrollment.objects.filter(student=student)
            student_assignments = []
            
            for enrollment in enrollments:
                course = enrollment.course
                assignments = Assignment.objects.filter(course = course).order_by('-start_at')
                
                for assignment in assignments:
                    submission = Submission.objects.filter(student=student, assignment=assignment).first()
                    
                    student_assignments.append(
                        {
                            'assignment_id': assignment.assignment_id,
                            'title': assignment.title,
                            'submitted': True if submission else False
                        }
                    )
        
            return JsonResponse({'data': student_assignments}, status=200)
        
        except Exception as e:
            return JsonResponse({"message": "Something went wrong"}, status=500)
    else:
        return JsonResponse({'message': "method should be POST"}, status=400)
    
    
    
    
def delete_assignment(request, assignment_id):
    if request.method == "DELETE" :
        try:
            assignment = get_object_or_404(Assignment, pk=assignment_id)
            deleted_assignment = {
                'assignment_id': assignment.assignment_id,
                'title': assignment.title,
                'description': assignment.description,
                'start_at': assignment.start_at,
                'end_at': assignment.end_at
            }
            assignment.delete()
            return JsonResponse({'message': 'Assignmnet deleted successfully', 'data': deleted_assignment}, status=200)
        
        
        except Exception as e:
            return JsonResponse({"message": "Assignmnet Not Found"}, status=404)
    else:
        return JsonResponse({'message': "method should be POST"}, status=400)