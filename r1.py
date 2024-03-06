def read_file(filename):
	chat = []
	with open(filename, "r", encoding = "utf-8-sig") as f:
		for line in f:
			chat.append(line.strip())
	return chat

def convert(chat):
	new = []
	for line in chat:
		if line == "Allen":
			person = "Allen"
		elif line == "Tom":
			person = "Tom"
		else:
			new.append(person + ":" + line + "\n")
	return new

def write_chat(filename, new):
	with open (filename, "w", encoding = "utf-8-sig") as f:
		for line in new:
			f.write(line)

def main():
	chat = read_file("input.txt")
	print(chat)
	new = convert(chat)
	write_chat("output.txt",new)

main()


