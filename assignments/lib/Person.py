class Profession:
    Title = ''
    Salary = 0
    Years = 0

    def __init__(this, title, salary, years):
        this.Title = title
        this.Salary = salary
        this.Years = years

class Person:
    FirstName = ''
    LastName = ''
    Age = 0
    Height = 0
    Weight = 0
    Race = ''
    Job = (Profession)

    def __init__(this, firstName, lastName, age, height, weight, race, profession):
        this.FirstName = firstName
        this.LastName = lastName
        this.Age = age
        this.Height = height
        this.Weight = weight
        this.Race = race
        this.Job = profession

    def GetName(this):
        return this.LastName + ', ' + this.FirstName


workers = [
    Person('Mark', 'Jones', 37, 68, 185, 'White', Profession('Sr. Engineer', 146000, 8)),
    Person('Mike', 'Roberts', 23, 66, 205, 'Black', Profession('Jr. Developer', 105000, 2)),
    Person('John', 'Parsons', 42, 62, 162, 'Asian', Profession('Sales Representative 1', 66000, 2)),
    Person('Nick', 'Nolte', 52, 71, 177, 'Hispanic', Profession('Sales Representative 3', 112000, 4)),
    Person('Jim', 'Evans', 46, 66, 192, 'White', Profession('Sr. Developer', 186000, 8)),
]

for worker in workers:
    prof = worker.Job
    print(worker.GetName(), 'is a', worker.Age, 'year old', prof.Title, 'with', prof.Years,
    'years of experience, who makes ', prof.Salary, 'a year.')



