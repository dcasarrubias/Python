"""
def add_numbers(*args):
    total = 0
    for a in args:
        total += a
        print(total)

add_numbers(3,15,16,18)    
"""
"""
def health_calculator(age, apples_ate, cigs_smoked):
    answer = (100 - age) + (apples_ate * 3.5) - (cigs_smoked * 2)
    print(answer)

davids_data = [19,0.1,0]

health_calculator(*davids_data)
"""
"""
class Enemy:
    life = 3

    def attack(david):
        print('ouch!')
        david.life -= 1

    def checkLife(david):
        if(david.life <= 0):
            print('I am dead')
        else:
            print(str(david.life) + " life left")

            
enemy1 = Enemy()
enemy1.attack()
enemy1.checkLife()
"""
