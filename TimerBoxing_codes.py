import sqlite3
con = sqlite3.connect("idealdatabase.db")
mycursor = con.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS tblTimer (TID TEXT, TTitle TEXT, TRoundCount TEXT, TFightMinute TEXT, TFightSecond TEXT, TRestMinute TEXT, TRestSecond TEXT, TWait TEXT) ")
mycursor.execute("SELECT * FROM tblTimer")
# mycursor.execute("Delete From tblTimer")
if not mycursor.fetchone():
    mycursor.execute("INSERT INTO tblTimer (TID, TTitle, TRoundCount, TFightMinute, TFightSecond, TRestMinute, TRestSecond, TWait) VALUES (1, 0, 0, 0, 0, 0, 0, 0)")
    mycursor.execute("INSERT INTO tblTimer (TID, TTitle, TRoundCount, TFightMinute, TFightSecond, TRestMinute, TRestSecond, TWait) VALUES (2, 0, 0, 0, 0, 0, 0, 0)")
    mycursor.execute("INSERT INTO tblTimer (TID, TTitle, TRoundCount, TFightMinute, TFightSecond, TRestMinute, TRestSecond, TWait) VALUES (3, 0, 0, 0, 0, 0, 0, 0)")
    mycursor.execute("INSERT INTO tblTimer (TID, TTitle, TRoundCount, TFightMinute, TFightSecond, TRestMinute, TRestSecond, TWait) VALUES (4, 0, 0, 0, 0, 0, 0, 0)")
    mycursor.execute("INSERT INTO tblTimer (TID, TTitle, TRoundCount, TFightMinute, TFightSecond, TRestMinute, TRestSecond, TWait) VALUES (5, 0, 0, 0, 0, 0, 0, 0)")
    mycursor.execute("INSERT INTO tblTimer (TID, TTitle, TRoundCount, TFightMinute, TFightSecond, TRestMinute, TRestSecond, TWait) VALUES (6, 0, 0, 0, 0, 0, 0, 0)")
    mycursor.execute("INSERT INTO tblTimer (TID, TTitle, TRoundCount, TFightMinute, TFightSecond, TRestMinute, TRestSecond, TWait) VALUES (7, 0, 0, 0, 0, 0, 0, 0)")
    mycursor.execute("INSERT INTO tblTimer (TID, TTitle, TRoundCount, TFightMinute, TFightSecond, TRestMinute, TRestSecond, TWait) VALUES (8, 0, 0, 0, 0, 0, 0, 0)")
    mycursor.execute("INSERT INTO tblTimer (TID, TTitle, TRoundCount, TFightMinute, TFightSecond, TRestMinute, TRestSecond, TWait) VALUES (9, 0, 0, 0, 0, 0, 0, 0)")
    mycursor.execute("INSERT INTO tblTimer (TID, TTitle, TRoundCount, TFightMinute, TFightSecond, TRestMinute, TRestSecond, TWait) VALUES (10, 0, 0, 0, 0, 0, 0, 0)")
con.commit()

class GYM:
    def select(self,number):
        sql = "SELECT * FROM tblTimer WHERE TID=?"
        record = mycursor.execute(sql,[str(number)]).fetchall()
        if record:
            return record
    def delete(TID):
        sql = "UPDATE tblTimer SET TTitle = ?  , TRoundCount = ? , TFightMinute = ?, TFightSecond = ? , TRestMinute = ? , TRestSecond = ? , TWait = ?  WHERE TID=?"
        val = ("",0,0,0,0,0,0,TID)
        record = mycursor.execute(sql,val)
        con.commit()
        if record:
            return record
    def save(TID,TTitle,TRoundCount,TFightMinute,TFightSecond,TRestMinute,TRestSecond,TWait):
        sql = "Update tblTimer set TTitle = ? , TRoundCount = ? , TFightMinute = ? , TFightSecond = ?, TRestMinute = ? , TRestSecond = ? , TWait = ?  Where TID=?"
        val = (TTitle,TRoundCount,TFightMinute,TFightSecond,TRestMinute,TRestSecond,TWait,TID)
        record = mycursor.execute(sql,val)
        con.commit()
        if record:
            return record