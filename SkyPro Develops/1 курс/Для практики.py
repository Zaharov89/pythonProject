books = {
   "Саймон Сингх": "Книга шифров",
   "Брюс Шнайер": "Практическая криптография",
   "Нил Стивенсон": "Криптономикон",
   "Дэвид Кан": "Взломщики кодов",
   "Альбрехт Бойтельспахер": "Криптология",
}

print("-")
print("Книги:")
print(*books.values(), sep='\n')

print("-")
print("Авторы:")
print(*books.keys(), sep='\n')

print("-")
print("Библиотека:")
for author, book in books.items():
    print(f"{author} - {book}")