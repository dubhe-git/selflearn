import sqlite3

# 连接到数据库
conn = sqlite3.connect('files.db')
c = conn.cursor()

# 删除数据表中所有数据
c.execute('DELETE FROM files')

# 确认删除操作
conn.commit()

# 关闭连接
conn.close()