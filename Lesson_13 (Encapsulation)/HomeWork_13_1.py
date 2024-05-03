class Employees:
    def __init__(self, region, grade, base_salary):
        self._region = region
        self._grade = grade
        self._base_salary = base_salary

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, value):
        if not isinstance(value, str):
            raise ValueError("Region must be a string.")
        self._region = value

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Grade must be a number.")
        self._grade = value

    @property
    def base_salary(self):
        return self._base_salary

    @base_salary.setter

        def __str__(self):
        return f" if employee: region - {self.region}, grade - {self.grade}, then his base sallary is - {self.base_salary}"
            
    def base_salary(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Base salary must be a positive number.")
        self._base_salary = value

    def salary_calc(self):
        return self.base_salary * self.region * self.grade  # Assuming region is a numeric factor

class OutstaffEmployees(Employees):
    kurs_list = {"Ukraine": 1}

    def __init__(self, region, grade, base_salary):
        super().__init__(region, grade, base_salary)  # No country passed. To think on future how to implement country to this case

    def salary_calc(self):
        kurs = self.kurs_list.get(self.region)
        if kurs is None:
            raise ValueError(f"Unknown exchange rate for the region: {self.region}")
        return super().salary_calc() * kurs

    def __str__(self):
        return (f" if Employee is Outstaffer: region - {self.region}, "
                f"grade - {self.grade}, than his base sallary is - {self.base_salary}")


# Code to test the classes (assuming `Ukraine` is a valid region)
ukraine_employee = Employees("Ukraine", 2, 1000)
outstaff_employee = OutstaffEmployees("Ukraine", 3, 1500)

print(f"For Ukrainian employee:")
print(ukraine_employee)

print(f"For outstaffer employee:")
print(outstaff_employee)

