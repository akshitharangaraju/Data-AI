from employee.employee import employee_list

search_name = input("Enter employee name: ")
found = False

for emp in employee_list:
    if emp.name.lower() == search_name.lower():
        print("\nEmployee Found ✅")
        emp.display()
        found = True
        break

if not found:
    print("\nEmployee not found ❌")
