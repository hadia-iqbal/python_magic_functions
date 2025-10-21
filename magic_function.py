class Product:
    def __init__(self,name,price):
        self.name=name;
        self.price=price;
    def __str__(self):
        return f"{self.name} (Rs.{self.price})";
class Shopping_cart:
    def __init__(self):
        self.items=[];
    def add_items(self, product):
        self.items.append(product);
    def __str__(self):
        cart_content=','.join(p.name for p in self.items);
        total=sum(p.price for p in self.items);
        return f" Cart: [{cart_content}]  |  Total: {total}";
    def __len__(self):
        return len(self.items);
    def __add__(self, other):
        new_cart=Shopping_cart();
        new_cart.items=self.items+other.items;
        return new_cart;
    def __eq__(self, other):
        return sum(p.price for p in self.items)==sum(p.price for p in other.items);
p1=Product("Laptop",85000);
p2=Product("Mouse",1500);
p3=Product("Headphones",800);
p4=Product("Keyboard",1000);
c1=Shopping_cart();
c2=Shopping_cart();
c1.add_items(p1);
c1.add_items(p2);
c2.add_items(p3);
c2.add_items(p4);
print(c1);
print(c2);
merged_cart=c1+c2;
print("\n Merged: ",merged_cart);
print("\n Are both carts equal in price: ",c1==c2);
print("\n Total items in merged cart :",len(merged_cart));




