__author__ = "Silas Ten Elshof"
__copyright__ = "Copyright 2024, Westmont College"
__credits__ = ["Silas Ten Elshof", "Mike Ryu"]
__license__ = "MIT"
__email__ = "Stenelshof@westmont.edu"

def main():
    # the first element is id, second element is number of semesters left, third is number of credits needed before grad
    students = [[1, 5, 15], [2, 2, 6], [3, 4, 12], [4, 2, 12]]
    next_sem_demand = 0

    for student in students:
        demand_per_sem = student[2]/student[1]
        next_sem_demand += demand_per_sem

    print(next_sem_demand)

if __name__ == "__main__":
    main()