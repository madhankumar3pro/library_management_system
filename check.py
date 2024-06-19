class Checkout:
    def __init__(self, user_id, isbn):
        self.user_id = user_id
        self.isbn = isbn

    def __str__(self):
        return f"User ID: {self.user_id}, ISBN: {self.isbn}"


# Storage for checkouts
class CheckoutManager:
    def __init__(self):
        self.checkouts = []

    def add_checkout(self, user_id, isbn):
        checkout = Checkout(user_id, isbn)
        self.checkouts.append(checkout)

    def list_checkouts(self):
        for checkout in self.checkouts:
            print(checkout)

    def delete_checkout(self, user_id, isbn):
        self.checkouts = [checkout for checkout in self.checkouts if not (checkout.user_id == user_id and checkout.isbn == isbn)]


