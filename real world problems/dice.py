import random
player1=input()
player2=input()

value1=random.randint(1,6)
value2=random.randint(1,6)

print("Player1 got",value1)
print("Player2 got",value2)

if value1>value2:
    print("Player1 wins")
elif value1<value2:
    print("Player2 wins")
else:
    print("It is a draw")
