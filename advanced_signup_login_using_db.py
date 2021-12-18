import pymongo

if __name__ == "__main__":
    print("Welcome to Pratik's Application\n")
    print("1. Sign up to Application\n")
    print("2. Login to Application\n")
    print("3. Update Email Address\n")
    print("4. Update Password\n")
    print("5. Update Username\n")
    print("6. Exit\n")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["PratikKaDatabase"] #Created a Databased named "Pratik's Database""'
    collection = db["PratikKaCollection"] #CREATED A COLLECTION NAMED "Pratik's Collection'"
    # dictt = {"name" : "Pratik" , "marks" : 69}
    # collection.insert_one(dictt)
    # print(f"added {dictt}")

    # print(collection.find_one({"name" : "Pratik"}))
    while True:
        inp = int(input("Enter your choice: \n"))
        if inp == 1:
            SignUpUsername = input("Enter your name: \n")
            SignUpemail = input("Enter your email: \n")
            SignUpPassword = input("Enter your password: \n")
            if SignUpUsername == "" or SignUpemail == "" or SignUpPassword == "":
                print("Please enter all the fields")
            CheckIfUsernameExists = collection.find_one({"username" : SignUpUsername})
            CheckIfEmailExists = collection.find_one({"email" : SignUpemail})
            if CheckIfUsernameExists == None and CheckIfEmailExists == None:
                collection.insert_one({"username" : SignUpUsername , "email" : SignUpemail , "password" : SignUpPassword})
                print("Account created successfully")
            else:
                print("Username or Email already exists")
        elif inp == 2:
            LoginUsername = input("Enter your username: \n")
            LoginPassword = input("Enter your password: \n")
            if LoginUsername == "" or LoginPassword == "":
                print("Please enter all the fields")
            CheckIfUsernameExists = collection.find_one({"username" : LoginUsername})
            if CheckIfUsernameExists == None:
                print("Username does not exist")
            else:
                if LoginPassword == CheckIfUsernameExists["password"]:
                    print("Login Successful")
                else:
                    print("Incorrect Password")

        elif inp == 3:
            UpdateEmailUsername = input("Enter your username: \n")
            CheckIfUsernameExists = collection.find_one({"username" : UpdateEmailUsername})
            if CheckIfUsernameExists == None:
                print("Username does not exist")
            PasswordForUpdate = input("Enter your password: \n")
            if PasswordForUpdate == UpdateEmailUsername["password"]:
                UpdateEmail = input("Enter your new email: \n")
                print("Please enter all the fields")
                
                if CheckIfUsernameExists == None:
                    print("Username does not exist")
                    exit()
                else:
                    collection.update_one({"username" : UpdateEmailUsername} , {"$set" : {"email" : UpdateEmail}})
                    print("Email updated successfully")
            elif PasswordForUpdate != UpdateEmailUsername["password"]:
                print("Incorrect Password")
                exit()
        elif inp == 4:
            UpdatePasswordUsername = input("Enter your username: \n")
            CheckIfUsernameExists = collection.find_one({"username" : UpdatePasswordUsername})
            if CheckIfUsernameExists == None:
                print("Username does not exist")
            PasswordForUpdate = input("Enter your password: \n")
            if PasswordForUpdate == CheckIfUsernameExists["password"]:
                NewPassword = input("Enter your new password: \n")
                collection.update_one({"username" : UpdatePasswordUsername} , {"$set" : {"password" : NewPassword}})
                print("Password updated successfully")
            elif PasswordForUpdate != CheckIfUsernameExists["password"]:
                print("Incorrect Password")

        elif inp == 5:
            UpdateUsernameUsername = input("Enter your username: \n")
            CheckIfUsernameExists = collection.find_one({"username" : UpdateUsernameUsername})
            if CheckIfUsernameExists == None:
                print("Username does not exist")
                exit()
            PasswordForUpdate = input("Enter your password: \n")
            if PasswordForUpdate == CheckIfUsernameExists["password"]:
                NewUsername = input("Enter your new username: \n")
                collection.update_one({"username" : UpdateUsernameUsername} , {"$set" : {"username" : NewUsername}})
                print("Username updated successfully")
            elif PasswordForUpdate != CheckIfUsernameExists["password"]:
                print("Incorrect Password")
                exit()
        elif inp == 6:
            exit()