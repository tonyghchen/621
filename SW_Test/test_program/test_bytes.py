message="Hello哈囉"  #0xe5,0x93,0x88  0xe5,0x9b,0x89
byte_message = bytes(message, 'utf-8')
print(byte_message)
byte_size=bytes(10)
print(byte_size) 

print(byte_size+byte_message)

rList = [1, 2, 3, 4, 5,65,255]   #65='A',陣列的值不能大於255

arr = bytes(rList)
print(arr)

