"""
API ENDPOINTS:

Authentication:
- POST /api/auth/register/ - Register new user
- POST /api/auth/login/ - Login user
- POST /api/auth/logout/ - Logout user
- GET /api/auth/profile/ - Get user profile

Products:
- GET /api/products/ - List all products (all users)
- POST /api/products/ - Create product (admin only)
- GET /api/products/{id}/ - Get product detail (all users)
- PUT /api/products/{id}/ - Update product (admin only)
- DELETE /api/products/{id}/ - Delete product (admin only)
- GET /api/products/{id}/reviews/ - Get product reviews (all users)
- POST /api/products/{id}/add_review/ - Add review to product (regular users only)

Reviews:
- GET /api/reviews/ - List all reviews (all users)
- GET /api/reviews/?product={product_id} - Filter reviews by product
- POST /api/reviews/ - Create review (regular users only)
- GET /api/reviews/{id}/ - Get review detail (all users)
- PUT /api/reviews/{id}/ - Update review (review owner only)
- DELETE /api/reviews/{id}/ - Delete review (review owner only)

Usage Examples:

1. Register User:
POST /api/auth/register/
{
    "username": "testuser",
    "email": "test@example.com",
    "password": "testpass123",
    "password_confirm": "testpass123"
}

2. Login:
POST /api/auth/login/
{
    "username": "testuser",
    "password": "testpass123"
}

3. Create Product (Admin):
POST /api/products/
Headers: Authorization: Token <your-token>
{
    "name": "Test Product",
    "description": "This is a test product",
    "price": "29.99"
}

4. Add Review:
POST /api/products/1/add_review/
Headers: Authorization: Token <your-token>
{
    "rating": 5,
    "comment": "Great product!"
}

5. Get Products with Reviews:
GET /api/products/
"""

# ============================================================================

"""
SETUP INSTRUCTIONS:

1. Create virtual environment:
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

2. Install dependencies:
   pip install -r requirements.txt

3. Create Django project:
   django-admin startproject project .
   python manage.py startapp products

4. Run migrations:
   python manage.py makemigrations
   python manage.py migrate

5. Create superuser (admin):
   python manage.py createsuperuser

6. Run server:
   python manage.py runserver

7. Test API endpoints using tools like Postman or curl
"""