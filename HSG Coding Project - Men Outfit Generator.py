#!/usr/bin/env python
# coding: utf-8

# # Men Outfit Generator 3000
# 
# ### Do you ever wake up and think "Ughhh I wish my mom still picked my outfits"? 
# ### Do you feel like people look at you funny because your outfit's colour scheme looks like a rainbow? 
# ### Do you feel like you wear the same outfit every day because you have no inspiration?
# 
# If you answered yes to any of the questions, we are here to help you!
# 
# Men Outfit Generator 3000 is a tool created to inspire men on what they should wear. It has all types of items that you probably already have on your wardrobe, I mean, who doesn't own a black t-shirt or some blue jeans? 
# 
# How to use it? Very simple:
# 
# - First insert your location
# - Second in how many days you want the outfit (don't worry, if you are that desperate and need to think of an outfit for today we got you covered! Just put that you want an outfit in 0 days)
# - Third choose the type of outfit - casual, sporty or formal
# - Forth lay back, relax and let us choose an outfit for you
# 
# Don't like the outfit we picked or you don't have a specific piece? Don't worry, we thought of everything! You can ask for a new outfit or ask to replace a specific piece
# 

# In[12]:


import random
import requests
import json


#Creating variables wardrobe, outfit, and weather which will be used later on
wardrobe = []
outfit = []
weather =""

#sunglasses
list_of_sunglasses = []
list_of_sunglasses_fit = []

#hats
list_of_hats = []
list_of_hats_fit = []

#umbrellas
list_of_umbrellas = []
list_of_umbrellas_fit = []

#scarf
list_of_scarf = []
list_of_scarf_fit = []

#tops
list_of_tops = []
list_of_tops_fit = []

#Outerwear
list_of_outerwear = []
list_of_outerwear_fit = []

#bottoms
list_of_bottoms = []
list_of_bottoms_fit = []

#Shoes
list_of_shoes = []
list_of_shoes_fit = []


            #Colour schemes for outfits
scheme1 = ["blue", "white", "grey"]
scheme2 = ["black", "white"]
scheme3 = ["blue", "green", "white"]
scheme4 = ["red", "black"]
scheme5 = ["red", "blue", "white"]
scheme6 = ["yellow", "black"]
scheme7 = ["orange", "blue", "white"]
scheme8 = ["brown", "white"]
scheme9 = ["green", "white", "brown"]
scheme10 = ["green", "yellow"]
scheme11 = ["brown", "black"]
scheme12 = ["white", "black", "brown"]
scheme13 = ["blue", "white", "brown"]
scheme14 = ["green", "white"]
scheme15 = ["blue", "white"]
scheme16 = ["pink", "white", "blue"]
scheme17 = ["purple", "white", "grey"]
scheme18 = ["red", "white", "grey"]

#List of all schemes to choose from
schemes = [scheme1,scheme2,scheme3,scheme4,scheme5,scheme6,scheme7,scheme8,scheme9,scheme10,scheme11,scheme12,scheme13,scheme14,scheme15,scheme16,scheme17,scheme18]

#Creating the class for clothing
class clothing:
    def __init__(self, name, colour, category, occasion, weather, temperature):
        self.name = name
        self.category = category
        self.occasion = occasion
        self.weather = weather
        self.colour = colour
        self.temperature = temperature


# In[13]:


#creating function to add new clothing to the wardrobe
def add_clothing_to_wardrobe(name, colour, category, occasion, weather, temperature):
    name = clothing(name, colour, category, occasion, weather, temperature)
    wardrobe.append(name)


# In[14]:



#add a bunch of clothing to the wardrobe
add_clothing_to_wardrobe("round", "blue", "sunglasses", "casual", ["sunny"], ["cold","mild","hot"])
add_clothing_to_wardrobe("round", "red", "sunglasses", "casual", ["sunny"], ["cold","mild","hot"])
add_clothing_to_wardrobe("round", "black", "sunglasses", "casual", ["sunny"], ["cold","mild","hot"])
add_clothing_to_wardrobe("round", "white", "sunglasses", "casual", ["sunny"], ["cold","mild","hot"])
add_clothing_to_wardrobe("retro", "red", "sunglasses", "casual", ["sunny"], ["cold","mild","hot"])
add_clothing_to_wardrobe("retro", "blue", "sunglasses", "casual", ["sunny"], ["cold","mild","hot"])
add_clothing_to_wardrobe("retro", "white", "sunglasses", "casual", ["sunny"], ["cold","mild","hot"])
add_clothing_to_wardrobe("retro", "black", "sunglasses", "casual", ["sunny"], ["cold","mild","hot"])
add_clothing_to_wardrobe("squared", "black", "sunglasses", "formal", ["sunny"], ["cold","mild","hot"])
add_clothing_to_wardrobe("squared", "white", "sunglasses", "formal", ["sunny"], ["cold","mild","hot"])
add_clothing_to_wardrobe("squared", "blue", "sunglasses", "formal", ["sunny"], ["cold","mild","hot"])
add_clothing_to_wardrobe("squared", "red", "sunglasses", "formal", ["sunny"], ["cold","mild","hot"])
add_clothing_to_wardrobe("aviator", "white", "sunglasses", "formal", ["sunny"], ["cold","mild","hot"])
add_clothing_to_wardrobe("aviator", "black", "sunglasses", "formal", ["sunny"], ["cold","mild","hot"])
add_clothing_to_wardrobe("aviator", "blue", "sunglasses", "formal", ["sunny"], ["cold","mild","hot"])
add_clothing_to_wardrobe("aviator", "red", "sunglasses", "formal", ["sunny"], ["cold","mild","hot"])
add_clothing_to_wardrobe("sporty", "blue", "sunglasses", "sporty", ["sunny"], ["cold","mild","hot"])
add_clothing_to_wardrobe("sporty", "red", "sunglasses", "sporty", ["sunny"], ["cold","mild","hot"])
add_clothing_to_wardrobe("sporty", "white", "sunglasses", "sporty", ["sunny"], ["cold","mild","hot"])
add_clothing_to_wardrobe("sporty", "black", "sunglasses", "sporty", ["sunny"], ["cold","mild","hot"])
add_clothing_to_wardrobe("panama", "white", "hat", "formal", ["sunny"], ["mild","hot"])
add_clothing_to_wardrobe("panama", "blue", "hat", "formal", ["sunny"], ["mild","hot"])
add_clothing_to_wardrobe("panama", "black", "hat", "formal", ["sunny"], ["mild","hot"])
add_clothing_to_wardrobe("panama", "grey", "hat", "formal", ["sunny"], ["mild","hot"])
add_clothing_to_wardrobe("baseball cap", "black", "hat", "casual", ["sunny"], ["mild","hot"])
add_clothing_to_wardrobe("baseball cap", "green", "hat", "casual", ["sunny"], ["mild","hot"])
add_clothing_to_wardrobe("baseball cap", "white", "hat", "casual", ["sunny"], ["mild","hot"])
add_clothing_to_wardrobe("baseball cap", "yellow", "hat", "casual", ["sunny"], ["mild","hot"])
add_clothing_to_wardrobe("baseball cap", "pink", "hat", "casual", ["sunny"], ["mild","hot"])
add_clothing_to_wardrobe("baseball cap", "grey", "hat", "casual", ["sunny"], ["mild","hot"])
add_clothing_to_wardrobe("baseball cap", "blue", "hat", "casual", ["sunny"], ["mild","hot"])
add_clothing_to_wardrobe("cap", "blue", "hat", "sporty", ["sunny"], ["mild","hot"])
add_clothing_to_wardrobe("cap", "white", "hat", "sporty", ["sunny"], ["mild","hot"])
add_clothing_to_wardrobe("cap", "grey", "hat", "sporty", ["sunny"], ["mild","hot"])
add_clothing_to_wardrobe("cap", "black", "hat", "sporty", ["sunny"], ["mild","hot"])
add_clothing_to_wardrobe("cashmere", "black", "scarf", "formal", ["sunny","cloudy","rainy"], ["cold"])
add_clothing_to_wardrobe("cashmere", "white", "scarf", "formal", ["sunny","cloudy","rainy"], ["cold"])
add_clothing_to_wardrobe("cashmere", "blue", "scarf", "formal", ["sunny","cloudy","rainy"], ["cold"])
add_clothing_to_wardrobe("cotton", "white", "scarf", "casual", ["sunny","cloudy","rainy"], ["cold"])
add_clothing_to_wardrobe("cotton", "blue", "scarf", "casual", ["sunny","cloudy","rainy"], ["cold"])
add_clothing_to_wardrobe("cotton", "black", "scarf", "casual", ["sunny","cloudy","rainy"], ["cold"])
add_clothing_to_wardrobe("linen", "blue", "scarf", "casual", ["sunny","cloudy","rainy"], ["cold"])
add_clothing_to_wardrobe("linen", "white", "scarf", "casual", ["sunny","cloudy","rainy"], ["cold"])
add_clothing_to_wardrobe("linen", "black", "scarf", "casual", ["sunny","cloudy","rainy"], ["cold"])
add_clothing_to_wardrobe("linen", "grey", "scarf", "casual", ["sunny","cloudy","rainy"], ["cold"])
add_clothing_to_wardrobe("polo", "blue", "top", "casual", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("polo", "black", "top", "casual", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("polo", "white", "top", "casual", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("polo", "brown", "top", "casual", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("polo", "green", "top", "casual", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("polo", "grey", "top", "casual", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("polo", "yellow", "top", "casual", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("polo", "red", "top", "casual", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("polo", "orange", "top", "casual", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("polo", "white", "top", "formal", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("polo", "black", "top", "formal", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("polo", "grey", "top", "formal", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("polo", "brown", "top", "formal", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("t-shirt", "black", "top", "casual", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("t-shirt", "white", "top", "casual", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("t-shirt", "green", "top", "sporty", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("t-shirt", "yellow", "top", "casual", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("t-shirt", "orange", "top", "casual", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("t-shirt", "brown", "top", "casual", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("t-shirt", "blue", "top", "casual", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("t-shirt", "grey", "top", "casual", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("t-shirt", "red", "top", "casual", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("shirt", "white", "top", "formal", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("shirt", "black", "top", "formal", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("shirt", "blue", "top", "formal", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("sleeveless shirt", "red", "top", "sporty", ["sunny","cloudy"], ["mild","hot"])
add_clothing_to_wardrobe("sleeveless shirt", "black", "top", "sporty", ["sunny","cloudy"], ["mild","hot"])
add_clothing_to_wardrobe("sleeveless shirt", "grey", "top", "sporty", ["sunny","cloudy"], ["mild","hot"])
add_clothing_to_wardrobe("sleeveless shirt", "white", "top", "sporty", ["sunny","cloudy"], ["mild","hot"])
add_clothing_to_wardrobe("sleeveless shirt", "blue", "top", "sporty", ["sunny","cloudy"], ["mild","hot"])
add_clothing_to_wardrobe("long-sleeve", "black", "top", "casual", ["sunny","cloudy","rainy"], ["cold","mild"])
add_clothing_to_wardrobe("long-sleeve", "white", "top", "casual", ["sunny","cloudy","rainy"], ["cold","mild"])
add_clothing_to_wardrobe("long-sleeve", "red", "top", "casual", ["sunny","cloudy","rainy"], ["cold","mild"])
add_clothing_to_wardrobe("long-sleeve", "blue", "top", "casual", ["sunny","cloudy","rainy"], ["cold","mild"])
add_clothing_to_wardrobe("long-sleeve", "grey", "top", "casual", ["sunny","cloudy","rainy"], ["cold","mild"])
add_clothing_to_wardrobe("linen shirt", "blue", "top", "casual", ["sunny","cloudy"], ["mild","hot"])
add_clothing_to_wardrobe("linen shirt", "black", "top", "casual", ["sunny","cloudy"], ["mild","hot"])
add_clothing_to_wardrobe("linen shirt", "white", "top", "casual", ["sunny","cloudy"], ["mild","hot"])
add_clothing_to_wardrobe("linen shirt", "green", "top", "casual", ["sunny","cloudy"], ["mild","hot"])
add_clothing_to_wardrobe("linen shirt", "pink", "top", "casual", ["sunny","cloudy"], ["mild","hot"])
add_clothing_to_wardrobe("short-sleeved shirt", "grey", "top", "casual", ["sunny","cloudy"], ["hot"])
add_clothing_to_wardrobe("short-sleeved shirt", "green", "top", "casual", ["sunny","cloudy"], ["hot"])
add_clothing_to_wardrobe("short-sleeved shirt", "black", "top", "casual", ["sunny","cloudy"], ["hot"])
add_clothing_to_wardrobe("short-sleeved shirt", "blue", "top", "casual", ["sunny","cloudy"], ["hot"])
add_clothing_to_wardrobe("short-sleeved shirt", "white", "top", "casual", ["sunny","cloudy"], ["hot"])
add_clothing_to_wardrobe("turtleneck", "brown", "top", "casual", ["sunny","cloudy","rainy"], ["cold"])
add_clothing_to_wardrobe("turtleneck", "purple", "top", "casual", ["sunny","cloudy","rainy"], ["cold"])
add_clothing_to_wardrobe("turtleneck", "black", "top", "formal", ["sunny","cloudy","rainy"], ["cold"])
add_clothing_to_wardrobe("turtleneck", "blue", "top", "formal", ["sunny","cloudy","rainy"], ["cold"])
add_clothing_to_wardrobe("sweater", "pink", "top", "casual", ["sunny","cloudy","rainy"], ["cold","mild"])
add_clothing_to_wardrobe("sweater", "red", "top", "casual", ["sunny","cloudy","rainy"], ["cold","mild"])
add_clothing_to_wardrobe("sweater", "orange", "top", "casual", ["sunny","cloudy","rainy"], ["cold","mild"])
add_clothing_to_wardrobe("sweater", "grey", "top", "sporty", ["sunny","cloudy","rainy"], ["cold","mild"])
add_clothing_to_wardrobe("sweater", "blue", "top", "sporty", ["sunny","cloudy","rainy"], ["cold","mild"])
add_clothing_to_wardrobe("sweater", "white", "top", "sporty", ["sunny","cloudy","rainy"], ["cold","mild"])
add_clothing_to_wardrobe("sweater", "black", "top", "sporty", ["sunny","cloudy","rainy"], ["cold","mild"])
add_clothing_to_wardrobe("linen pants", "black", "bottom", "casual", ["sunny","cloudy"], ["mild","hot"])
add_clothing_to_wardrobe("linen pants", "blue", "bottom", "casual", ["sunny","cloudy"], ["mild","hot"])
add_clothing_to_wardrobe("linen pants", "white", "bottom", "casual", ["sunny","cloudy"], ["mild","hot"])
add_clothing_to_wardrobe("linen pants", "grey", "bottom", "casual", ["sunny","cloudy"], ["mild","hot"])
add_clothing_to_wardrobe("suit pants", "black", "bottom", "formal", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("suit pants", "blue", "bottom", "formal", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("suit pants", "grey", "bottom", "formal", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("jeans", "black", "bottom", "casual", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("jeans", "grey", "bottom", "casual", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("jeans", "blue", "bottom", "casual", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("cargo pants", "blue", "bottom", "casual", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("cargo pants", "green", "bottom", "casual", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("cargo pants", "brown", "bottom", "casual", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("cargo pants", "grey", "bottom", "casual", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("shorts", "red", "bottom", "casual", ["sunny","cloudy"], ["mild","hot"])
add_clothing_to_wardrobe("shorts", "black", "bottom", "casual", ["sunny","cloudy"], ["mild","hot"])
add_clothing_to_wardrobe("trousers", "white", "bottom", "formal", ["sunny","cloudy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("trousers", "blue", "bottom", "formal", ["sunny","cloudy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("trousers", "black", "bottom", "formal", ["sunny","cloudy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("trousers", "grey", "bottom", "formal", ["sunny","cloudy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("chinos pants", "white", "bottom", "formal", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("chinos pants", "grey", "bottom", "formal", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("chinos pants", "blue", "bottom", "formal", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("chinos pants", "black", "bottom", "formal", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("shorts", "white", "bottom", "sporty", ["sunny","cloudy","rainy"], ["mild","hot"])
add_clothing_to_wardrobe("shorts", "blue", "bottom", "sporty", ["sunny","cloudy","rainy"], ["mild","hot"])
add_clothing_to_wardrobe("shorts", "black", "bottom", "sporty", ["sunny","cloudy","rainy"], ["mild","hot"])
add_clothing_to_wardrobe("shorts", "red", "bottom", "sporty", ["sunny","cloudy","rainy"], ["mild","hot"])
add_clothing_to_wardrobe("shorts", "green", "bottom", "sporty", ["sunny","cloudy","rainy"], ["mild","hot"])
add_clothing_to_wardrobe("sweatpants", "blue", "bottom", "sporty", ["sunny","cloudy","rainy"], ["cold","mild"])
add_clothing_to_wardrobe("sweatpants", "black", "bottom", "sporty", ["sunny","cloudy","rainy"], ["cold","mild"])
add_clothing_to_wardrobe("sweatpants", "red", "bottom", "sporty", ["sunny","cloudy","rainy"], ["cold","mild"])
add_clothing_to_wardrobe("sweatpants", "grey", "bottom", "sporty", ["sunny","cloudy","rainy"], ["cold","mild"])
add_clothing_to_wardrobe("sweatpants", "white", "bottom", "sporty", ["sunny","cloudy","rainy"], ["cold","mild"])
add_clothing_to_wardrobe("sweatpants", "green", "bottom", "sporty", ["sunny","cloudy","rainy"], ["cold","mild"])
add_clothing_to_wardrobe("sneakers", "black", "shoes", "casual", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("sneakers", "white", "shoes", "casual", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("sneakers", "blue", "shoes", "casual", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("sneakers", "brown", "shoes", "casual", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("sneakers", "grey", "shoes", "casual", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("trainers", "white", "shoes", "sporty", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("trainers", "black", "shoes", "sporty", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("trainers", "blue", "shoes", "sporty", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("sneakers", "blue", "shoes", "sporty", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("boots", "blue", "shoes", "casual", ["sunny","cloudy","rainy"], ["cold","mild"])
add_clothing_to_wardrobe("boots", "black", "shoes", "casual", ["sunny","cloudy","rainy"], ["cold","mild"])
add_clothing_to_wardrobe("boots", "grey", "shoes", "casual", ["sunny","cloudy","rainy"], ["cold","mild"])
add_clothing_to_wardrobe("boots", "brown", "shoes", "casual", ["sunny","cloudy","rainy"], ["cold","mild"])
add_clothing_to_wardrobe("oxford shoes", "black", "shoes", "formal", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("oxford shoes", "brown", "shoes", "formal", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("loafers", "black", "shoes", "formal", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("loafers", "brown", "shoes", "formal", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("boots", "black", "shoes", "formal", ["cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("boots", "brown", "shoes", "formal", ["cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("blazer", "white", "outerwear", "formal", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("blazer", "black", "outerwear", "formal", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("blazer", "blue", "outerwear", "formal", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("blazer", "grey", "outerwear", "formal", ["sunny","cloudy","rainy"], ["cold","mild","hot"])
add_clothing_to_wardrobe("overcoat", "grey", "outerwear", "formal", ["cloudy","rainy"], ["cold"])
add_clothing_to_wardrobe("overcoat", "blue", "outerwear", "formal", ["cloudy","rainy"], ["cold"])
add_clothing_to_wardrobe("overcoat", "black", "outerwear", "formal", ["cloudy","rainy"], ["cold"])
add_clothing_to_wardrobe("trench coat", "black", "outerwear", "formal", ["rainy"], ["cold","mild"])
add_clothing_to_wardrobe("trench coat", "blue", "outerwear", "formal", ["rainy"], ["cold","mild"])
add_clothing_to_wardrobe("cardigan", "black", "outerwear", "casual", ["sunny","cloudy"], ["mild"])
add_clothing_to_wardrobe("cardigan", "blue", "outerwear", "casual", ["sunny","cloudy"], ["mild"])
add_clothing_to_wardrobe("cardigan", "grey", "outerwear", "casual", ["sunny","cloudy"], ["mild"])
add_clothing_to_wardrobe("cardigan", "brown", "outerwear", "casual", ["sunny","cloudy"], ["mild"])
add_clothing_to_wardrobe("trench coat", "black", "outerwear", "casual", ["rainy"], ["cold","mild"])
add_clothing_to_wardrobe("trench coat", "blue", "outerwear", "casual", ["rainy"], ["cold","mild"])
add_clothing_to_wardrobe("trench coat", "white", "outerwear", "casual", ["rainy"], ["cold","mild"])
add_clothing_to_wardrobe("rain coat", "white", "outerwear", "casual", ["rainy"], ["cold","mild"])
add_clothing_to_wardrobe("rain coat", "black", "outerwear", "casual", ["rainy"], ["cold","mild"])
add_clothing_to_wardrobe("rain coat", "blue", "outerwear", "casual", ["rainy"], ["cold","mild"])
add_clothing_to_wardrobe("rain coat", "red", "outerwear", "sporty", ["cloudy","rainy"], ["cold","mild"])
add_clothing_to_wardrobe("rain coat", "blue", "outerwear", "sporty", ["cloudy","rainy"], ["cold","mild"])
add_clothing_to_wardrobe("rain coat", "green", "outerwear", "sporty", ["cloudy","rainy"], ["cold","mild"])
add_clothing_to_wardrobe("jacket", "grey", "outerwear", "casual", ["sunny","cloudy","rainy"], ["cold","mild"])
add_clothing_to_wardrobe("jacket", "black", "outerwear", "casual", ["sunny","cloudy","rainy"], ["cold","mild"])
add_clothing_to_wardrobe("jacket", "red", "outerwear", "casual", ["sunny","cloudy","rainy"], ["cold","mild"])
add_clothing_to_wardrobe("jacket", "green", "outerwear", "casual", ["sunny","cloudy","rainy"], ["cold","mild"])
add_clothing_to_wardrobe("jacket", "blue", "outerwear", "casual", ["sunny","cloudy","rainy"], ["cold","mild"])
add_clothing_to_wardrobe("jacket", "white", "outerwear", "casual", ["sunny","cloudy","rainy"], ["cold","mild"])
add_clothing_to_wardrobe("zipped hoodie", "grey", "outerwear", "casual", ["sunny","cloudy"], ["cold","mild"])
add_clothing_to_wardrobe("zipped hoodie", "black", "outerwear", "casual", ["sunny","cloudy"], ["cold","mild"])
add_clothing_to_wardrobe("zipped hoodie", "blue", "outerwear", "casual", ["sunny","cloudy"], ["cold","mild"])
add_clothing_to_wardrobe("zipped hoodie", "white", "outerwear", "casual", ["sunny","cloudy"], ["cold","mild"])
add_clothing_to_wardrobe("zipped hoodie", "green", "outerwear", "casual", ["sunny","cloudy"], ["cold","mild"])
add_clothing_to_wardrobe("zipped hoodie", "red", "outerwear", "casual", ["sunny","cloudy"], ["cold","mild"])
add_clothing_to_wardrobe("vest", "black", "outerwear", "casual", ["sunny","cloudy","rainy"], ["hot"])
add_clothing_to_wardrobe("vest", "blue", "outerwear", "casual", ["sunny","cloudy","rainy"], ["hot"])
add_clothing_to_wardrobe("vest", "grey", "outerwear", "casual", ["sunny","cloudy","rainy"], ["hot"])
add_clothing_to_wardrobe("vest", "green", "outerwear", "casual", ["sunny","cloudy","rainy"], ["hot"])
add_clothing_to_wardrobe("vest", "orange", "outerwear", "casual", ["sunny","cloudy","rainy"], ["hot"])
add_clothing_to_wardrobe("vest", "white", "outerwear", "casual", ["sunny","cloudy","rainy"], ["hot"])
add_clothing_to_wardrobe("light jacket", "white", "outerwear", "casual", ["sunny","cloudy","rainy"], ["hot"])
add_clothing_to_wardrobe("light jacket", "black", "outerwear", "casual", ["sunny","cloudy","rainy"], ["hot"])
add_clothing_to_wardrobe("light jacket", "brown", "outerwear", "casual", ["sunny","cloudy","rainy"], ["hot"])
add_clothing_to_wardrobe("light jacket", "blue", "outerwear", "casual", ["sunny","cloudy","rainy"], ["hot"])
add_clothing_to_wardrobe("light jacket", "grey", "outerwear", "casual", ["sunny","cloudy","rainy"], ["hot"])
add_clothing_to_wardrobe("hoodie", "purple", "outerwear", "sporty", ["sunny","cloudy"], ["cold","mild"])
add_clothing_to_wardrobe("hoodie", "pink", "outerwear", "sporty", ["sunny","cloudy"], ["cold","mild"])
add_clothing_to_wardrobe("hoodie", "red", "outerwear", "sporty", ["sunny","cloudy"], ["cold","mild"])
add_clothing_to_wardrobe("hoodie", "black", "outerwear", "sporty", ["sunny","cloudy"], ["cold","mild"])
add_clothing_to_wardrobe("hoodie", "white", "outerwear", "sporty", ["sunny","cloudy"], ["cold","mild"])
add_clothing_to_wardrobe("hoodie", "blue", "outerwear", "sporty", ["sunny","cloudy"], ["cold","mild"])
add_clothing_to_wardrobe("hoodie", "green", "outerwear", "sporty", ["sunny","cloudy"], ["cold","mild"])
add_clothing_to_wardrobe("umbrella", "black", "umbrella", "sporty", ["rainy"], ["cold","mild", "hot"])
add_clothing_to_wardrobe("umbrella", "white", "umbrella", "sporty", ["rainy"], ["cold","mild", "hot"])
add_clothing_to_wardrobe("umbrella", "blue", "umbrella", "sporty", ["rainy"], ["cold","mild", "hot"])
add_clothing_to_wardrobe("umbrella", "green", "umbrella", "sporty", ["rainy"], ["cold","mild", "hot"])
add_clothing_to_wardrobe("umbrella", "grey", "umbrella", "sporty", ["rainy"], ["cold","mild", "hot"])
add_clothing_to_wardrobe("umbrella", "black", "umbrella", "casual", ["rainy"], ["cold","mild", "hot"])
add_clothing_to_wardrobe("umbrella", "white", "umbrella", "casual", ["rainy"], ["cold","mild", "hot"])
add_clothing_to_wardrobe("umbrella", "blue", "umbrella", "casual", ["rainy"], ["cold","mild", "hot"])
add_clothing_to_wardrobe("umbrella", "green", "umbrella", "casual", ["rainy"], ["cold","mild", "hot"])
add_clothing_to_wardrobe("umbrella", "grey", "umbrella", "casual", ["rainy"], ["cold","mild", "hot"])
add_clothing_to_wardrobe("umbrella", "black", "umbrella", "formal", ["rainy"], ["cold","mild", "hot"])
add_clothing_to_wardrobe("umbrella", "white", "umbrella", "formal", ["rainy"], ["cold","mild", "hot"])
add_clothing_to_wardrobe("umbrella", "blue", "umbrella", "formal", ["rainy"], ["cold","mild", "hot"])
add_clothing_to_wardrobe("umbrella", "green", "umbrella", "formal", ["rainy"], ["cold","mild", "hot"])
add_clothing_to_wardrobe("umbrella", "grey", "umbrella", "formal", ["rainy"], ["cold","mild", "hot"])


# In[15]:


#defining the function to generate the outfit
class outfit:
    
    
    #Initially define an outfit
    def __init__(self):
        #user inputs 
        
        location_verification = True
        while location_verification:

            try:
                location = input(f"Enter the location: ")

                days_ahead_verification = True
                while days_ahead_verification:
                    try:
                        days_ahead = int(input(f"In how many days do you plan on using the outfit? "))
                        if days_ahead in range(15):
                            days_ahead_verification = False
                        elif days_ahead < 0:
                            print("Oops! Unfortunately we can't change your past outfits (we wish!) Please input an integer between 0 and 14.")
                        elif days_ahead > 14:
                            print("Oops! Unfortunately we can't choose an outfit that much time in advance (I guess you can wait!) Please input an integer between 0 and 14.")
                    except:
                        print("Nice try but that is not an integer! Please input an integer between 0 and 14.")


                occasion_choice_verification = False
                while occasion_choice_verification == False:
                    occasion_choice = input("What is the type of outfit desired? press 0 for sporty, 1 for casual, 2 for formal ")
                    if occasion_choice == "0" or occasion_choice == "1" or occasion_choice == "2":
                        occasion_choice_verification = True
                    else:
                        print("Don't act like there are other choices! Please press 0 for sporty, 1 for casual, 2 for formal")


                #conversion of user occasion input into occasion to minimize typo mistakes
                if occasion_choice == "0":
                    occasion = "sporty"
                elif occasion_choice == "1":
                    occasion = "casual"
                elif occasion_choice == "2":
                    occasion = "formal"


                #API to get weather forecast
                request_weather = requests.get(f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?unitGroup=metric&key=SCGFH98U37K6Y7P2VNXSBJJX6&contentType=json")
                json = request_weather.json()
                date = json["days"][days_ahead]["datetime"]
                average_temp = json["days"][days_ahead]["temp"]
                condition = json["days"][days_ahead]["conditions"]
                rain = json["days"][days_ahead]["precip"]
                location_verification = False
            except:
                print("Oops looks like you are searching for a place that doesn't exist. Try again with a real location.")


        #converting celcius into temperature range for clothing
        if average_temp < 10:
            temperature = "cold"
        elif average_temp >= 10 and average_temp < 20:
            temperature = "mild"
        else:
            temperature = "hot"

        #converting condition into weather type for clothing
        if rain > 0.5:
            weather = "rainy"
        elif condition == "Clear":
            weather = "sunny"
        else:
            weather = "cloudy"


        #Segmenting the wardrobe into categories
        for item in wardrobe:
            if item.category == "sunglasses":
                list_of_sunglasses.append(item)
            elif item.category == "hat":
                list_of_hats.append(item)
            elif item.category == "umbrella":
                list_of_umbrellas.append(item)
            elif item.category == "top":
                list_of_tops.append(item)
            elif item.category == "outerwear":
                list_of_outerwear.append(item)
            elif item.category == "scarf":
                list_of_scarf.append(item)
            elif item.category == "bottom":
                list_of_bottoms.append(item)
            elif item.category == "shoes":
                list_of_shoes.append(item)

        #conditions for trying different colour schemes
        stop = False
        counter = 0

        #while to try other outfit combinations for different schemes
        while stop == False:

            #clean outfit for next iteration
            outfit = []
            #clean fit for next iteration
            list_of_sunglasses_fit = []
            sunglasses_in_use = ""
            list_of_hats_fit = []
            hat_in_use = ""
            list_of_scarf_fit = []
            scarf_in_use = ""
            list_of_umbrellas_fit = []
            umbrella_in_use = ""
            list_of_outerwear_fit = []
            outerwear_in_use = ""
            list_of_tops_fit = []
            top_in_use = ""
            list_of_bottoms_fit = []
            bottom_in_use = ""
            list_of_shoes_fit = []
            shoes_in_use = ""

            #choose random colour scheme
            colour_scheme_in_use = random.choice(schemes)


                #SUNNY SPECIFIC 

            #comments on this would be very similar for any clothing type
            if weather == "sunny": # check weather the forecasted eather is sunny
                for sunglasses in list_of_sunglasses: #iterate for every sunglasses
                    if sunglasses.occasion == occasion: #check if the sunglasses' occasion is the one inputed by user
                        for colour in colour_scheme_in_use: #iterate for every colour in the colour scheme
                            if colour == sunglasses.colour: #check whether the colour of the sunglasses is the same as the one in the colour scheme for the current iteration
                                for temp in sunglasses.temperature: #iterate for the different temperatures usable for the item
                                    if temp == temperature: #check whether the forecasted temperature is on the possible usable temperatures
                                        list_of_sunglasses_fit.append(sunglasses) #add to the number of sunglasses that could be used in this iteration

                for hat in list_of_hats:
                    if hat.occasion == occasion:
                        for colour in colour_scheme_in_use:
                            if colour == hat.colour:
                                for temp in hat.temperature:
                                    if temp == temperature:
                                        list_of_hats_fit.append(hat)



            #if there is at least one peice that fits within the category, choose a random piece that fits    
            if len(list_of_sunglasses_fit) > 0:
                    sunglasses_in_use=random.choice(list_of_sunglasses_fit)
                    outfit.append(sunglasses_in_use)
            if len(list_of_hats_fit) > 0:
                    hat_in_use=random.choice(list_of_hats_fit)
                    outfit.append(hat_in_use)



            #RAINY SPECIFIC

            if weather == "rainy":
                for umbrella in list_of_umbrellas:
                    if umbrella.occasion == occasion:
                        for colour in colour_scheme_in_use:
                            if colour == umbrella.colour:
                                for temp in umbrella.temperature:
                                    if temp == temperature:
                                        list_of_umbrellas_fit.append(umbrella)

            if len(list_of_umbrellas_fit) > 0:
                umbrella_in_use=random.choice(list_of_umbrellas_fit)
                outfit.append(umbrella_in_use) 



             #COLD SPECIFIC

            if temperature == "cold":
                for scarf in list_of_scarf:
                    if scarf.occasion == occasion:
                        for colour in colour_scheme_in_use:
                            if colour == scarf.colour:
                                for temp in scarf.temperature:
                                    if temp == temperature:
                                        list_of_scarf_fit.append(scarf)
            if len(list_of_scarf_fit) > 0:
                scarf_in_use=random.choice(list_of_scarf_fit)
                outfit.append(scarf_in_use)

             #OUTERWEAR
            for outerwear in list_of_outerwear:
                for climate in outerwear.weather:
                    if climate == weather:
                        if outerwear.occasion == occasion:
                            for colour in colour_scheme_in_use:
                                if colour == outerwear.colour:
                                    for temp in outerwear.temperature:
                                        if temp == temperature:
                                            list_of_outerwear_fit.append(outerwear)
            if len(list_of_outerwear_fit) > 0:
                outerwear_in_use = random.choice(list_of_outerwear_fit)
                outfit.append(outerwear_in_use)


            #Mandatory clothing

            #TOPS
            for top in list_of_tops:
                for climate in top.weather:
                    if climate == weather:
                        if top.occasion == occasion:
                            for temp in top.temperature:
                                if temp == temperature:
                                    for colour in colour_scheme_in_use:
                                        if colour == top.colour:
                                            list_of_tops_fit.append(top)

            if len(list_of_tops_fit) > 0:
                top_in_use=random.choice(list_of_tops_fit)
                outfit.append(top_in_use)

            #BOTTOMS       
            for bottom in list_of_bottoms:
                for climate in bottom.weather:
                    if climate == weather:
                        if bottom.occasion == occasion:
                            for colour in colour_scheme_in_use:
                                if colour == bottom.colour:
                                    for temp in bottom.temperature:
                                        if temp == temperature:
                                            list_of_bottoms_fit.append(bottom)

            if len(list_of_bottoms_fit) > 0:
                bottom_in_use = random.choice(list_of_bottoms_fit)
                outfit.append(bottom_in_use)

            #SHOES    
            for shoes in list_of_shoes:
                for climate in shoes.weather:
                    if climate == weather:
                        if shoes.occasion == occasion:
                            for colour in colour_scheme_in_use:
                                if colour == shoes.colour:
                                    for temp in shoes.temperature:
                                        if temp == temperature:
                                             list_of_shoes_fit.append(shoes)

            if len(list_of_shoes_fit) > 0:
                shoes_in_use = random.choice(list_of_shoes_fit)
                outfit.append(shoes_in_use)



            #Makes sure that all colours on the colour scheme are used
            colour_pass=[]
            for colour in colour_scheme_in_use: #iterates each colour in the colour scheme in use
                    colour_counter=0 #helpfull variable 
                    for item in outfit:
                        if item.colour == colour:
                            colour_counter += 1
                    if colour_counter > 0:
                        colour_pass.append("Y")
                    else:
                        colour_pass.append("N")
            colour_pass_verification=0

            for colour in colour_pass:
                if colour == "Y":
                    colour_pass_verification += 0
                else:
                    colour_pass_verification += 1

            counter += 1

            #conditions to exit while loop -> not go for another try
            if colour_pass_verification == 0 and temperature == "cold" and len(list_of_tops_fit) != 0 and len (list_of_bottoms_fit) != 0 and len(list_of_shoes_fit) != 0 and len(list_of_outerwear_fit) != 0:
                stop = True
            elif colour_pass_verification == 0 and temperature != "cold" and len(list_of_tops_fit) != 0 and len (list_of_bottoms_fit) != 0 and len(list_of_shoes_fit) != 0:
                stop = True
            elif counter > 1000:
                stop = True
                print("No combinations were found")

        print(f"According to our forecast for {date} in {location} it is going to be {weather} and {temperature}, with an average temperature of {average_temp}.")
        print(f"With this, and the fact that you want a {occasion} style, we created an outfit for you based on the colour scheme {colour_scheme_in_use} composed of:")

        if len(list_of_umbrellas_fit) != 0:
            print(f"A {umbrella_in_use.colour} {umbrella_in_use.name}")
        if len(list_of_sunglasses_fit) != 0:
            print(f"Some {sunglasses_in_use.colour} {sunglasses_in_use.name} sunglasses")
        if len(list_of_hats_fit) != 0:
            print(f"A {hat_in_use.colour} {hat_in_use.name}")
        if len(list_of_scarf_fit) != 0:
            print(f"A {scarf_in_use.colour} {scarf_in_use.name} scarf")
        if len(list_of_outerwear_fit) != 0:
            print(f"A {outerwear_in_use.colour} {outerwear_in_use.name}")
        if len(list_of_tops_fit) != 0:
            print(f"A {top_in_use.colour} {top_in_use.name}")
        if len(list_of_bottoms_fit) != 0:
            print(f"A pair of {bottom_in_use.colour} {bottom_in_use.name}")
        if len(list_of_shoes_fit) != 0:
            print(f"And {shoes_in_use.colour} {shoes_in_use.name}")

        
        self.outfit = outfit
        self.colour_scheme = colour_scheme_in_use
        self.date = date
        self.temperature = temperature
        self.weather = weather
        self.location = location
        self.occasion = occasion
        self.average_temp = average_temp
        self.sunglasses = sunglasses_in_use
        self.hat = hat_in_use
        self.scarf = scarf_in_use
        self.umbrella = umbrella_in_use
        self.outerwear = outerwear_in_use
        self.top = top_in_use
        self.bottom = bottom_in_use
        self.shoes = shoes_in_use
        
        
        

        
        
#Initially define an outfit
    def generate_new(self):
        
        date = self.date
        temperature = self.temperature
        weather = self.weather
        location = self.location
        occasion = self.occasion
        average_temp = self.average_temp
        
        
        #Segmenting the wardrobe into categories
        for item in wardrobe:
            if item.category == "sunglasses":
                list_of_sunglasses.append(item)
            elif item.category == "hat":
                list_of_hats.append(item)
            elif item.category == "umbrella":
                list_of_umbrellas.append(item)
            elif item.category == "top":
                list_of_tops.append(item)
            elif item.category == "outerwear":
                list_of_outerwear.append(item)
            elif item.category == "scarf":
                list_of_scarf.append(item)
            elif item.category == "bottom":
                list_of_bottoms.append(item)
            elif item.category == "shoes":
                list_of_shoes.append(item)

        #conditions for trying different colour schemes
        stop = False
        counter = 0

        #while to try other outfit combinations for different schemes
        while stop == False:

            #clean outfit for next iteration
            outfit = []
            #clean fit for next iteration
            list_of_sunglasses_fit = []
            sunglasses_in_use = ""
            list_of_hats_fit = []
            hat_in_use = ""
            list_of_scarf_fit = []
            scarf_in_use = ""
            list_of_umbrellas_fit = []
            umbrella_in_use = ""
            list_of_outerwear_fit = []
            outerwear_in_use = ""
            list_of_tops_fit = []
            top_in_use = ""
            list_of_bottoms_fit = []
            bottom_in_use = ""
            list_of_shoes_fit = []
            shoes_in_use = ""

            #choose random colour scheme
            colour_scheme_in_use = random.choice(schemes)


                #SUNNY SPECIFIC 

            #comments on this would be very similar for any clothing type
            if weather == "sunny": # check weather the forecasted eather is sunny
                for sunglasses in list_of_sunglasses: #iterate for every sunglasses
                    if sunglasses.occasion == occasion: #check if the sunglasses' occasion is the one inputed by user
                        for colour in colour_scheme_in_use: #iterate for every colour in the colour scheme
                            if colour == sunglasses.colour: #check whether the colour of the sunglasses is the same as the one in the colour scheme for the current iteration
                                for temp in sunglasses.temperature: #iterate for the different temperatures usable for the item
                                    if temp == temperature: #check whether the forecasted temperature is on the possible usable temperatures
                                        list_of_sunglasses_fit.append(sunglasses) #add to the number of sunglasses that could be used in this iteration

                for hat in list_of_hats:
                    if hat.occasion == occasion:
                        for colour in colour_scheme_in_use:
                            if colour == hat.colour:
                                for temp in hat.temperature:
                                    if temp == temperature:
                                        list_of_hats_fit.append(hat)



            #if there is at least one peice that fits within the category, choose a random piece that fits    
            if len(list_of_sunglasses_fit) > 0:
                    sunglasses_in_use=random.choice(list_of_sunglasses_fit)
                    outfit.append(sunglasses_in_use)
            if len(list_of_hats_fit) > 0:
                    hat_in_use=random.choice(list_of_hats_fit)
                    outfit.append(hat_in_use)



            #RAINY SPECIFIC

            if weather == "rainy":
                for umbrella in list_of_umbrellas:
                    if umbrella.occasion == occasion:
                        for colour in colour_scheme_in_use:
                            if colour == umbrella.colour:
                                for temp in umbrella.temperature:
                                    if temp == temperature:
                                        list_of_umbrellas_fit.append(umbrella)

            if len(list_of_umbrellas_fit) > 0:
                umbrella_in_use=random.choice(list_of_umbrellas_fit)
                outfit.append(umbrella_in_use) 



             #COLD SPECIFIC

            if temperature == "cold":
                for scarf in list_of_scarf:
                    if scarf.occasion == occasion:
                        for colour in colour_scheme_in_use:
                            if colour == scarf.colour:
                                for temp in scarf.temperature:
                                    if temp == temperature:
                                        list_of_scarf_fit.append(scarf)
            if len(list_of_scarf_fit) > 0:
                scarf_in_use=random.choice(list_of_scarf_fit)
                outfit.append(scarf_in_use)

             #OUTERWEAR
            for outerwear in list_of_outerwear:
                for climate in outerwear.weather:
                    if climate == weather:
                        if outerwear.occasion == occasion:
                            for colour in colour_scheme_in_use:
                                if colour == outerwear.colour:
                                    for temp in outerwear.temperature:
                                        if temp == temperature:
                                            list_of_outerwear_fit.append(outerwear)
            if len(list_of_outerwear_fit) > 0:
                outerwear_in_use = random.choice(list_of_outerwear_fit)
                outfit.append(outerwear_in_use)


            #Mandatory clothing

            #TOPS
            for top in list_of_tops:
                for climate in top.weather:
                    if climate == weather:
                        if top.occasion == occasion:
                            for temp in top.temperature:
                                if temp == temperature:
                                    for colour in colour_scheme_in_use:
                                        if colour == top.colour:
                                            list_of_tops_fit.append(top)

            if len(list_of_tops_fit) > 0:
                top_in_use=random.choice(list_of_tops_fit)
                outfit.append(top_in_use)

            #BOTTOMS       
            for bottom in list_of_bottoms:
                for climate in bottom.weather:
                    if climate == weather:
                        if bottom.occasion == occasion:
                            for colour in colour_scheme_in_use:
                                if colour == bottom.colour:
                                    for temp in bottom.temperature:
                                        if temp == temperature:
                                            list_of_bottoms_fit.append(bottom)

            if len(list_of_bottoms_fit) > 0:
                bottom_in_use = random.choice(list_of_bottoms_fit)
                outfit.append(bottom_in_use)

            #SHOES    
            for shoes in list_of_shoes:
                for climate in shoes.weather:
                    if climate == weather:
                        if shoes.occasion == occasion:
                            for colour in colour_scheme_in_use:
                                if colour == shoes.colour:
                                    for temp in shoes.temperature:
                                        if temp == temperature:
                                             list_of_shoes_fit.append(shoes)

            if len(list_of_shoes_fit) > 0:
                shoes_in_use = random.choice(list_of_shoes_fit)
                outfit.append(shoes_in_use)



            #Makes sure that all colours on the colour scheme are used
            colour_pass=[]
            for colour in colour_scheme_in_use: #iterates each colour in the colour scheme in use
                    colour_counter=0 #helpfull variable 
                    for item in outfit:
                        if item.colour == colour:
                            colour_counter += 1
                    if colour_counter > 0:
                        colour_pass.append("Y")
                    else:
                        colour_pass.append("N")
            colour_pass_verification=0

            for colour in colour_pass:
                if colour == "Y":
                    colour_pass_verification += 0
                else:
                    colour_pass_verification += 1

            counter += 1

            #conditions to exit while loop -> not go for another try
            if colour_pass_verification == 0 and temperature == "cold" and len(list_of_tops_fit) != 0 and len (list_of_bottoms_fit) != 0 and len(list_of_shoes_fit) != 0 and len(list_of_outerwear_fit) != 0:
                stop = True
            elif colour_pass_verification == 0 and temperature != "cold" and len(list_of_tops_fit) != 0 and len (list_of_bottoms_fit) != 0 and len(list_of_shoes_fit) != 0:
                stop = True
            elif counter > 1000:
                stop = True
                print("No combinations were found")

        print(f"We created a new outfit for you, that you can use on {date} in {location}. Hope you like it better!")
        print(f"We created an {occasion} outfit for you based on the colour scheme {colour_scheme_in_use} composed of:")

        
        if len(list_of_umbrellas_fit) != 0:
            print(f"A {umbrella_in_use.colour} {umbrella_in_use.name}")
        if len(list_of_sunglasses_fit) != 0:
            print(f"Some {sunglasses_in_use.colour} {sunglasses_in_use.name} sunglasses")
        if len(list_of_hats_fit) != 0:
            print(f"A {hat_in_use.colour} {hat_in_use.name}")
        if len(list_of_scarf_fit) != 0:
            print(f"A {scarf_in_use.colour} {scarf_in_use.name} scarf")
        if len(list_of_outerwear_fit) != 0:
            print(f"A {outerwear_in_use.colour} {outerwear_in_use.name}")
        if len(list_of_tops_fit) != 0:
            print(f"A {top_in_use.colour} {top_in_use.name}")
        if len(list_of_bottoms_fit) != 0:
            print(f"A pair of {bottom_in_use.colour} {bottom_in_use.name}")
        if len(list_of_shoes_fit) != 0:
            print(f"And {shoes_in_use.colour} {shoes_in_use.name}")
        
        self.outfit = outfit
        self.colour_scheme = colour_scheme_in_use
        self.date = date
        self.temperature = temperature
        self.weather = weather
        self.location = location
        self.occasion = occasion
        self.average_temp = average_temp
        self.sunglasses = sunglasses_in_use
        self.hat = hat_in_use
        self.scarf = scarf_in_use
        self.umbrella = umbrella_in_use
        self.outerwear = outerwear_in_use
        self.top = top_in_use
        self.bottom = bottom_in_use
        self.shoes = shoes_in_use
        
        
        
    def change_piece(self):
        
        outfit_constituents = []
        
        #user chooses piece to change
        piece_change_verification = False
        while piece_change_verification == False:
            piece_change = input("Which piece would you like to change? Possible categories are sunglasses, hat, scarf, umbrella, outerwear, top, bottom or shoes\n")
            for piece in self.outfit:
                if piece_change == piece.category:
                    piece_change_verification = True
            
            if piece_change_verification == False:
                print("That category doesn't exist or isn't appropriate for these weather conditions. Please try again.")
        
        
        #set the constituents of the current outfit
        for piece in self.outfit:
            outfit_constituents.append(piece.category)
        

        #which index is the pience meant to be changed in the list of the outfit 
        index_piece = outfit_constituents.index(piece_change)
        
        
        #save the substituted piece to make sure it is not placed back in
        substituted_piece = self.outfit[index_piece]
        
        #take out the piece to be changed
        self.outfit.pop(index_piece)
        
        
         #conditions for trying different colour schemes
        stop = False
        counter = 0

        #while to try other outfit combinations for different schemes
        while stop == False:
        
            list_of_substitutes_fit = []
            substitute_in_use =""




            for piece in wardrobe:
                if piece.category == piece_change:
                    for climate in piece.weather:
                        if climate == self.weather:
                            if self.occasion == piece.occasion:
                                for colour in self.colour_scheme:
                                    if colour == piece.colour:
                                        for temp in piece.temperature:
                                            if temp == self.temperature:
                                                if piece != substituted_piece:
                                                    list_of_substitutes_fit.append(piece)

                    
                    
            if len(list_of_substitutes_fit) > 0:
                substitute_in_use = random.choice(list_of_substitutes_fit)
                self.outfit.insert(index_piece, substitute_in_use)





            #Makes sure that all colours on the colour scheme are used
            colour_pass=[]
            for colour in self.colour_scheme: #iterates each colour in the colour scheme in use
                    colour_counter=0 #helpfull variable 
                    for item in self.outfit:
                        if item.colour == colour:
                            colour_counter += 1
                    if colour_counter > 0:
                        colour_pass.append("Y")
                    else:
                        colour_pass.append("N")
                            
            colour_pass_verification=0

            for colour in colour_pass:
                if colour == "Y":
                    colour_pass_verification += 0
                else:
                    colour_pass_verification += 1

            counter += 1
            
            

            #conditions to exit while loop -> not go for another try
            if colour_pass_verification == 0 and len(list_of_substitutes_fit) > 0:
                stop = True  
            elif counter > 50:
                stop = True
                print("No combinations were found for this colour scheme.")
            elif colour_pass_verification != 0 and len(list_of_substitutes_fit) >0:
                self.outfit.pop(index_piece) #takes back the previously added item as it does not adhere to all conditions
        
        
        
        
        if counter <= 50:
            print(f"We created a new outfit for you, that you can use on {self.date} in {self.location}. Hope you like it better!")
            print(f"We created an {self.occasion} outfit for you based on the colour scheme {self.colour_scheme} composed of:")      




            for piece in self.outfit:
                if piece.category == "sunglasses":
                    print(f"Some {piece.colour} {piece.name} sunglasses") 
                elif piece.category == "bottom":
                    print(f"A pair of {piece.colour} {piece.name}")
                elif piece.category == "shoes":
                    print(f"And {piece.colour} {piece.name}")
                elif piece.category == "scarf":
                    print(f"A {piece.colour} {piece.name} scarf")
                else:
                    print(f"A {piece.colour} {piece.name}")


# In[16]:


outfit1 = outfit()

like_outfit_verification = False
while like_outfit_verification == False:
    like_outfit = input("Do you like your outfit? (Y/N)")
    if like_outfit == "Y":
        print("Perfect, I made it especially for you!")
        like_outfit_verification = True
    elif like_outfit == "N":
        like_outfit_verification = True
        change_outfit_verification = False
        while change_outfit_verification == False:       
            change_outfit = input("Thats a shame! To generate a new outfit press 1, to change a specific piece in the outfit press 0. ")
            if change_outfit == "1":
                outfit1.generate_new()
                change_outfit_verification = True
            elif change_outfit == "0":
                outfit1.change_piece()
                change_outfit_verification = True
            else:
                print("Wrong input. Please try again") 
    else:
        print("Wrong input. Please try again")

print("Thank you for bearing with me. Feel free to ask for help whenever you want more outfits!")


# HSG Introduction to Programming Spring 2023 - Carlota Ferreira 22-625-537, Carolina Quinaz 22-625-511
