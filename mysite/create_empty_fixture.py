import json

# Создаем пустой список (пустая фикстура)
data = []

# Записываем в файл с кодировкой UTF-8
with open('mysite_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Создан пустой файл mysite_data.json в кодировке UTF-8") 