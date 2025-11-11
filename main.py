from library_books import library_books
from datetime import datetime, timedelta

#Created a Book class that has all attributes
class Book:
    def __init__(self, id, title, author, genre, available, due_date, checkouts):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available
        self.due_date = due_date
        self.checkouts = checkouts


#List_book function, shows a list of all books
#Pre-condition: User enters 1 in the main menu
#Post-condition: Shows a list of each book's information
def list_books():
    for book in books:
        print("\n__________________________________________________\n")
        print(f"Book ID: {book.id}") 
        print(f"Title: {book.title}")
        print(f"Author: {book.author}")
        print(f"Genre: {book.genre}")
        print(f"Is this book available?: {book.available}")
        print(f"Due Date: {book.due_date}")
        print(f"This book has been checkout: {book.checkouts} times")
    print("\n__________________________________________________\n")

#Search_Book function, shows books that match what the user inputed
#Pre-condition: User enters 2 in the main menu
#Post-condition: Shows a list of each book's information, if the user's input matches its genre or author.
def search_Book():
    #Asks for either genre or author
    book_choice = input("Search up by author or genre: ").lower().title()
    
    #Set False in order for header to show only once, or if no book in found
    found = False 

    for book in books:
        #Checks if genre or author matches book_choice
        if book.genre == book_choice or book.author == book_choice:
            #Header
            if not found:  
                print("\n__________________________________")
                print("\n Books that Match Your Search")
                print("__________________________________\n")
                #Set to true in order to not activate line 63
                found = True

            #Book info
            print(f"Book ID: {book.id}") 
            print(f"Title: {book.title}")
            print(f"Author: {book.author}")
            print(f"Genre: {book.genre}")
            print(f"Is this book available?: {book.available}")
            print(f"Due Date: {book.due_date}")
            print(f"This book has been checked out: {book.checkouts} times")
            print("\n__________________________________________________\n")

    #if no books are found
    if not found:
        print("\nNo books found matching your search.\n")
    
        
#Checkout function, allows to checkout a book from library_books.py
#Pre-condition: User enters 3 in the main menu
#Post-condition: A book has been checkout and the "checkouts" in the dictionary increase by 1, 
#"avaliable" is set to False, and a due date is given for 2 weeks
def checkout():
    #asks for ID
    book_id = input("\nEnter book ID: ").capitalize()
    for book in books:
        if book_id == book.id:
            if book.available == True:
                #Sets the "avalable to False"
                book.available = False
                #Adds 1 to the checkouts
                book.checkouts += 1
                #Sets today's date
                today = datetime.today()
                #Adds 2 weeks to today for the due date
                book.due_date = today + timedelta(weeks=2)
                print("Checkout completed sucessfully!")
                #Prints the due date
                print(f"Your due date is: {book.due_date.strftime("%B %d, %Y")}")
            else:
                print("sorry, this book is not available")

#return_Book function, returns a book 
#Pre-condition: User enters 4 in the main menu
#Post-condition: Shows "availabe" to True and sets due date to none
def return_book():
    #Asks for ID
    book_id = input("\nEnter book ID: ").capitalize()
    for book in books:
        if book_id == book.id:
            
            #Checks if the book is already returned
            if book.available == True:
                print("This book has already been returned")
            
            #Sets available to True
            #Sets due date to none 
            else:
                book.available = True
                book.due_date = None
                print("Book returned sucessfully!")
            break
    else:
        print("Sorry, no book found with that ID.")

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out

def overdue_books():
    today = datetime.today().date()  
    print("\n__________________________________")
    print("\n           OVER DUE BOOKS")
    print("__________________________________\n") 
    for book in books:
        if not book.due_date or book.available:
            continue
        due_date = datetime.strptime(book.due_date, "%Y-%m-%d").date()
        
        if today > due_date:
            print(f"-{book.title}")

#most_checkout function, shows the top 3 most checkout books 
#Pre-condition: User enters 6 in the main menu
#Post-condition: Shows the title of the top 3 most checkout books
def most_checkout():
    #Sets all variables to 0 or None
    greatest = None
    greatest2 = None
    greatest3 = None
    i = 0  
    j = 0  
    a = 0

    #Its going to check for each book, if that book is greater than i
    #it will become the greatest, and then i is assigned to its checkout
    #For example, in the first iteration i = 0, and if a book has more checkout than 0, it will become 
    #the greatest (lets say that book had a checkout of 2), the on the 2nd iteration its going to check if 
    #the checkout is greater than 2, and if it is, the new book will become the new greatest. 
    for book in books:
        if book.checkouts > i:
            greatest = book
            i = book.checkouts

    #checks for 2nd greatest
    for book in books:
        if book != greatest and book.checkouts > j:
            greatest2 = book
            j = book.checkouts
    #checks for 3rd greatest
    for book in books:
        if book != greatest and book != greatest2 and book.checkouts > a:
            greatest3 = book
            a = book.checkouts
    print('\nThe top 3 most checkout books are:')
    print(f'1. {greatest.title}')
    print(f'2. {greatest2.title}')
    print(f'3. {greatest3.title}')


#it sets the dictionary into a book object
books = [Book(book["id"], book["title"], book["author"], book["genre"], book["available"], book["due_date"], book["checkouts"]) for book in library_books]

#Main menu
while True:
    print("\n__________________________________")
    print("\n            MAIN MENU")
    print("__________________________________\n") 
    print("1. List Books")
    print("2. Search Book")
    print("3. Checkout Book")
    print("4. Return Book")
    print("5. View Overdue Books")
    print("6. Top 3 Most Checkout Books")
    print("7. Exit")
    
    choice = input("Please choose 1 option: ")

    #Checks if choice is a number, if its not, it will ask the user to type it again
    try:
        choice = int(choice)
    except ValueError:
        print("Please enter a valid number from 1-6")
    
    #Menu list
    if choice ==1:
        list_books()
    elif choice == 2:
        search_Book()
    elif choice == 3:
        checkout()
    elif choice == 4:
        return_book()
    elif choice ==5:
        overdue_books()
    elif choice ==6:
        most_checkout()
    elif choice ==7:
        break


#Sources/Websites used to help me write the code
#1. https://stackoverflow.com/questions/14619494/how-to-understand-strptime-vs-strftime
#2. https://docs.python.org/3/library/datetime.html
#3. https://www.w3schools.com/python/python_class_init.asp
