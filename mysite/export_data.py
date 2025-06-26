import os
import django
import json
import sys

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

# Импортируем необходимые модели
from blog.models import Post, Comment
from django.contrib.auth.models import User

# Создаем структуру для JSON
posts_data = []
for post in Post.objects.all():
    post_data = {
        'model': 'blog.post',
        'pk': post.id,
        'fields': {
            'title': post.title,
            'slug': post.slug,
            'author_id': post.author_id,
            'body': post.body,
            'publish': str(post.publish),
            'created': str(post.created),
            'updated': str(post.updated),
            'status': post.status
        }
    }
    posts_data.append(post_data)

comments_data = []
for comment in Comment.objects.all():
    comment_data = {
        'model': 'blog.comment',
        'pk': comment.id,
        'fields': {
            'post_id': comment.post_id,
            'name': comment.name,
            'email': comment.email,
            'body': comment.body,
            'created': str(comment.created),
            'updated': str(comment.updated),
            'active': comment.active
        }
    }
    comments_data.append(comment_data)

users_data = []
for user in User.objects.all():
    user_data = {
        'model': 'auth.user',
        'pk': user.id,
        'fields': {
            'username': user.username,
            'password': user.password,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'is_active': user.is_active,
            'is_staff': user.is_staff,
            'is_superuser': user.is_superuser,
            'date_joined': str(user.date_joined),
            'last_login': str(user.last_login) if user.last_login else None
        }
    }
    users_data.append(user_data)

# Объединяем все данные
all_data = users_data + posts_data + comments_data

# Записываем в файл с явным указанием кодировки UTF-8
with open('mysite_data.json', 'w', encoding='utf-8') as f:
    json.dump(all_data, f, indent=2, ensure_ascii=False)

print(f"Данные экспортированы в mysite_data.json. Всего объектов: {len(all_data)}") 