import json
from django.http import JsonResponse
from django.shortcuts import render
from enrollments.models import Enrollment
from courses.models import Course

from students.models import Student

# Create your views here.

# Used to enroll one student to course
def enroll_student_to_course(request, student_id, course_id):
    if request.method == 'POST':
        try:
            student = Student.objects.get(student_id = student_id)
            course = Course.objects.get(course_id = course_id)
            if student is None:
                return JsonResponse({'message': 'Student Not Found'}, status=404)
            if course is None:
                return JsonResponse({'message': 'Course Not Found'}, status=404)
            
            existing_enrollment = Enrollment.objects.filter(student=student, course=course).first()
            if existing_enrollment is not None:
                return JsonResponse({'message': 'Student is already in the Course'}, status=400)
            
            enrollment = Enrollment.objects.create(
                student = student,
                course = course
            )
            
            created_enrollment = {
                'enrollment_id': enrollment.enrollment_id,
                "student": {
                    "student_id": student.student_id,
                    'student_name': student.name,
                },
                'course': {
                    'course_id': course.course_id,
                    'course_code': course.course_code,
                    'course_name': course.course_name
                }
            }
            return JsonResponse({'message': 'student enrolled in course successfully', 'data': created_enrollment}, status=201)
        
        except Exception as e:
            return JsonResponse({"message": str(e)}, status=400)
    else:
        return JsonResponse({'message': "method should be POST"}, status=400)
    
    


def bulk_enrollment(request, course_id):
    if request.method == 'POST':
        try:
            course = Course.objects.get(course_id=course_id)
            if course is None:
                return JsonResponse({'message': 'Course Not Found'}, status=404)

            created_enrollments = []
            errors = []
            
            data = json.loads(request.body)
            student_ids = data.get('student_ids')

            for student_id in student_ids:
                student = Student.objects.get(student_id=student_id)
                if student is None:
                    errors.append(f'Student with student_id: {student_id} Not Found')

                existing_enrollment = Enrollment.objects.filter(student=student, course=course).first()
                if existing_enrollment:
                    continue  # Skip this student, as they are already enrolled

                # Create a new enrollment for the student and course
                enrollment = Enrollment.objects.create(student=student, course=course)

                # Add the enrollment details to the list
                created_enrollments.append({
                    'enrollment_id': enrollment.enrollment_id,
                    'student': {
                        'student_id': student.student_id,
                        'student_name': student.name,
                    },
                    'course': {
                        'course_id': course.course_id,
                        'course_code': course.course_code,
                        'course_name': course.course_name,
                    }
                })

            # Return a JSON response with the created enrollments
            return JsonResponse({'message': 'Bulk enrollment successful', 'data': created_enrollments}, status=201)

        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)
    else:
        return JsonResponse({'message': 'Method should be POST'}, status=400)