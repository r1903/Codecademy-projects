#pokemon class
class Pokemon:
    def __init__(self,name,level,type):
        self.name = name
        self.level = level
        self.type = type
        self.max_health = level
        self.health = level
        self.knockout_status = False
        self.exp = 0

#method for loosing health
    def lose_health(self,damage):
        self.health-=damage
        if self.health <= 0:
            self.health = 0
            print("{name} now has 0 health.".format(name = self.name))
            self.knock_out()
        else:
            print("{name} now has {health} health.".format(name = self.name, health = self.health))   

 #method for setting knockout status to True
    def knock_out(self):
        self.knockout_status = True
        print("{name} was knocked out!".format(name = self.name))

#method for setting knockout status to False
    def revive(self):
        self.knockout_status = False
        print("{name} was revived!".format(name = self.name))

#method for health gain
    def gain_health(self,gain):
        self.revive()
        self.health += gain
        if self.health > self.max_health:
            self.health = self.max_health
            print("{name} has {health} health after gaining health".format(name = self.name, health = self.health))

#method for pokemon attack
    def attack(self,other_pokemon):
        if self.knockout_status:
            print("{name} is knocked out! so it can not attack".format(name = self.name))
            return
        if (self.type == "Fire" and other_pokemon.type == "Water") or (self.type == "Water" and other_pokemon.type == "Grass") or (self.type == "Grass" and other_pokemon.type == "Fire"):
            damage = self.level * 0.5
            print("{self} attacked {other_pokemen} for {damage} damage.".format(self = self.name, other_pokemen = other_pokemen.name,damage = damage))
            other_pokemon.lose_health(damage)
        if (self.type == other_pokemon.type):
            damage = self.level 
            print("{self} attacked {other_pokemen} for {damage} damage.".format(self = self.name, other_pokemen = other_pokemon.name, damage = damage))
            other_pokemon.lose_health(damage)
        if (self.type == "Fire" and other_pokemon.type == "Grass") or (self.type == "Water" and other_pokemon.type == "Fire") or (self.type == "Grass" and other_pokemon.type == "Water"):
            damage = self.level * 2
            print("{my_name} attacked {other_name} for {damage} damage.".format(my_name = self.name, other_name = other_pokemon.name, damage = damage))
            other_pokemon.lose_health(damage)   
        self.gain_exp()


#method to increase exp value after each attack
    def gain_exp(self):
        self.exp += 1
        print("{name} gained {exp} experience".format(name=self.name,exp=self.exp))
        if self.exp >= 2:
            self.level_up()


#method to level up pokemon if exp vaue reached to 2
    def level_up(self):
        self.exp = 0
        self.level += 1
        self.health +=self.health
        print("{name} is leveled up by {level}, health now is {health}.".format(name=self.name, level=self.level, health=self.max_health))
        
  


#Trainer class
class Trainer:
    def __init__(self,name,potions,pokemons):
        self.name = name
        self.potions = potions
        self.pokemons = pokemons
        self.current_pokemon = 0

#method for attacking other trainer pokemon
    def attack_other_trainer(self,other_trainer):
        their_pokemon = other_trainer.pokemons[other_trainer.current_pokemon]
        my_pokemon = self.pokemons[self.current_pokemon]
        my_pokemon.attack(their_pokemon)
     
#method for poistion to improve pokemon health
    def position_use(self):
        if self.potions > 0:
            self.pokemons[self.current_pokemon].gain_health(1)
            self.potions-=1
            print("Potion is used on {name} and now {potions} potions are left with trainer {trainername}.".format(name = self.pokemons[self.current_pokemon].name,potions = self.potions,trainername=self.name))
        else:
             print("There is no potion left to use on {name} with trainer {trainername}.".format(name = self.pokemons[self.current_pokemon].name,trainername=self.name))

#method for switching active pokemon 
    def switch_pokemon(self,new_pokemon):
        if new_pokemon < len(self.pokemons) and new_pokemon >= 0:
            if self.pokemons[new_pokemon].knockout_status:
                print("{current} is knocked out.so we can not make it active".format(current = self.current_pokemon))
            else:
                self.current_pokemon = new_pokemon
                print("{current} is new active pokemon".format(current = self.current_pokemon))  
        else:
            print("{current} is not in the range so cannot change the active pokemon".format(current = new_pokemon))



pikachu = Pokemon("Pikachu", 3, "Fire")
mute = Pokemon("Mute", 5, "Water")
eve = Pokemon("Eve", 5, "Fire")
pokemon1 = Pokemon("abc", 5, "Grass")
pokemon2 = Pokemon("mno", 7, "Grass")


# Charmander is inheriting pokemon class
class Charmander (Pokemon):
    def __init__(self, name, level, type, stat):
        super().__init__(name, level, type)
        self.stat = stat

#pokemon3 with Charmander class
pokemon3 = Charmander("xyz",6,"Water","xyz")


trainer1 = Trainer("ABC", 5, [pikachu,mute,pokemon1,pokemon2,pokemon3])
trainer2 = Trainer("XYZ", 1, [eve,pokemon1,pokemon2])

#testing
trainer1.attack_other_trainer(trainer2)
trainer2.attack_other_trainer(trainer1)
trainer2.position_use()
trainer1.switch_pokemon(2)
trainer1.switch_pokemon(5)
trainer1.position_use()
trainer1.switch_pokemon(4)
trainer1.attack_other_trainer(trainer2)