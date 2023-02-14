# module should contain all related functions and classes

import converter
from converter import kg_to_lbs

print(kg_to_lbs(40))

print(converter.lbs_to_kg(70))

# Package

# folder as package -- _init_.py
# import ecommerce.shipping
# ecommerce.shipping.calc_shipping()

# from ecommerce.shipping import calc_shipping()
# calc_shipping() --- calling normally as function 
