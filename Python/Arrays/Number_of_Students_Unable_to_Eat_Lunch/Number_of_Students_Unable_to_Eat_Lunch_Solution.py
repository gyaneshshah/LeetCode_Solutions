class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0
        while students:
            student = students[0]
            sandwich = sandwiches[0]
            if student == sandwich:
                del sandwiches[0]
                del students[0]
                count = 0
            else:
                del students[0]
                count += 1
                students.append(student)
            if count == len(sandwiches):
                break
        return len(students)
