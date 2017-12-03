3)#Program that accepts name as argument and prints happy birtday song

def happy_birthday(name):
    print("Happy Birthday to You\nHappy Birthday, Happy Birthday\nHappy Birthday to You {:s}!!".format(name))
    print("\n\nMay God Bless Yoy\nMay God bless you\nHope your wishes all come true\nHappy Bithday to you")


friend_name = str(input('Enter your friend name : '))
print("\n\n")
happy_birthday(friend_name)

