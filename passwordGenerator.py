import random
def ask_questions():
    alpha_num = [1,2,3,4,5,6,7,8,9,0,'q','w','e','r','t','y','u','i','o','i','o',\
             'p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n',\
             'm']
    length = input("Length of password? \n")
    password = ''
    i = 0
    while i < length:
        temp = random.choice(alpha_num)
        if random.random() > 0.5 and type(temp) == str:
            temp = temp.upper()      
        password += str(temp)
        i+=1
    print password       
if __name__ == "__main__":
    while True:
        ask_questions()