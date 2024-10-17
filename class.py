import random

class Warrior:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other_warrior):
        # Véletlenszerű sebzés a támadási erő +/- 2 tartományában
        damage = random.randint(self.attack_power - 2, self.attack_power + 2)
        other_warrior.health -= damage
        print(f"{self.name} támadja {other_warrior.name}-t, sebzés: {damage}")

    def is_alive(self):
        return self.health > 0

    def special_ability(self):
        # Véletlenszerű aktiválás (25% eséllyel)
        if random.random() < 0.25:
            # Kritikus sebzés: duplázza a támadási erőt
            print(f"{self.name} aktiválja a speciális képességét!")
            return self.attack_power * 2
        return self.attack_power


def battle(warrior1, warrior2):
    round_count = 0

    while warrior1.is_alive() and warrior2.is_alive():
        round_count += 1
        print(f"\n--- {round_count}. kör ---")
        
        try:
            # Warrior 1 támad
            damage = warrior1.special_ability()
            warrior1.attack(warrior2)
            print(f"{warrior2.name} életereje: {warrior2.health}")

            if not warrior2.is_alive():
                print(f"{warrior2.name} legyőzve! {warrior1.name} nyert!")
                break

            # Warrior 2 támad
            damage = warrior2.special_ability()
            warrior2.attack(warrior1)
            print(f"{warrior1.name} életereje: {warrior1.health}")

            if not warrior1.is_alive():
                print(f"{warrior1.name} legyőzve! {warrior2.name} nyert!")
                break

        except Exception as e:
            print(f"Hiba történt: {e}")


if __name__ == "__main__":
    warrior1 = Warrior("Harcos1", 100, 10)
    warrior2 = Warrior("Harcos2", 100, 10)
    
    battle(warrior1, warrior2)

        
    
        

        
