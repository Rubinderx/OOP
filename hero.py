class Superhero():
    def __init__(hero, super_name, super_identity, super_power, super_enemy):
        hero.name = super_name
        hero.identity = super_identity
        hero.power = super_power
        hero.enemy = super_enemy
    
    def introduce(hero):
        print(f"I’m {hero.name}, also known as {hero.identity}, and I use my {hero.power} to protect the world, often facing off against my greatest enemy, {hero.enemy}.")
    
    def transform(hero):
        print(f"{hero.identity} has transformed into {hero.name}!")

    def set_lair(hero, lair_name):
        hero.lair = lair_name
        print(f"{hero.name} has a secret lair called {hero.lair}.")

flash = Superhero("The Flash", "Barry Allen", "super speed", "Reverse Flash")
batman = Superhero("Batman", "Bruce Wayne", "wealth, intellect, and training", "The Joker")
superman = Superhero("Superman", "Clake Kent", "super strengh, flight, and heat vision", "Lex Luthor")
ww = Superhero("Wonder Woman", "Diana of Themyscia", "superhuman strength, agility, and divine weapons", "Ares")

# flash.set_lair("S.T.A.R. Labs")
# batman.set_lair("The Batcave")
# superman.set_lair("The Fortress of Solitude")
# ww.set_lair("Themyscira")
