from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from.models import Postal,PostalAddress
from.serializers import postalserializer,postaladdressserializer
import requests

# Create your views here.


# postalapp/views.py




def home(request):
    return render(request, 'postalapp/home.html')
def get(request):
    return render(request, 'postalapp/post.html')

def post(request):
    print('Post view called')
    if request.method == 'POST':
        postal_code = request.POST.get('postal_code', '')
        result = get_postal_info(postal_code)
        return JsonResponse(result)
    else:
        # Handle GET requests (if needed)
        return render(request, 'postalapp/post.html')

def get_postal_info(postal_code):
    api_endpoint = f'https://api.postalpincode.in/pincode/{postal_code}'

    try:
        response = requests.get(api_endpoint)
        data = response.json()

        if data and data[0]['Status'] == 'Success':
            post_office_data = data[0]['PostOffice'][0]

            # Populate fields from the API response
            postal_code_instance = Postal(
                Pincode=postal_code,
                Area=post_office_data.get('Name', ''),
                Branch_type=post_office_data.get('BranchType', ''),
                Circle=post_office_data.get('Circle', ''),
                District=post_office_data.get('District', ''),
                Division=post_office_data.get('Division', ''),
                Region=post_office_data.get('Region', ''),
                State=post_office_data.get('State', ''),
                Country=post_office_data.get('Country', '')
            )

            # Save the instance to the database
            postal_code_instance.save()

            # Serialize the instance for the response
            serializer = postalserializer(postal_code_instance)

            return {'success': True, 'data': serializer.data}

        else:
            return {'success': False, 'error': 'Error in API response'}

    except requests.exceptions.RequestException as e:
        return {'success': False, 'error': f'Error connecting to API: {str(e)}'}

    except Exception as e:
        return {'success': False, 'error': f'An error occurred: {str(e)}'}
    

    
    



def get1(request):
    return render(request, 'postalapp/post-add.html')

@api_view(['POST'])
def post1(request):
    print('Post view called')

    if request.method == 'POST':
        post_office_branch = request.POST.get('post_office_branch', '')
        result = get_postal_info1(post_office_branch)

        if result['success']:
            serializer = postaladdressserializer(data=result['data'], many=True)
            if serializer.is_valid():
                return Response({'success': True, 'data': serializer.data})
            else:
                return Response({'success': False, 'error': 'Serializer validation failed'})
        else:
             return Response({'success': False, 'error': result['error']})
    else:
        return render(request, 'postalapp/post.html')
    

def get_postal_info1(post_office_branch):
    api_endpoint = f'https://api.postalpincode.in/postoffice/{post_office_branch}'

    try:
        response = requests.get(api_endpoint)
        data = response.json()

        if data and isinstance(data, list) and 'Status' in data[0] and data[0]['Status'] == 'Success':
            post_office_entries = data[0]['PostOffice']
            if post_office_entries:
                result_data = []  # Initialize the list outside the loop

                for post_office_data in post_office_entries:
                    name = post_office_data.get('Name', '')
                    branch_type = post_office_data.get('BranchType', '')
                    circle = post_office_data.get('Circle', '')
                    district = post_office_data.get('District', '')
                    division = post_office_data.get('Division', '')
                    region = post_office_data.get('Region', '')
                    state = post_office_data.get('State', '')
                    country = post_office_data.get('Country', '')
                    pincode = post_office_data.get('Pincode', '')

                    # Create instance of PostalAddress inside the loop
                    postal_info_instance = PostalAddress(
                        Place=name,
                        Branch_type=branch_type,
                        Circle=circle,
                        District=district,
                        Division=division,
                        Region=region,
                        State=state,
                        Country=country,
                        Pincode=pincode
                    )
                    result_data.append(postal_info_instance.__dict__)

                    print("Post Office Entry Data:", postal_info_instance.__dict__)

                print("Result Data:", result_data) 
                return {'success': True, 'data': result_data}
            else:
                return {'success': False, 'error': 'No postal entries found in API response'}
        else:
            return {'success': False, 'error': 'Invalid or unexpected API response'}

    except requests.exceptions.RequestException as e:
        return {'success': False, 'error': f'Error connecting to API: {str(e)}'}

    except Exception as e:
        return {'success': False, 'error': f'An error occurred: {str(e)}'}
