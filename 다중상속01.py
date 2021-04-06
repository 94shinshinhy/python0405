#다중상속의 문제점
class Tiger:
    def jump(self):
        print("호랑이 점프")
    def cry(self):
        print("호랑이 어흥")

class Lion:
    def bite(self):
        print("사자 물어뜯기")
    def cry(self):
        print("사자 으르릉")

class Liger(Lion, Tiger):
    def play(self):
        print("라이거와 놀기")

#인스턴스 생성
l = Liger()
l.cry()
print("내부에 상속 순서 튜플 : {0}".format(Liger.__mro__))
# l = Liger()
# l.play()
# l.jump()
# l.bite()

        
