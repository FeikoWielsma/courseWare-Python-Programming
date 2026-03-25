class FoodExpert:
    def init(self):
        self.good_food = []

    def add_good_food(self, food):
        self.good_food.append(food)

    def likes(self, x):
        return x in self.good_food

    def prefers(self, x, y):
        assert self.likes(x) and self.likes(y)
        x_rating = self.good_food.index(x)
        y_rating = self.good_food.index(y)
        if x_rating > y_rating:
            return y
        else:
            return x


f = FoodExpert()
f.add_good_food("Pizza")
f.likes("Pizza")
f.likes("Pasta")
