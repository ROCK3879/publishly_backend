# Requirements.txt

asgiref==3.8.1
dj-database-url==2.2.0
Django==5.0.7
django-cors-headers==4.4.0
django-heroku==0.3.1
djangorestframework==3.15.2
djangorestframework-simplejwt==5.2.2

gunicorn==22.0.0
mysqlclient==2.2.4
packaging==24.1
psycopg2==2.9.9
py==1.11.0
sqlparse==0.5.1
typing_extensions==4.12.2
tzdata==2024.1
whitenoise==6.7.0
python-decouple==3.8
django-environ==0.9.0

# Users Endpoints
List Users: GET /api/users/
Create User: POST /api/users/create/
Retrieve User: GET /api/user/<int:pk>/
Update User: PUT /api/user/update/<int:pk>/
Delete User: DELETE /api/user/<int:pk>/
User Login: POST /api/user/login/


# Profile Endpoints
List Profiles: GET /api/profiles/
Create Profile: POST /api/profile/create/<int:pk>/
Retrieve Profile: GET /api/profile/<int:pk>/
Update Profile: PUT /api/profile/update/<int:pk>/
Delete Profile: DELETE /api/profile/<int:pk>/

# Followers Endpoints
List Followers: GET /api/followers/
Create Follower: POST /api/user/follow/<int:pk>/
Delete Follower: DELETE /api/user/unfollow/<int:pk>/

# Posts Endpoints
List Posts: GET /api/posts/

Create Post: POST /api/post/create/<int:user_id>/

Retrieve Post: GET /api/post/<int:pk>/

Update Post: PUT /api/post/update/<int:pk>/

Delete Post: DELETE /api/post/<int:pk>/
Like Post: POST /api/posts/like/<int:post_id>/
Dislike Post:Post /api/posts/dislike/<int:post_id>/

# Comment Endpoints
List Comment: GET /api/comments/
Create Comment: POST /api/comment/create/<int:post_id>/
Retrieve Comment: GET /api/comment/<int:pk>/
Update Comment: PUT /api/comment/update/<int:pk>/
Delete Comment: DELETE /api/comment/<int:pk>/'

# Category Endpoints
List Category: GET /api/categories/
Create Category: POST /api/category/create/
Retrieve Category: GET /api/category/<int:pk>/
Update Category: PUT /api/category/update/<int:pk>/
Delete Category: DELETE /api/category/<int:pk>/

# Manual Testing using Postman
## List all the posts
![List all the posts](/images/4.0.readme_manual_testing_using_postman)

## Create a Post
![Create a Post](src/images/)

## Delete a Post
![Delete a Post](src/images/)

## Like a Post
![Like a Post](src/images/)

## List Categories
![List Categories](src/images/)

## Add a Category
![Add a Category](src/images/)

## Delete a Category
![Delete a Category](src/images/)

















