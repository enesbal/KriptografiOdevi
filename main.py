import hashlib
file=open("md5.txt")
read= file.read()
yedinciler=""

i=int(input("Parola icin karakter sayisi giriniz: "))
for k in range(i):
	read=hashlib.md5(read.encode('utf-8')).hexdigest()
	yedinciler+=read[7]

print("deger: ", int(yedinciler,16))
