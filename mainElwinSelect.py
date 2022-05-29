import os
from tokenize import String
import psycopg2
import datetime
# from datetime import datetime, timedelta


list1 = ['elwin2', 'Honda', 'Civic', 2015, 2, 3, 2022, 450.00]
list_as_tuple = tuple(list1)


def exec_statement(conn, stmt):
    try:
        with conn.cursor() as cur:
            cur.execute(stmt, list1)
            row = cur.fetchone()
            conn.commit()
            # if row: print(row)
    except psycopg2.ProgrammingError:
        return


# def main():

#     # Connect to CockroachDB
#     connection = psycopg2.connect(os.environ['DATABASE_URL'])

#     statements = [

#         """INSERT INTO coEmissionsTable (username, make, model, modelYear, day, month, year, co2)
#             VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
#         """,
       
#         """SELECT * FROM coEmissionsTable"""
#     ]

    

#     for statement in statements:
#         exec_statement(connection, statement)

    
#     # Close communication with the database
#     connection.close()





def retrieveCO2():
    #Make a function for select, you want the values for either a specific month, or specific weeks and make it into a dataframe so they can graph it

    
    connection = psycopg2.connect(os.environ['DATABASE_URL'])


#YEAR MONTH DAY

    todayDate = datetime.datetime.now()
    DaysPrior = datetime.timedelta(days=7)
    sevenDaysPrior = todayDate - DaysPrior

    # modToday = str(todayDate.strftime("%Y-%m-%d"))
    # modSeven = str(sevenDaysPrior.strftime("%Y-%m-%d"))

    modToday = todayDate.strftime("%Y-%m-%d 00:00:00")
    modSeven = sevenDaysPrior.strftime("%Y-%m-%d 23:59:00")

    # d = datetime.today() - timedelta(days =7)

    #tab2 = pd.read_sql_query("SELECT * FROM bbb.ccc WHERE DT between ? and ?", con, params=['2015-09-18', '2015-10-02']) 
    #where game_date between '2012-03-11 00:00:00' and '2012-05-11 23:59:00' 

    with connection.cursor() as cur:

        cur.execute("SELECT * FROM coEmissionsTable;")
        # cur.execute("SELECT * FROM coEmissionsTable WHERE date BETWEEN " + modToday + " AND " + modSeven + ";")
        # cur.execute("SELECT * FROM coEmissionsTable WHERE date BETWEEN " + modSeven + " AND " + modToday + ";")
        # cur.execute("SELECT * FROM coEmissionsTable WHERE date BETWEEN '2012-03-11 00:00:00' and '2023-05-11 23:59:00'")

        rows = cur.fetchall()
        for row in rows:
            print([str(cell) for cell in row])


if __name__ == "__main__":
    main()
