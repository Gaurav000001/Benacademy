import json
from uuid import UUID
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Instructor
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_instructors(request):
    if request.method == "GET":
        
        instructors = Instructor.objects.all()
        data = [{
            "instructor_id": instructor.instructor_id, 
            "name": instructor.name, 
            'gender': instructor.gender,
            'date_of_birth': instructor.date_of_birth,
            'email': instructor.email, 
            'contact_number': instructor.contact_number
            } for instructor in instructors]
        
        return JsonResponse({'data': data}, safe=False, status=200)
        
    else:
        return JsonResponse({'message': "method should be GET"}, status=400)
    





@csrf_exempt
def register_instructor(request):
    if request.method == "POST":
        try:
            instructor_data = json.loads(request.body)
            
            # check if instructor with same email already exists
            email = instructor_data.get('email')
            instructor_with_email = Instructor.objects.filter(email = email)
            if instructor_with_email:
                return JsonResponse({'message': 'Instructor with email already exists, try another email or login'}, status=400)
            
            # check if instructor with same contact number already exists
            contact_number = instructor_data.get('contact_number')
            
            # check if contact_number is of 10 digit or not
            if len(contact_number) < 10 or len(contact_number) > 10:
                return JsonResponse({'message': 'contact number should be of 10 digists only'}, status=400)
            
            
            instructor_with_contact_number = Instructor.objects.filter(contact_number = contact_number)
            if instructor_with_contact_number:
                return JsonResponse({'message': 'Instructor with contact number already exists, try another contact number or login'}, status=400)
            

            instructor = Instructor(
                name = instructor_data.get('name'),
                gender = instructor_data.get('gender'),
                date_of_birth = instructor_data.get('date_of_birth'),
                email = instructor_data.get('email'),
                contact_number = instructor_data.get('contact_number'),
                password = instructor_data.get('password')
            )
            instructor.save()
            
            created_instructor = {
                "instructor_id" : instructor.instructor_id,
                "name" : instructor.name,
                "gender" : instructor.gender,
                "date_of_birth" : instructor.date_of_birth,
                "email" : instructor.email,
                "contact_number" : instructor.contact_number
            }
            
            return JsonResponse({"message": "Instructor created successfully.", 'data': created_instructor}, safe=False, status=201)
        except Exception as e:
            return JsonResponse({"message": str(e)}, status=400)
        
    else:
        return JsonResponse({'message': "method should be POST"}, status=400)




@csrf_exempt
def get_instructor(request, instructor_id):
    if request.method == "GET":
        try:
            instructor = get_object_or_404(Instructor, instructor_id=instructor_id)
            data = {
                "id": instructor.instructor_id,
                "name": instructor.name,
                "gender": instructor.gender,
                "date_of_birth": instructor.date_of_birth,
                "email": instructor.email,
                "contact_number": instructor.contact_number,
            }
            return JsonResponse({'data': data}, status=200)
        except Exception as e:
            return JsonResponse({'message': 'Instructor Not Found'}, status=404)

    else:
        return JsonResponse({'message': "method should be GET"}, status=400)







@csrf_exempt
def update_instructor(request, instructor_id):
    if request.method == "PUT":
        try:
            # changing type of instructor_id from str to UUID for comparisons
            instructor_id = UUID(instructor_id)
            instructor = get_object_or_404(Instructor, pk=instructor_id)
            instructor_data = json.loads(request.body)
            
            
            
            # check if instructor with same email already exists
            email = instructor_data.get('email')
            instructor_with_email = Instructor.objects.filter(email = email)
            if instructor_with_email:
                if instructor_with_email[0].instructor_id is not instructor_id:
                    return JsonResponse({'message': 'Instructor with email already exists, try another email'}, status=400)
            
            # check if instructor with same contact number already exists
            contact_number = instructor_data.get('contact_number')
            
            # check if contact_number is of 10 digit or not
            if len(contact_number) < 10 or len(contact_number) > 10:
                return JsonResponse({'message': 'contact number should be of 10 digists only'}, status=400)
            
            
            instructor_with_contact_number = Instructor.objects.filter(contact_number = contact_number)
            if instructor_with_contact_number:
                if instructor_with_contact_number[0].instructor_id is not instructor_id:
                    return JsonResponse({'message': 'Instructor with contact number already exists, try another contact number'}, status=400)
            
            
            # extract data from request body to update instructor
            instructor_data_extracted = {
                "name" : instructor_data.get('name'),
                "gender" : instructor_data.get('gender'),
                "date_of_birth" : instructor_data.get('date_of_birth'),
                "email" : instructor_data.get('email'),
                "contact_number" : instructor_data.get('contact_number')
            }
            
            # setting up the values to update instructor
            for key, value in instructor_data_extracted.items():
                setattr(instructor, key, value)

            instructor.save()
            
            updated_instructor = {
                "instructor_id" : instructor.instructor_id,
                "name" : instructor.name,
                "gender" : instructor.gender,
                "date_of_birth" : instructor.date_of_birth,
                "email" : instructor.email,
                "contact_number" : instructor.contact_number
            }
            
            return JsonResponse({'message': 'Instructor updated successfully', 'data': updated_instructor}, status=200)
        except Exception as e:
            return JsonResponse({'message': 'Instructor Not Found'}, status=404)

    else:
        return JsonResponse({'message': "method should be PUT"}, status=400)





@csrf_exempt
def delete_instructor(request, instructor_id):
    if request.method == "DELETE":
        try:
            instructor = get_object_or_404(Instructor, instructor_id=instructor_id)
            
            deleted_instructor = {
                "instructor_id" : instructor.instructor_id,
                "name" : instructor.name,
                "gender" : instructor.gender,
                "date_of_birth" : instructor.date_of_birth,
                "email" : instructor.email,
                "contact_number" : instructor.contact_number
            }
            instructor.delete()
            
            return JsonResponse({'message': 'Instructor deleted successfully', 'data': deleted_instructor}, status=200)
        except Exception as e:
            return JsonResponse({'message': 'Instructor Not Found'}, status=404)

    else:
        return JsonResponse({'message': "method should be DELETE"}, status=400)
