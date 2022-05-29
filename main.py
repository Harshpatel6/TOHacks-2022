import os
from tokenize import String
import psycopg2



list1 = ["Frosti", "Toyota", "Camry", "2010", 2, 3, 2022, 400.00]


def exec_statement(conn, stmt):
    try:
        with conn.cursor() as cur:
            cur.execute(stmt)
            row = cur.fetchone()
            conn.commit()
            if row: print(row[0])
    except psycopg2.ProgrammingError:
        return


def main():

    # Connect to CockroachDB
    connection = psycopg2.connect(os.environ['DATABASE_URL'])

    statements = [
        # CREATE the messages table
        
        # INSERT a row into the messages table
        "INSERT INTO messages (message) VALUES ('Hello world!')",
        # SELECT a row from the messages table
        "SELECT message FROM messages"
    ]

    for statement in statements:
        exec_statement(connection, statement)

    # Close communication with the database
    connection.close()


if __name__ == "__main__":
    main()

def addPoggyWoggy(listerino):
    #dddd
    # Connect to CockroachDB
    connection = psycopg2.connect(os.environ['DATABASE_URL'])

    statements = ['''
    
    INSERT INTO coEmissionsTable(username, make, model, modelYear, day, month, year, co2)
    VALUES (%s,%s,%s,%d,%d,%d,%d,%f)
    
    
    ''']

        