class restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
class IceCreamStand(restaurant):
	def __init__(self,name,cuisine_type,flavors):
		super().__init__(name,cuisine_type)
		self.flavors = flavors
	def show_flavors(self):
		for flavor in  self.flavors:
			print(flavor)
iceCream=IceCreamStand('aa','bb',['aaa','bbb','ccc'])
iceCream.show_flavors()
