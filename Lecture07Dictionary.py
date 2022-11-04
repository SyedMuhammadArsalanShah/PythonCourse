

# a = {

#     "daniyal": "2001",
#     "age": "123",
#     "hobies": ["playing", "Reading"],
#     "other":{"kashif":"faris", "number":"022"},
#       12: "maaz"

# }




# print(a['age'])
# print(a['other']['number'])
# print(a['other']['kashif'])




# methods of dictionaries;


# print(a.keys())
# print(a.values())
# print(a.items())
# b={"color":"red", "num":"07"}
# print(a.update(b))

# print(a)

# print(a["other"])
# print(a.get("other"))



# print(a["others"])
# print(a.get("others"))


words={
"saniha":"accident",
"kitab":"book",
"qalam":"pen"
}
print("check your words ", list(words.keys()))

search=input("enter your word ")


# print(words[search]) #its throw an error while key not there


print(words.get(search))






