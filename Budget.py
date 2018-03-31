def main() :
    print("Hello, can I help you save?")
    print("It is quite easy. Just follow")
    print("the steps given.")

    fixed=input("Please enter number of fixed expenses -> ")
    fixed=int(fixed)

    expense=input("Now type what fixed expenses you have.")
    score_list=[]
    for i in range(fixed) :
        expense=input("Now type what fixed expenses you have.")
        expense=input("expense -> ")
        expense=str(expense)
        score_list.append(expense)
        
main()
