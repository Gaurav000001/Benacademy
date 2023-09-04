import datetime
from django.http import JsonResponse
from submissions.models import Submission
from students.models import Student

from assignments.models import Assignment

# Create your views here.
def create_submission(request, assignment_id, student_id):
    if request.method == 'POST':
        try:
            assignment = Assignment.objects.get(assignment_id=assignment_id)
            if assignment is None:
                return JsonResponse({'message': "Assignment Not Found"}, status=404)
            
            student = Student.objects.get(student_id=student_id)
            if student is None:
                return JsonResponse({'message': 'Student Not Found'}, status=404)
            
            existing_submission = Submission.objects.filter(student=student, assignment=assignment).first()
            if existing_submission:
                return JsonResponse({'message': "Assignment already been submitted"}, status=400)
            
            
            submission = Submission.objects.create(
                submitted_at = datetime.datetime.now(),
                status = "Submitted" if (assignment.end_at - datetime.datetime.now())>0 else "Late",
                remarks = "Submitted the Assignment",
                student = student,
                assignment = assignment
            )
            
            created_submission = {
                'submission_id': submission.submission_id,
                'status': submission.status,
                'remarks': submission.remarks,
                'student': {
                    'student_id': student.student_id,
                    'name': student.name
                },
                'assignment': {
                    'assignment_id': assignment.assignment_id,
                    'title': assignment.title
                }
            }
            return JsonResponse({'message': 'Assignment Submitted Successfully', 'data': created_submission}, status=201)
        
        except Exception as e:
            return JsonResponse({"message": str(e)}, status=400)
    else:
        return JsonResponse({'message': "method should be POST"}, status=400)
    
    
    
    
