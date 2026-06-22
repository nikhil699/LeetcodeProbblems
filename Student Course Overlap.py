# Time Complexity : 0(M + n * n * c)
from collections import defaultdict


class Solution(object):
    def studentCourseOverlap(self, student_course_pairs):

        pairStudentCourse = defaultdict(set)

        for student, course in student_course_pairs:
            pairStudentCourse[student].add(course)

        students = list(pairStudentCourse.keys())

        result = {}

        for i in range(len(students)):
            for j in range(i + 1, len(students)):

                student1 = students[i]
                student2 = students[j]
                # 0(c)
                commonCourses = list(
                    pairStudentCourse[student1] &
                    pairStudentCourse[student2]
                )

                result[(student1, student2)] = commonCourses

        return result




sol = Solution()

student_course_pairs = [
    ["58", "Software Design"],
    ["58", "Linear Algebra"],
    ["94", "Art History"],
    ["94", "Operating Systems"],
    ["17", "Software Design"],
    ["58", "Mechanics"],
    ["58", "Economics"],
    ["17", "Linear Algebra"],
    ["17", "Political Science"],
    ["94", "Economics"],
    ["25", "Economics"]
]
# Example
# 58 -> Software Design, Linear Algebra, Mechanics, Economics
# 94 -> Art History, Operating Systems, Economics
# 17 -> Software Design, Linear Algebra, Political Science
# 25 -> Economics



print(sol.studentCourseOverlap(student_course_pairs))