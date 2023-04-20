
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines


def convert(lines):
    allen_word_count = 0
    allen_sticker_count = 0
    allen_photo_count = 0
    viki_word_count = 0
    viki_sticker_count = 0
    viki_photo_count = 0
    for line in lines:
        s = line.split(" ")
        time = s[0]
        name = s[1]
        if name == "Allen":
            if s[2] == "貼圖":
                allen_sticker_count += 1
            elif s[2] == "圖片":
                allen_photo_count +=1
            else:
                for m in s[2:]:
                    allen_word_count += len(m)

        elif name == "Viki":
            if s[2] == "貼圖":
                viki_sticker_count += 1
            elif s[2] == "圖片":
                viki_photo_count +=1
            else:
                for m in s[2:]:
                    viki_word_count += len(m)
    print("Allen say", allen_word_count, "words,", "sent",allen_sticker_count, "stickers, and sent", allen_photo_count, "photos" )
    print("Viki say", viki_word_count, "words,", "sent", viki_sticker_count, "stickers, and sent", viki_photo_count, "photos" )
      
       
def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')    


def main():
    lines = read_file('LINE-Viki.txt')
    lines = convert(lines)
    # write_file("output.txt", lines)
main()
