name = "shoxrux";
age = 26;
height = 1.77;
isStudent = True;

new = bool(age);
print(new - 0.4);
print(type(new));
#input()orqali malumot olsa bolar ekan va uni ozgaruvchiga olish kerak,shundan song foydalansa boladi"!
name = input("isming nima?: ");


age = input(f"yoshni kiriting: ");
age = int(age);
print(f"foydalanuvchi yoshi: {age}");
print(f"foydalanuvchi ismi: {name}");
if age > 18:
    print("alkogol sotib olsa boladi ");
else:
    print("alkogol sotib olish mumkin emas");