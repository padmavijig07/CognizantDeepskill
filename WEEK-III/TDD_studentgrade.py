class GradeCalculator:

    def calculate_grade(self, marks):
        if marks < 0 or marks > 100:
            raise ValueError("Invalid marks")

        if marks >= 90:
            return "A"
        elif marks >= 75:
            return "B"
        elif marks >= 60:
            return "C"
        elif marks >= 40:
            return "D"
        else:
            return "F"


gc = GradeCalculator()

print("95 ->", gc.calculate_grade(95))
print("82 ->", gc.calculate_grade(82))
print("68 ->", gc.calculate_grade(68))
print("45 ->", gc.calculate_grade(45))
print("25 ->", gc.calculate_grade(25))