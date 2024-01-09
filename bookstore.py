"""
This program keeps track of all of our books
version : 2.0.0P
Date :15.05.2022
"""
import os


def main(filename):
    
    booksList = []
    infile = open(f"{filename}.txt", "a+")
    line = infile.readline()
    while line:
        booksList.append(line.rstrip("\n").split(",") )
        line = infile.readline()
    infile.close()

    choice = 0
    while choice !=4:
        print("*** Books Manager ***")
        print("1) Add a book")
        print("2) Lookup a book")
        print("3) Display books")
        print("4) Quit")
        choice = int(input("Option: "))
        
        if choice == 1:
            print("Addig a book...")
            nBook = input("Enter the name of the book >>> ")
            nAuthor = input("Enter the name of the author >>> ")
            while True:
                try:
                    rBefore = input("Have you read it before (yes/no) ? >>> ")

                    if rBefore.lower() not in ['yes', 'no']:
                        print('Wrong Answer!, Try Again \n')
                        continue
                    nPages = input("Enter the number of pages >>> ")

                    if not nPages.isnumeric(): 
                        print('not a valid number! \n')
                        nPages = input("Enter the number of pages >>> ")
                    break
                except:
                    print("Wrong type")
            booksList.append([nBook, nAuthor, rBefore, nPages])
        
        elif choice == 2:
            print("Looking up for a book...")
            keyword = input("Enter Book Name: ")
            for bookList in booksList:
                if keyword == bookList[0]:
                    print(bookList)
        
        elif choice == 3:
            print("Displaying all books...")
            for i in range(len(booksList)):
                print(booksList[i])
        
        elif choice == 4:
            print("Quitting Program")
    print("Program Terminated!")
    
    # Saving to external TXT file
    outfile = open(f"{filename}.txt", "w")
    for book in booksList:
        outfile.write(",".join(book) + "\n")
    outfile.close()
                    


if __name__ == "__main__":
    file = 'BookList'
    main(file)