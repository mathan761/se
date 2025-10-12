import os
from datetime import datetime

folder = '.'  # Текущая папка
image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')

# Получаем список изображений, исключая уже существующие picX
files = [f for f in os.listdir(folder)
         if f.lower().endswith(image_extensions) and not f.lower().startswith('pic')]

if not files:
    print("Не найдено изображений для переименования.")
else:
    print(f"Найдено {len(files)} изображений:")

# Получаем дату модификации каждого файла
files_with_mtime = []
for f in files:
    full_path = os.path.join(folder, f)
    mtime = os.path.getmtime(full_path)  # дата последней модификации
    files_with_mtime.append((f, mtime))
    print(f" - {f} (дата модификации: {datetime.fromtimestamp(mtime)})")

# Сортируем по дате (от старого к новому)
files_sorted = sorted(files_with_mtime, key=lambda x: x[1])

# Переименовываем сначала во временные уникальные имена
temp_names = []
for i, (f, _) in enumerate(files_sorted, start=1):
    extension = os.path.splitext(f)[1]
    temp_name = f"temp_unique_{i}{extension}"
    temp_path = os.path.join(folder, temp_name)
    os.rename(os.path.join(folder, f), temp_path)
    temp_names.append(temp_path)
    print(f"{f} -> {temp_name} (временно)")

# Потом присваиваем финальные имена pic1, pic2…
for i, temp_path in enumerate(temp_names, start=1):
    extension = os.path.splitext(temp_path)[1]
    final_name = f"pic{i}{extension}"
    final_path = os.path.join(folder, final_name)
    os.rename(temp_path, final_path)
    print(f"{os.path.basename(temp_path)} -> {final_name} (финально)")

print("Переименование завершено!")
