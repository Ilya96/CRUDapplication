import mysql.connector

class CRUDService():

    def __init__(self):
        self.mydb = mysql.connector.connect(host="127.0.0.1",
                                       user="root",
                                       passwd="root",
                                       database="quotes"
                                       )

    def get_all(self):
        sql = "SELECT author, quote FROM quotes"
        mycursor = self.mydb.cursor()
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        #for x in myresult:
            #print("read the entry: {1}", x)
        return myresult

    def get(self, id):

        sql = "SELECT * FROM quotes WHERE id = %s"
        val = (id,)
        mycursor = self.mydb.cursor()
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        #for x in myresult:
            #print("read the entry: {1}", x)
        return myresult

    def post(self, author, quote):

        sql = "SELECT * FROM quotes WHERE author = %s and quote = %s"
        val = (author, quote)
        mycursor = self.mydb.cursor()
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        if not myresult:
            sql = "INSERT INTO quotes (author, quote) VALUES (%s, %s)"
            val = (author, quote)
            mycursor.execute(sql, val)
            self.mydb.commit()
            #print(mycursor.rowcount, "record affected")
            return 0
        else:
            return 1
    def put(self, author, quote, old_author, old_quote):

        sql = "SELECT * FROM quotes WHERE author = %s and quote = %s"
        val = (author, quote)
        mycursor = self.mydb.cursor()
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        if not myresult:
            sql = "UPDATE quotes SET author = %s, quote = %s WHERE author = %s and quote = %s"
            val = (author, quote, old_author, old_quote)
            mycursor = self.mydb.cursor()
            mycursor.execute(sql, val)
            self.mydb.commit()
            return 0
        else:
            return 1
        #print(mycursor.rowcount, "record affected")

    def delete(self, author, quote):

        sql = "DELETE FROM quotes WHERE author = %s and quote = %s"
        val = (author, quote)
        mycursor = self.mydb.cursor()
        mycursor.execute(sql, val)
        self.mydb.commit()
        #print(mycursor.rowcount, "record(s) deleted")