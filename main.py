from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author
def search_Book():
    book_choice = input("Write an author or genre: ").lower().title()
    for book in library_books:
        if book["genre"] == book_choice:
            print(book["title"])
        elif book["author"] == book_choice:
            print(book["title"])
        

def checkout():
    book_id = input("Enter book ID: ").capitalize()
    for book in library_books:
        if book_id == book["id"]:
            if book["available"] == True:
                book["available"] = False
                book["checkouts"] += 1
                today = datetime.today()
                book["due_date"] = today + timedelta(weeks=2)
                print("checkout completed sucessfully")
                print(f"Your due date is: {book["due_date"].strftime("%B %d, %Y")}")
            else:
                print("sorry, this book is not available")

def return_book():
    book_id = input("Enter book ID: ").capitalize()
    for book in library_books:
        if book_id == book["id"]:
            if book["available"] == True:
                print("This book has already been returned")
            else:
                book["available"] = True
                book["due_date"] = None
                print("Book returned sucessfully")
            break
    else:
        print("Sorry, no book found with that ID.")

       #try to add an else statement if book id doesnt match

while True:
    print("option 1")
    print("option 2")
    print("option 3")
    print("option 3")
    print("option 4")
    print("option 5")
    
    choice = int(input("Please choose 1 option: "))
    
    if choice == 1:
        search_Book()
    elif choice == 2:
        checkout()
    elif choice == 3:
        return_book()

# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books
#DONE

# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out
#DONE


# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date



# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out


# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

if __name__ == "__main__":
    # You can use this space to test your functions
    pass
