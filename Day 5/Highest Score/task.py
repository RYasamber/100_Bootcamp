student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
b_num = 0
for scores in student_scores:
    if scores > b_num:
        b_num = scores
print(b_num)
