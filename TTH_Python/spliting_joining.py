flavors = ["vanilla", "strawberry"]
", ".join(flavors)
return flavors

"My favorite flavors favorite:" + ", ".join(flavors)
#only can use join for strings
"my favorite flavors are: {}"".format(", ".join(flavors))


available = "Banana split;hot fudge;cherry;malted;black and white"
sundaes = available.split(";")
display_menu = ",".join(sundaes)
menu = "our available flavors are: {}.".format(display_menu)
