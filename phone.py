import json

class Phone:

    def __init__(self,name,model):
        self.name = name
        self.model = model
        self.active = True
        self.on = True
        self.cam_app = True
        self.msg = True
        self.ring = True
        self.img = True

    def diaplay_name(self):
        print(f"Phone name: {self.name} ")
        print(f"Phone model: {self.model}")

    def lock_unlock(self):
        
        while self.active:
                print( "Your phone is on now.")
                user  = int(input("\nEnter your password: "))
                if user == 2026 :
                    print(f"Your password : {user}")
                    
                    self.active = False
                    break
                else:
                    print("-----Invalid Password------")
                    # self.active = False
                    break
        else:        
            print("Your phone is off now")
            self.active = True

            
    def Brightness_level(self):
        number = int(input("Enter your brightness here: "))
        if number <= 100:
            print(f"\nBrightness : {number}")
    
    def data_on_or_off(self):
        while self.on:
            print("Your data is On....")
            self.on = False
            break
        else:
            print("Your data is Off....")
            self.on = True
            

    def camera(self):
        while self.cam_app:
            print("Your camera is open now.")
            self.cam_app = False
            break
        else:
            print("Your camera is off now.")
            self.cam_app = True

    def messanger(self):
    
        while self.msg:
            print("You can send your msg now.")
            print(input("Enter your msg: "))
            self.msg = False
            break
        else:
            print("Messanger is off now. ") 
            self.msg = True

    
    def call_person(self,filename = 'contacts.json'):
        while self.ring:
            print("Call is open\n")
            try:
                with open(filename) as f:
                    file = json.load(f)
                    print(file)
                    while True:
                            user = input("\nTo whom you want to call(enter your no. ) or else enter 'q': ")
                            if user == 'q':
                                break
                            else:
                                user = int(user)
                                if user != file[user]:
                                    print(f"Calling {file[user]}")

            except FileNotFoundError:
                print("No contacts are available. Please add contacts first.")
                break
                
            self.ring = False
            break
        
                    
        else:
            print("call is off.")
            self.ring = True


    def gallery(self,filename = 'gallery_store.json'):
        while self.img:
            print("your gallery is open now.\n")
            try:
                with open(filename) as f:
                    file = json.load(f)
                    print(file)
                    while True:
                        user = input("\nwhich imag you want to open (enter no.) or else enter 'q': ")
                        if user == 'q':
                            break
                        else:
                            user = int(user)
                            if user != file[user]:
                                print(f"{file[user]} is Opend !")
   
            except FileNotFoundError:
                print("No gallery file is available. Please add images first.")
                break
               
            self.img = False
            break
        else:
            print("Your gallery is off now.")
            self.img = True


phone = Phone(' Samsung Galaxy S25 5G','SM-S931B/Ds')

phone.diaplay_name()

print("""
        1 = Lock and Unlock
        2 = Brightness
        3 = Data on or off
        4 = Camera
        5 = Messanger
        6 = Call
        7 = Gallery
          """)
while True :
    
    enter = int(input("\nEnter one number between (1 to 6 ): "))
    
    
    if enter == 1:
        phone.lock_unlock()
        user = input("If you want to continue print yes otherwise 'quit' : ")
        if user == 'quit':
            break
        
            
    elif enter == 2:
        phone.Brightness_level()
        user = input("If you want to continue print yes otherwise 'quit' : ")
        if user == 'quit':
            break
        

    elif enter == 3:
        phone.data_on_or_off()
        user = input("If you want to continue print yes otherwise 'quit' : ")
        if user == 'quit':
            break
        

    elif enter == 4:
        if phone.msg == False:
            print("First Close Messanger .")
        
        elif phone.ring == False:
            print("First Close Call.")

        elif phone.img == False:
            print("First close your gallery.")
        
        else:
            phone.camera()
      
        user = input("If you want to continue print yes otherwise 'quit' : ")
        if user == 'quit':
            break
        

    elif enter == 5:
        if phone.cam_app == False:
            print("First Close Camera.")
        
        elif phone.ring == False:
            print("First Close Call.")

        elif phone.img == False:
            print("First close your gallery.")

        else:
            phone.messanger()
        user = input("If you want to continue print yes otherwise 'quit' : ")
        if user == 'quit':
            break
        
   

    elif enter == 6:
        if phone.cam_app == False:
            print("First Close Camera.")

        elif phone.msg == False:
            print("First Close Messanger .")

        elif phone.img == False:
            print("First close your gallery.")

        else:
            phone.call_person()

        user = input("If you want to continue print yes otherwise 'quit' : ")
        if user == 'quit':
            break
    
    elif enter == 7:
       
        if phone.cam_app == False:
            print("First Close Camera.")

        elif phone.msg == False:
            print("First Close Messanger .")

        elif phone.ring == False:
            print("First close your call app.")
        else:
            phone.gallery()

        user = input("If you want to continue print yes otherwise 'quit' : ")
        if user == 'quit':
            break
