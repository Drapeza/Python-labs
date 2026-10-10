
people_salary={}
dept_salary={}
with open("staff.txt", "r", encoding="utf-8") as f:
    for line in f:
        line=line.strip()
        if not line:
            continue

        parts=line.strip().split(";")
        surname, dept, job, salary = parts
        salary=float(salary)


        people_salary[surname]=[dept, job, salary]

        dept_salary.setdefault(dept,[]).append(surname)
    f.seek(0)
    text1 = f.read()

#птыаемся посчитать среднее
with open("rise.txt", "w", encoding="utf-8") as f:
    for dept in dept_salary:
        amount=0
        total=0
        for surname in people_salary:
            if surname in dept_salary[dept]:
                amount+=1
                total+=people_salary[surname][2]
        average=total/amount

        for surname in people_salary:
            if surname in dept_salary[dept]:
                if people_salary[surname][2]<average:
                    people_salary[surname][2]*=1.1
                else: people_salary[surname][2]*=1.05

                f.write(f"{surname};{people_salary[surname][0]};{people_salary[surname][1]};{people_salary[surname][2]}\n")

with open("rise.txt", "r", encoding="utf-8") as f:
    text2 = f.read()

print("Старые оклады:")
print(text1)
print("Новые оклады:")
print(text2)