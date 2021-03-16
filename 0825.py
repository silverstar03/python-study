# f1 = open("tmp/write.txt", 'w', encoding="utf-8")
#
# f1.write("안녕하세요.\n")
# f1.write("2203 강은별입니다.")
#
# f1.close()

# f2 = open("tmp/append.txt",mode='a',encoding="utf-8")
# f2.write("append\n")
# f2.close()

# with open("tmp/with.txt", 'w', newline='', encoding='utf-8') as f:
#     f.write("with 구문 사용하기\n")
#     f.write("2번째 줄\n")
#     f.write("3번째 줄")

# with open('tmp/with.txt', 'r', encoding='utf-8') as f:
#     text = f.read()
#     print(text)

# with open('tmp/with.txt', 'r', encoding='utf-8') as f:
#     lines = f.readlines()
#     print("줄 수 :", len(lines))
#     for idx, line in enumerate(lines):
#         print("[" + str(idx) + "]", line, end="")
#     print()

# def copy_file(src, dest):
#     with open(src, 'rb') as copied
#         rbytes = copied.read()
#         with open(dest, 'wb') as new:
#             new.write(rbytes)

import os
import shutil
from pathlib import Path

# os.mkdir("hello")
# os.mkdir("hello/asdf")
# os.mkdir("hello/asdf/bye") os는 상위 클래스가 없으면 만들어줘야 함

# Path("hello").mkdir(parents=True, exist_ok=True) #hello라는 디렉토리를 만든다는 것
# print(Path("hello").exists())
# path는 os가 귀찮아서 만든 것이다.
# exist_ok=False는 폴더가 존재하면 에러, True는 이미 폴더가 있어도 에러가 안뜸

# Path("hello").rename("bye")

