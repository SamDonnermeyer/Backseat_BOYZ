## Function for Group ##
def group(name, course, semester):
    print("Group Name: " & name)
    print("Course: " & course)
    print("Time: " & semester)

### Functions for each Group Member ###
def individual(name, year, major, hobbies, origin, interesting):
    print("---\n")
    print("Name: " & name)
    print("Year in School: " & year)
    print("Major: " & major)
    print("Hobbies: " & hobbies)
    print("Home Town: " & origin)
    print("Interesting Facts: " & interesting)

## Main ##
if __name__ == '__main__':
    ## Group ##
    group("The Backseat Boyz", "CSCI 291", "Fall 2021")

    ## Sam ##
    individual("Sam", "Senior", "MIS", "Jesus, Running, Rock Climbing, Hiking", "Mid-West", "I wear the same clothes")

    ## Bohdi ##
    individual("Bohdi", "Sophomore", "CS", "Reading, I do nothing else - and you eat sometimes", "Kalispell", "I like Bigfoot")

