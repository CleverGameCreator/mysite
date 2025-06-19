import os
import django

# Настройка окружения Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

# Импорт необходимых модулей
from django.db import connection

# SQL для создания таблицы blog_comment
SQL = '''
CREATE TABLE IF NOT EXISTS blog_comment (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(80) NOT NULL,
    email VARCHAR(254) NOT NULL,
    body TEXT NOT NULL,
    created DATETIME NOT NULL,
    updated DATETIME NOT NULL,
    active BOOLEAN NOT NULL,
    post_id INTEGER NOT NULL REFERENCES blog_post(id)
);

CREATE INDEX IF NOT EXISTS blog_comment_created_idx ON blog_comment (created);

-- Добавляем запись в django_migrations, чтобы Django знал, что миграция выполнена
INSERT INTO django_migrations (app, name, applied) 
VALUES ('blog', '0003_create_comment_model', datetime('now'));
'''

def create_comment_table():
    with connection.cursor() as cursor:
        cursor.executescript(SQL)
    print("Таблица blog_comment успешно создана!")

if __name__ == '__main__':
    create_comment_table() 