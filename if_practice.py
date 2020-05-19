#  if 연습
#  멤버수로 아이돌 찾기. 10: nct127 , 9: EXO 7: 방탄소년단 , 4: 마마무 , 13: 슈퍼주니어 , 그외 : 못찾았어요.
#  member = int(input("아이돌을 찾아보자. 멤버수를 입력하세요 : "))  # "13"으로 입력한 것과 같음
#  if member == 10:
#      print("nct127")
#  elif member == 9:
#      print("exo 중에 최고는 백현")
#  elif member == 7:
#      print("방탄소년단")
#  elif member == 4:
#      print("마마무")
#  elif member == 13:
#      print("슈퍼주니어 중에 최고는 은혁")
#  else:
#       print("못찾았어요")

# 평점 매기기. 90 이상 : A, 80 이상 90 미만 : B, 70 이상 80 미만 : C, 70 미만 : F

score = int(input("당신의 점수는?"))
if 90 <= score:
    print("A")
elif 80 <= score < 90:
    print("B")
elif 70 <= score < 80:
    print("C")
elif score < 70:
    print("F")
