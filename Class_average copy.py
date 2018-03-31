# Class Average by Gracie Bracken

def main() :
    # print instructions
    print("This program inputs test scores")
    print("and calculates the average.")
    print("")
    
    # get the # of students
    number_students=input("please enter the number of students -> ")
    number_students=int(number_students)
    
    # get the scores
    score_list=[]
    for i in range(number_students) :
        score=input("score -> ")
        score=int(score)
        score_list.append(score)
        
    # calc the average
    total=0
    for i in range(len(score_list)):
        total= total + score_list[i]
    average_score=total/len(score_list)
    
    # print results
    print("I have thought long and hard . . . .")
    print("The average score is",average_score,"!")
    

main()
