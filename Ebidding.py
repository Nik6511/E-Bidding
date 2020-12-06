import random
class Bidding():
    # def __init__(self):
    #     inp=input('''
    #     Choose your option to BID
    #     1. Property
    #     2. Paintings
    #     3. Vintage Cars
    #     ''')
    #     if inp==1:
    #         inp1=input('''
    #     Choose your option:
    #     1. T - 404 Victory Amara Noida Extension
    #     2. 2101-Tower D, 3BHK Apartment
    #     3. Florence Estate
    #     ''')
            

    #     if inp==2:
    #         inp=input('''
    #     Choose your option:
    #     1. William Quigley Untitled, Black..., 1985 
    #         Starting Bid:5,000 USD 
    #     2. Damien Hirst Grace (H6-2), 2019
    #         Starting Bid:9,500 USD (6 Bids)
    #     3. Julie Mehretu Fracture, 2007
    #         Starting Bid:4,000—6,000 USD
    #     ''')
    #     if inp==3:
    #         inp=input('''
    #     Choose your option:
    #     1. Ford Model T (1908) 
    #         Starting Bid:5,000 USD 
    #     2. Rolls-Royce Phantom (1925)
    #         Starting Bid:9,500 USD (6 Bids)
    #     3. Alfa Romeo 8C (1938)
    #         Starting Bid:4,000—6,000 USD
    #     ''')
    def __init__(self):
        D1={1:"Property",
            2:"Paintings",
            3:"Vintage Cars"}
        print("Choose your Option to BID:-")
        print(f"1. {D1[1]}\n2. {D1[2]}\n3. {D1[3]}")
        inp=int(input())
        if inp==1:
          P1={1:"T - 404 Victory Amara Noida Extension",
              2:"2101-Tower D, 3BHK Apartment",
              3:"Florence Estate"}
          print(f"\nChoose the {D1[inp]}:-")
          print(f"1. {P1[1]}\n2. {P1[2]}\n3. {P1[3]}\n")
          inp1=int(input())
          
          print(f"\nYou are Bidding for [{P1[inp1]}]")
          print("The starting BID is: 5,000 USD")
          self.Bidding(5000,D1[inp],P1[inp1])
        
        elif inp==2:
          P1={1:"William Quigley Untitled, Black..., 1985", 
              2:"Damien Hirst Grace (H6-2), 2019",
              3:"Julie Mehretu Fracture, 2007"}
            
          print(f"\nChoose the {D1[inp]}:-")
          print(f"1. {P1[1]}\n2. {P1[2]}\n3. {P1[3]}")
          inp1=int(input())
          print(f"\nYou are Bidding for [{P1[inp1]}]")
          print("The starting BID is: 5,000 USD")
          self.Bidding(2000,D1[inp],P1[inp1])
        
        elif inp==3:
          P1={1:"Ford Model T (1908)" ,
              2:"Rolls-Royce Phantom (1925)",
              3:"Alfa Romeo 8C (1938)"}
            
          print(f"\nChoose the {D1[inp]}:-")
          print(f"1. {P1[1]}\n2. {P1[2]}\n3. {P1[3]}")
          inp1=int(input())
          print("\n\n----------NOTE----------")
          print(f"\nYou are Bidding for [{P1[inp1]}]")
          print("The starting BID is: 5,000 USD")
          self.Bidding(7000,D1[inp],P1[inp1])
        



          
        

        
    def Bidding(self,m,item,item1):
        print("Total number of Bidders: 5")
        # b1=random.randint(n,n*3)
        # b2=random.randint(n,n*3)
        # b3=random.randint(n,n*3)
        # b4=random.randint(n,n*3)
        # b5=random.randint(n,n*3)
        # n=1
        # l=[]
        # b6=int(input("Place your BID: \n"))
        # l.append(b6)
        # while n!=5:
        #     b=random.randint(m,m*3)
        #     l.append(b)
        #     print(f"{n}st Bidder's BID: {b}\n")
        #     n+=1
        n=1
        l={}
        b6=int(input("Place your BID: "))
        l['You']=b6
        print("\n\n----------BIDDIND DETAILS---------- ")
        while n<=5:
            b=random.randint(m,m*3)
            if n==1:
                l['First']=b
                print(f"\nFirst Bidder's BID: {b} USD\n")
            if n==2:
                l['Second']=b
                print(f"Second Bidder's BID: {b} USD\n")
            if n==3:
                l['Third']=b
                print(f"Third Bidder's BID: {b} USD\n")
            if n==4:
                l['Fourth']=b
                print(f"Fourth Bidder's BID: {b} USD\n")
            if n==5:
                l['Fifth']=b
                print(f"Fifth Bidder's BID: {b} USD\n")
            n+=1

        
        
        print(f"Your BID is {b6} USD\n")
        print("------------------------------------------------\n")
        print(f"The winning BID is {max(l.values())} USD\n")
        index=max(l,key=l.get)
        if b6==max(l.values()):
            print(f"The {item}: [{item1}]\nSold to [{index}]\nWith the highest BID of: {max(l.values())} USD\n")
        else:
            print(f"The {item}: [{item1}]\nSold to the: [{index} Bidder]\nWith the highest BID of: {max(l.values())} USD\n")
        print("------------------------------------------------\n")
        
        # print(f"First Bidder's BID: {b1}\nSecond Bidder's BID: {b2}\n Third Bidder's BID: {b3}\n Fourth Bidder's BID: {b4}\n Fifth Bidder's BID: {b5}\n")

class User():
    print()
    def __init__(self):
        print("Welcome to E.bidding Portal.")
        ans=int(input('''
To Log In,      Enter 1
To Sign Up,     Enter 2 
                 '''))
        if ans==1:
            self.login()
        elif ans==2:
            self.signup()
        else:
            print("You've entered invalid input\n")
    def login(self):
        userid=input("Enter a userid\n")
        password=input("Enter your password\n")
        self.validation(userid,password)

    def signup(self):
        name=input("Enter your name\n")
        age=int(input("Enter your age\n"))
        gender=input("Enter your gender\n")
        profession=input("Enter your profession\n")
        userid=input("Enter a userid\n")
        password=input("Choose your password\n")
        password1=input("Confirm your password\n")
        while password!=password1:
            print("Password did not match! Try again!!!\n")
            password=input("Choose your password\n")
            password1=input("Confirm your password\n")
        self.insert(userid,password,name,age,gender,profession)
        
        print(f"\n----------Signed In as {userid}----------\n")
        B=Bidding()
        
    
    def validation(self,userid,password):
        with open('EDatabse.txt','r') as f:
            content=True
            while content:
                content=f.readline()
                print(content)
                if userid and password in content:
                    print(f"----------Logged In! as {userid}----------\n")
                    B=Bidding()
                    exit()

            if content!=True:
                print("User not found! Try again\n")
                self.login()

        
    def insert(self,userid,password,name,age,gender,profession):
        with open('EDatabse.txt','a') as f:
            b=f.write(f"{userid} {password} {name} {age} {gender} {profession}\n")


A=User()
