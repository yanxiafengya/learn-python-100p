# def read_file():
#     result = []
#     with open("./student_grade_input.txt",encoding='utf8') as fin:
#         for line in fin:
#             line = line[:-1]
#             result.append(line.split(","))
#     return result
#
# datas = read_file()
# for data in datas:
#     data[2] = int(data[2])
# print(datas)
#
# def computer_score(datas):
#     max_score = min_score = int(datas[0][2])
#     avg_score = sum_score =0,
#     for score in datas:
#         if score[2] > max_score:
#             max_score = score[2]
#     for score in datas:
#         sum_score += score[2]
#     for score in datas[2]:
#         if score[2] <min_score:
#             min_score = score[2]
#
#     avg = sum_score / len(datas)
#
#     return max_score,min_score,avg_score

def computer_score():
    scores = []
    with open("./student_grade_input.txt",encoding='utf8') as fin:
        for line in fin:
            line = line[:-1]
            item = line.split(",")
            scores.append(int(item[-1]))
    max_score = max(scores)
    min_score = min(scores)
    avg_score = round(sum(scores)/len(scores),2)
    return max_score,min_score,avg_score


max_score,min_score,avg_score = computer_score()
print(max_score,min_score,avg_score)