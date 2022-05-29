import os
from tokenize import String
import psycopg2



list1 = ['Harsh', 'Honda', 'Civic', 2015, 2, 3, 2022, 450.00]
list_as_tuple = tuple(list1)


def exec_statement(conn, stmt):
    try:
        with conn.cursor() as cur:
            cur.execute(stmt, list1)
            row = cur.fetchone()
            conn.commit()
            if row: print(row[0])
    except psycopg2.ProgrammingError:
        return


def main():

    # Connect to CockroachDB
    connection = psycopg2.connect(os.environ['DATABASE_URL'])

    statements = [

        """INSERT INTO coEmissionsTable (username, make, model, modelYear, day, month, year, co2)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """,
       
        """SELECT model FROM coEmissionsTable
        WHERE username = 'Harsh'"""
    ]

    

    for statement in statements:
        exec_statement(connection, statement)

    # Close communication with the database
    connection.close()


if __name__ == "__main__":
    main()




        