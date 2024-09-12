from tkinter import *
import pyodbc

# back end

def showBtn():
    db_file = r'C:\Users\2018000485\Downloads\Movie_ListTbl.accdb'

    # Establish a connection to the database
    conn_str = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + db_file
    conn = pyodbc.connect(conn_str)

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    sqlComm = 'SELECT * FROM Movie_list;' # sql command

    try:
        # Execute a SELECT query
        cursor.execute(sqlComm)  # Enter correct Table Name

        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Print column headers
        # columns = [column[0] for column in cursor.description]
        # print('\t'.join(columns))

        # print format the heading title
        print(f'{"Movie Name":<70}{"Release Date":<20}{"Genres":<20}{"Maturity Ratings":<20}{"Number of Stars":<20}{"Views":<20}')

        # Print each row
        for row in rows:
            # print('\t'.join(str(item) for item in row))

            relDate = row.Release_Date.strftime("%d-%m-%Y")

            
            Movie_list = f'{row.Movie_Name:<70}{relDate:<20}{row.Genres:<20}{row.Maturity_Ratings:<20}{row.Number_of_Stars:<20}{row.Views:<20}'
            print(Movie_list)
            
    except pyodbc.Error as e:
        print(f"Error accessing database: {e}")

    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()
        
def submitBtn():
    # get data from text box
    Movie_Name = titleTxtbx.get()
    Release_Date = RdateTxtbx.get()
    Genres = genresTxtbx.get()
    Maturity_Ratings = MratingsTxtbx.get()
    Number_of_Stars = reviewTxtbx.get()
    Views = viewTxtbx.get()
    
    db_file = r'C:\Users\2018000485\Downloads\Movie_ListTbl.accdb'

    # Establish a connection to the database
    conn_str = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + db_file
    conn = pyodbc.connect(conn_str)

    # Create a cursor object to interact with the database
    cursor = conn.cursor()
    
   

    cursor.execute("INSERT INTO Movie_list (Movie_Name, Release_Date, Genres, Maturity_Ratings, Number_of_Stars, Views) VALUES (?, ?, ?, ?, ?, ?);",(Movie_Name, Release_Date, Genres, Maturity_Ratings, Number_of_Stars, Views))
    
    
    conn.commit()
    
    cursor.close()
    conn.close()
        
# def submitBtn():
#     db_file = r'C:\Users\2018000485\Downloads\Movie_ListTbl.accdb'

#     Establish a connection to the database
#     conn_str = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + db_file
#     conn = pyodbc.connect(conn_str)

#     Create a cursor object to interact with the database
#     cursor = conn.cursor()
    
#     sqlComm = f'INSERT INTO People VALUES (26, "Kerehi", "Matete", "kerehi.m3@gmail.com";'

#     cursor.execute(sqlComm)
    
#     conn.commit()
    
#     cursor.close()
#     conn.close()

# front end

widget = Tk() # creates the widget object from tkinter

widget.title("Assessment 2")
widget.geometry("400x200")

# creating labels and textboxes

titleLabel = Label(widget, text="Movie Name")
RdateLabel = Label(widget, text="Release Date")
genresLabel = Label(widget, text="Genre")
MratingsLabel = Label(widget, text="Maturity Rating")
reviewLabel = Label(widget, text="Number of Stars")
viewLabel = Label(widget, text="Views")

titleTxtbx = Entry(widget, width=10)
RdateTxtbx = Entry(widget, width=10)
genresTxtbx = Entry(widget, width=10)
MratingsTxtbx = Entry(widget, width=10)
reviewTxtbx = Entry(widget, width=10)
viewTxtbx = Entry(widget, width=10)

# first column elements
titleLabel.grid(row=1, column=1)
RdateLabel.grid(row=1, column=3)

# 2nd column elements
titleTxtbx.grid(row=1, column=2, padx=10, pady=5)
titleTxtbx.insert(0, "Movie Name")
RdateTxtbx.grid(row=1, column=4, padx=10, pady=5)
RdateTxtbx.insert(0, "Release Date")

# 3rd column elements
genresLabel.grid(row=2, column=1)
MratingsLabel.grid(row=2, column=3, padx=10, pady=5)

# 4th column elements
genresTxtbx.grid(row=2, column=2, padx=10, pady=5)
genresTxtbx.insert(0, "Genres")
MratingsTxtbx.grid(row=2, column=4, padx=10, pady=5)
MratingsTxtbx.insert(0, "Maturity Ratings")

# 5th column elements
reviewLabel.grid(row=4, column=1, padx=10, pady=5)
viewLabel.grid(row=4, column=3, padx=10, pady=5)

# 6th column elements
reviewTxtbx.grid(row=4, column=2, padx=10, pady=5)
reviewTxtbx.insert(0, "Number of Stars")
viewTxtbx.grid(row=4, column=4, padx=10, pady=5)
viewTxtbx.insert(0, "Views")

# create buttons

submitBtn = Button(widget, text="Submit", command=submitBtn).grid(row=7, column=2, padx = 10, pady=5)
showBtn = Button(widget, text="Show all", command=showBtn).grid(row=7, column=3, padx = 10, pady=5)
quitBtn = Button(widget, text="Quit", command=widget.destroy).grid(row=7, column=4, padx = 10, pady=5)

widget.mainloop() # runs mainloop to show widget


