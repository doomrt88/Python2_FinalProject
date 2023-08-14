import sqlite3
from contextlib import closing

class SpeechToAudio():
    def __init__(self, file_name, file_blob, text_speech):
        self.id = id
        self.file_name = file_name
        self.file_blob = file_blob
        self.text_speech = text_speech

    def __str__(self)->str:
        return f"file_name: {self.file_name}\t text: {self.text_speech}"


class DB():
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.conn.row_factory = sqlite3.Row

    def ping(self):
        with closing(self.conn.cursor()) as cur:
            sql = "select 'ping' as col"
            resp = cur.execute(sql)
            for r in resp.fetchall():
                print(r['col'])

    def get_audios(self):
        with closing(self.conn.cursor()) as cur:
            sql = '''select file_name,file_blob,text_speech from speechtoaudio order by id asc;'''
            audios = []
            print('testDb')
            rows = cur.execute(sql)
            print('testDb2')
            for row in rows.fetchall():
                audio = SpeechToAudio(row['file_name'],row['file_blob'],row['text_speech'])
                audios.append(audio)
            return audios
        
    def insert(self, speechToAudio):
        with closing(self.conn.cursor()) as cur:
            sql = '''
            insert into speechtoaudio (file_name,file_blob,text_speech) values(?,?,?);
            '''
            cur.execute(sql,[speechToAudio.file_name, speechToAudio.file_blob,speechToAudio.text_speech])
            self.conn.commit()
