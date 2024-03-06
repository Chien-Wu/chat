def read_file(filename):
	chat = []
	with open(filename, "r", encoding = "utf-8-sig") as f:
		for line in f:
			chat.append(line.strip().split())
	return chat


def count_words(chat):
	Allen_word_count = 0
	Allen_photo_count = 0
	Allen_sticker_count = 0
	Viki_word_count = 0
	Viki_photo_count = 0
	Viki_sticker_count = 0
	for line in chat:
		name = line[1]
		if name == "Allen":
			if line[2] == "圖片":
				Allen_photo_count += 1
			elif line[2] == "貼圖":
				Allen_sticker_count += 1
			else:
				for m in line[2:]:
					Allen_word_count += len(m)
		if name == "Viki":
			if line[2] == "圖片":
				Viki_photo_count += 1
			elif line[2] == "貼圖":
				Viki_sticker_count += 1
			else:
				for m in line[2:]:
					Viki_word_count += len(m)
	print("Allen:", Allen_word_count, "words,", Allen_photo_count, "photos,", Allen_sticker_count, "stickers")
	print("Viki:", Viki_word_count, "words,", Viki_photo_count, "photos,", Viki_sticker_count, "stickers")


def main():
	chat = read_file("LINE-Viki.txt")
	new = count_words(chat)

main()





