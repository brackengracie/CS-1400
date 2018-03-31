scores = [90, 89, 78, 87, 98, 95, 72, 62]
people = ["Allen", "Bob", "Cindy", "David", "Evan", "Frank", "Gina","Mark"]
print(scores[0]) # 90
print(people[4]) # Evan
print(people[len(people)-1])
for i in range(len(scores)):
    print(people[i], "received a ", scores[i], "percent.")
total = 0
for i in range(len(scores)):
    total = total + scores[i]

songs = []
songs.append("Happy")
songs.append("Hello")
songs.append("Sugar")
print(len(songs))
print(songs[1]) # Hello
