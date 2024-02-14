__author__ = "Silas Ten Elshof"
__copyright__ = "Copyright 2024, Westmont College"
__credits__ = ["Silas Ten Elshof", "Mike Ryu"]
__license__ = "MIT"
__email__ = "Stenelshof@westmont.edu"

def main():
    cred_per_class = 3
    # the first element is id, second element is number of semesters left, third is number of credits needed before grad
    students = [[1, 5, 15], [2, 2, 6], [3, 4, 12], [4, 2, 12], [5, 1, 3]]
    sem_2_away_demand = 0
    sem_3_away_demand = 0
    sem_4_away_demand = 0
    updated_students2 = []
    updated_students3 = []
    updated_students4 = []

    for student in students:
        cred_demand_per_sem = student[2]/student[1]
        student[1] -= 1
        student[2] -= cred_demand_per_sem
        if student[1] > 0:
            updated_students2.append(student)

    for updated_student in updated_students2:
        cred_demand_per_sem = updated_student[2] / updated_student[1]
        class_demand_per_sem = cred_demand_per_sem/cred_per_class
        sem_2_away_demand += class_demand_per_sem
    print(sem_2_away_demand)
    print(updated_students2)


    for student in updated_students2:
        cred_demand_per_sem = student[2]/student[1]
        student[1] -= 1
        student[2] -= cred_demand_per_sem
        if student[1] > 0:
            updated_students3.append(student)

    for updated_student in updated_students3:
        cred_demand_per_sem = updated_student[2] / updated_student[1]
        class_demand_per_sem = cred_demand_per_sem/cred_per_class
        sem_3_away_demand += class_demand_per_sem
    print(sem_3_away_demand)
    print(updated_students3)


    for student in updated_students3:
        cred_demand_per_sem = student[2]/student[1]
        student[1] -= 1
        student[2] -= cred_demand_per_sem
        if student[1] > 0:
            updated_students4.append(student)

    for updated_student in updated_students4:
        cred_demand_per_sem = updated_student[2] / updated_student[1]
        class_demand_per_sem = cred_demand_per_sem/cred_per_class
        sem_4_away_demand += class_demand_per_sem
    print(sem_4_away_demand)
    print(updated_students4)


if __name__ == "__main__":
    main()