lines = []
with open("3.txt", "r", encoding = "utf-8-sig")as f:
	for line in f:
		lines.append(line.strip())

for line in lines:
	s = line.split(" ")
	name = s[0][5:]
	message = s[1]
	print(name, ":", message)