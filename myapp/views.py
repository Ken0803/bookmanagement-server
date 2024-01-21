from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
import json
from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')

        if User.objects.filter(email=email).exists():
            return JsonResponse({'message': 'Email already in use'}, status=400)

        user = User.objects.create_user(username=email, email=email, password=password)
        token = get_tokens_for_user(user)
        return JsonResponse({'message': 'User created successfully', 'token': token}, status=201)

    return JsonResponse({'message': 'Invalid request'}, status=400)

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)

            token = get_tokens_for_user(user)
            return JsonResponse({'message': 'Login successful', 'token': token}, status=200)
        else:
            return JsonResponse({'message': 'Invalid credentials'}, status=400)

    return JsonResponse({'message': 'Invalid request'}, status=400)


from .models import Book
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def book_list(request):
    books = Book.objects.all().values('id', 'name', 'description', 'image')
    return JsonResponse(list(books), safe=False)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def book_detail(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        book_data = {
            'id': book.id,
            'name': book.name,
            'description': book.description,
            'image': book.image.url if book.image else None  # Assuming 'image' is a FileField or ImageField
        }
        return JsonResponse(book_data)
    except Book.DoesNotExist:
        return JsonResponse({'error': 'Book not found'}, status=404)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def create_book(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            book = Book.objects.create(
                name=data['name'],
                description=data['description'],
                image=data['image']  # Ensure your model and form handle image uploads correctly
            )
            return JsonResponse({'message': 'Book created successfully', 'id': book.id})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return HttpResponse("Method not allowed", status=405)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def update_book(request, book_id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            book = Book.objects.get(id=book_id)
            book.name = data.get('name', book.name)
            book.description = data.get('description', book.description)
            book.image = data.get('image', book.image)
            book.save()
            return JsonResponse({'message': 'Book updated successfully'})
        except Book.DoesNotExist:
            return JsonResponse({'error': 'Book not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return HttpResponse("Method not allowed", status=405)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def delete_book(request, book_id):
    if request.method == 'DELETE':
        try:
            book = Book.objects.get(id=book_id)
            book.delete()
            return JsonResponse({'message': 'Book deleted successfully'})
        except Book.DoesNotExist:
            return JsonResponse({'error': 'Book not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return HttpResponse("Method not allowed", status=405)

