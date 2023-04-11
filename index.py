from appliances.kitchen import DishWasher
from appliances import Dryer
from appliances import Washer
from appliances.kitchen import Refrigerator
from appliances.kitchen import CoffeeMaker
from appliances.kitchen import CanOpener

whirlpool_dishwasher = DishWasher("black")
whirlpool_dishwasher.wash_dishes()

samsung_washer = Washer("red", "gas")
samsung_dryer = Dryer("red", "gas")

lg_fridge = Refrigerator("stainless")
lg_fridge.make_ice()

mr_coffee = CoffeeMaker("white")
mr_coffee.make_coffee()

automatic_canopener = CanOpener('black')
automatic_canopener.open_can()
