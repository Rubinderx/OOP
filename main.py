from person import Person

person = Person("Robin", 25, "Medium")

# print(f"Hi, I'm {person.name}, I'm {person.age} years old and I'm a {person.height} build.")

from hero import Superhero

flash = Superhero("The Flash", "Barry Allen", "super speed", "Reverse Flash")
batman = Superhero("Batman", "Bruce Wayne", "wealth, intellect, and training", "The Joker")#
superman = Superhero("Superman", "Clake Kent", "super strengh, flight, and heat vision", "Lex Luthor")
ww = Superhero("Wonder Woman", "Diana of Themyscia", "superhuman strength, agility, and divine weapons", "Ares")


print(f"I’m {flash.name}, the fastest man alive—but my real name is {flash.identity}, and I use my {flash.power} to fight crime and protect my city, including from my greatest enemy, {flash.enemy}.")
print(f"I'm {batman.name}, the Dark Knight of Gotham City—but behind the mask, I’m {batman.identity}, using my {batman.power} to fight crime and face off against my greatest nemesis, {batman.enemy}.")
print(f"I'm {superman.name}, the protector of Earth—but my true identity is {superman.identity}, a reporter from Metropolis, and I use my incredible powers, like {superman.power}, to defend the world from villains like my greatest enemy, {superman.enemy}.")
print(f"I’m {ww.name}, a warrior and protector of peace—but among the Justice League, I’m also known as {ww.identity}, an Amazon princess who uses my {ww.power} to defend the world from threats like my nemesis, {ww.enemy}.")
