def read_file():
    result = []
    with open("./student_grade_input.txt",encoding="utf8") as fin:
        for line in fin:
            line = line[:-1]
            result.append(line.split(","))
    return result


def sort_grades(datas):
    return sorted(datas,key=lambda item:int(item[2]),reverse=True)


def write_file(datas):
    with open('./student_grade_output.txt',"w",encoding="utf8") as fout:
        for item in datas:
            fout.write(",".join(item) + "\n")


datas = read_file()
datas = sort_grades(datas)
# print(datas)
write_file(datas)