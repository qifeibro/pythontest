with open("bill.txt","r",encoding="UTF-8") as fr:
	with open("bill.txt.bak", "w",encoding="UTF-8") as fw:
		for line in fr:
			l = line.strip().split(",")
			if l[-1] == "测试":
				continue
			fw.write(line)
