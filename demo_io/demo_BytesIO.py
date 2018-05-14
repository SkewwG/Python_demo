import io

# write与getvalue对应
BytesIO_F = io.BytesIO()
BytesIO_F.write(b'qwerasdfzcxv')        # 写入内存必须是字节型
fwrite = BytesIO_F.getvalue()           # 从内存中读取出来
print(fwrite)

# BytesIO()与read()对应
fw = io.BytesIO(b'zxcvasdfweqr')        # 写入内存必须是字节型
fread = fw.read()                       # 从内存中读取出来
print(fread)