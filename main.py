def read_file():
    file = open(r"N:\Computing Science\S5 Computing\5.SQA Practice Assignments\Assignment Practice 25-26\training.csv", "r")
    raw_data = file.read().splitlines()
    file.close()

    raw_data.pop(0) #removes the header line from the CSV

    runners_f = []
    clubs_f = []
    run_dates_f = []
    is_completed_f = []
    paces_f = []

    for loop in range(len(raw_data)):
        line = raw_data[loop]
        line = line.split(",")

        runners_f.append(line[0])
        clubs_f.append(line[1])
        run_dates_f.append(line[2])
        is_completed_f.append(line[3])
        paces_f.append(line[4])

    return runners_f, clubs_f, run_dates_f, is_completed_f, paces_f

def club_finder(query_f, runners_f, clubs_f):
    runner_indexes = []
    club_count = 0
    for loop in range(len(runners_f)):
        if clubs_f[loop] == query_f:
            runner_indexes.append(loop)
            club_count = club_count + 1

    for loop in range(len(runner_indexes)):
        print(runners_f[loop])

    print("Total: " + str(club_count))

def achievement_status(run_dates_f, is_completed_f, paces_f): #takes in dates, whether theyre completed, and paces
    achievements_f = [] #initialises achievements array
    for instance in range(len(run_dates_f)): #loops for length of run_dates
        specific_date = 0 #initialises the specific_date variable
        if run_dates_f[instance][3:-6] == "0": #'xx/yy/zzzz' if the first y is a zero
            specific_date = int(run_dates_f[instance][3:-5][1]) #'xx/yy/zzzz' add only the second y and make it an int
        else: #'xx/yy/zzzz' if both ys are not zero
            specific_date = int(run_dates_f[instance][3:-5]) #'xx/yy/zzzz' add both the ys to the date variable and make it an int

        #refer to the table in the assignment documentation for this code:-
        if is_completed[instance] == "No" or run_dates_f[instance][6:] != "2025":
            achievements_f.append("N/A")
        elif specific_date >= 1 and specific_date <= 6 and int(paces_f[instance]) < 300:
            achievements_f.append("Elite")
        elif specific_date >= 1 and specific_date <= 6 and int(paces_f[instance]) >= 300:
            achievements_f.append("Pro")
        elif specific_date >= 7 and specific_date <= 12 and int(paces_f[instance]) < 330:
            achievements_f.append("Elite")
        elif specific_date >= 7 and specific_date <= 12 and int(paces_f[instance]) >= 330:
            achievements_f.append("Pro")

    classified_runners_f = []

    for loop in range(len(achievements_f)):
        if achievements_f[loop] != "N/A":
            classified_runners_f.append(loop)

    return classified_runners_f, achievements_f #return the achievements array once done

def write_to_file(classified_runners_f, runners_f, run_dates_f, achievements_f):
    file = open(r"N:\Computing Science\S5 Computing\5.SQA Practice Assignments\Assignment Practice 25-26\classified_runners.csv", "w")

    header = "Name,Date,Status"
    print(classified_runners_f)
    
    for loop in range(len(classified_runners)):
        specific_runner = classified_runners_f[loop]
        
        line = ""
        line = runners_f[specific_runner] + "," + run_dates_f[specific_runner] + "," + achievements_f[specific_runner] + "\n"
        file.write(line)

    file.close()
        
runners, clubs, run_dates, is_completed, paces = read_file()
query = str(input("Enter a club: "))
club_finder(query, runners, clubs)
classified_runners, achievements = achievement_status(run_dates, is_completed, paces)
write_to_file(classified_runners, runners, run_dates, achievements)
