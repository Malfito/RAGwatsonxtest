import singlestoredb as s2

conn = s2.connect(
    host="svc-28322643-c328-4e40-bfdb-8ea6ee323942-dml.gcp-mumbai-2.svc.singlestore.com",
    port=3306,
    user="admin",
    password="qfbk|azMenmObmpx;7G1d;:e",
    database="rag_db"
)

cursor = conn.cursor()
cursor.execute("SELECT 1;")
print(cursor.fetchone())

conn.close()
