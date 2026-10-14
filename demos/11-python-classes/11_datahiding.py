class Secretive:
    __secret_count = 0

    def count(self):
        self.__secret_count += 1
        print(self.__secret_count)

    def __inaccessible(self):
        print("Bet you can't see me...")

    def accessible(self):
        print("The secret message is:")
        self.__inaccessible()


s = Secretive()
s.accessible()
s._Secretive__inaccessible()
# s.__inaccessible()

s.count()
s.count()

print(s._Secretive__secret_count)
# print(s.__secret_count)  # AttributeError
