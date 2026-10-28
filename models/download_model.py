from database.db imporet get_db_connection

class DowloadModel:
    @staticmethod
    def find_by_filename(filename):
        conn = get_db_connection()
        file = conn.execute('SELECT = FROM uploads WHERE filename = ?', (filename)).fetchone()
        conn.close()
        return file