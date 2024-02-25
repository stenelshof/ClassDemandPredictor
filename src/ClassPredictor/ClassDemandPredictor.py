__author__ = "Silas Ten Elshof"
__copyright__ = "Copyright 2024, Westmont College"
__credits__ = ["Silas Ten Elshof", "Mike Ryu"]
__license__ = "MIT"
__email__ = "Stenelshof@westmont.edu"

import pandas as pd

def main():
    excel_file_path = '/Users/silastenelshof/Desktop/CS195/SeniorProjectFakeData1.xlsx'
    df = pd.read_excel(excel_file_path)
    df = df.dropna(subset=df.columns[:3])

    students = df.values.tolist()
    #print(students)

    cred_per_class = 3
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
    print("Demand for spots in philosophy classes in two semesters:", sem_2_away_demand)
    #print(updated_students2)


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
    print("Demand for spots in philosophy classes in three semesters:", sem_3_away_demand)
    #print(updated_students3)


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
    print("Demand for spots in philosophy classes in four semesters:", sem_4_away_demand)
    #print(updated_students4)


if __name__ == "__main__":
    main()