



def score_grade(my_score):

    if my_score >= 4.5 :
        return("A+")
    elif my_score >= 4.0 and my_score < 4.5:
        return("A0")
    elif my_score >= 3.5 and my_score < 4.0:
        return("B+")
    elif my_score >= 3.0 and my_score < 3.5:
        return("B0")
    else :
        return("F")



my_score = float(input("당신의 점수를 입력해 주세요\n"))

result = score_grade(my_score)

print(f"당신의 등급은 {result}입니다.")

