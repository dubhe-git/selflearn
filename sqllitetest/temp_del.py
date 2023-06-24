import sqlite3
import os

conn = sqlite3.connect('files.db')
c = conn.cursor()

# 创建数据表
# c.execute('''CREATE TABLE files
#              (id INTEGER PRIMARY KEY AUTOINCREMENT,
#              name TEXT NOT NULL,
#              path TEXT NOT NULL,
#              UNIQUE(name, path))''')

# 指定要遍历的硬盘路径
paths = ["D:\\bluefilm", "E:\\Blue avi", "F:\\Blue shows", "G:\\Blue shows"]

for path in paths:
    for dirname, subdirlist, filelist in os.walk(path):
        for filename in filelist:
            fullpath = os.path.join(dirname, filename)
            try:
                c.execute('INSERT INTO files (name, path) VALUES (?, ?)', (filename, fullpath))
                conn.commit()
            except sqlite3.IntegrityError:
                print(f'{filename} already exists in {fullpath}')

conn.close()
