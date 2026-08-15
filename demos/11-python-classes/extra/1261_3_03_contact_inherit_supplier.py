class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        print("tets")
        Contact.all_contacts.append(self)


class Supplier(Contact):
    def order(self, order):
        print(
            f"If this were a real system we would send {order} order to {self.name}"
        )


s = Supplier("a", "b")
