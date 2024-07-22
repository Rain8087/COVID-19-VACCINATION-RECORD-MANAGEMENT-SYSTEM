#Jordan Lau Jing Hong
#TP064941

'''----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
#Main menu function end here
def Pmain_menu():
    while True:
        print("\n\n")
        print("1 - New patient registration")
        print("2 - Patient login")
        print("3 - Staff login")
        print("4 - Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            new_patient_reg()
        elif choice == "2":
            patient_login()
        elif choice == "3":
            staff_login()
        elif choice == "4":
            exit()
        else:
            print("\n\nInvalid option")

def Smenu():
    while True:
        print("\n\n")
        print("1 - Vaccine Administration")
        print("2 - Search Patient Record and Vaccination Status")
        print("3 - Statistical Information on Patients Vaccinated")
        print("4 - Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            vc_admin()
        elif choice == "2":
            vc_admin()
        elif choice == "3":
            vc_statusview()
        elif choice == "4":
            exit(Pmain_menu())
        else:
            print("Invalid choice")

#Main menu function end here
'''----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
#Patient function starts here
def new_patient_reg():
    with open("patients.txt", "a") as fh:
        rec = []#for patient.txt
        rec2 = []#for vaccination.txt
        flg = 0#to detetmine age range
        while True:
            name = input("Enter new patient name: ")
            if len(name.strip()) == 0:
                print("Please input valid name.")
            else:
                break
        while True:
            try:
                age = int(input("Enter new patient age: "))
                break
            except:
                print("Invalid input")
        if age<12:
            print("Sorry, no vaccine available for this age")
            exit(Pmain_menu())
        elif age>=18 and age<=45:
            flg = 1
        elif age>=12 and age<=45:
            flg = 2
        elif age>45:
            flg = 3
        if flg == 1:
            print("Vaccine available: ")
            print("="*65)
            print("Vaccine Code".center(14)+"|"+"Dosage Required".center(24)+"|"+"Interval Between Doses".center(24))
            print("="*65)
            print("AF".ljust(14)+"|"+"2".center(24)+"|"+"2 weeks (14 days)".center(24))
            print("BV".ljust(14)+"|"+"2".center(24)+"|"+"3 weeks (21 days)".center(24))
            print("CZ".ljust(14)+"|"+"2".center(24)+"|"+"3 weeks (21 days)".center(24))
            print("DM".ljust(14)+"|"+"2".center(24)+"|"+"4 weeks (28 days)".center(24))
            print("EC".ljust(14)+"|"+"1".center(24)+"|"+"-".center(24))
            print("="*65)
        elif flg == 2:
            print("Vaccine available: ")
            print("="*60)
            print("Vaccine Code".center(14)+"|"+"Dosage Required".center(24)+"|"+"Interval Between Doses".center(24))
            print("="*60)
            print("AF".ljust(14)+"|"+"2".center(24)+"|"+"2 weeks (14 days)".center(24))
            print("CZ".ljust(14)+"|"+"2".center(24)+"|"+"3 weeks (21 days)".center(24))
            print("DM".ljust(14)+"|"+"2".center(24)+"|"+"4 weeks (28 days)".center(24))
            print("="*65)
        elif flg == 3:
            print("Vaccine available: ")
            print("="*65)
            print("Vaccine Code".center(14)+"|"+"Dosage Required".center(24)+"|"+"Interval Between Doses".center(24))
            print("="*65)
            print("AF".ljust(14)+"|"+"2".center(24)+"|"+"2 weeks (14 days)".center(24))
            print("BV".ljust(14)+"|"+"2".center(24)+"|"+"3 weeks (21 days)".center(24))
            print("DM".ljust(14)+"|"+"2".center(24)+"|"+"4 weeks (28 days)".center(24))
            print("EC".ljust(14)+"|"+"1".center(24)+"|"+"-".center(24))
            print("="*65)
        while True:
            vc = input("Enter vaccine you wish to take: ")
            if flg == 1 and vc == "AF" or vc == "BV" or vc == "CZ" or vc == "DM" or vc =="EC":
                break
            elif flg == 2 and vc == "AF" or vc == "CZ" or vc =="DM":
                break
            elif flg == 3 and vc == "AF" or vc == "BC" or vc =="DM" or vc == "EC":
                break
            else:
                print("Invalid choice")
        print("Vaccine successfully register")
        print("\n\n")
        while True:
            vc_location = input("Enter vaccine centre you wish to go(VC1 or VC2): ")
            if vc_location == "VC1" or vc_location == "VC2":
                print("Location successfully register")
                break
            else:
                print("Invalid input")
        if vc_location == "VC1":
            p_id = gen_new_id("VCA")
        elif vc_location == "VC2":
            p_id = gen_new_id("VCB")
        print("Patient ID: ",p_id)
        while True:
            try:
                p_number = int(input("Enter contact number: "))
                break
            except:
                print("Invalid input")
        while True:
            p_pass = input("Enter password for your account: ")
            p_pass2 = input("Reenter your password: ")
            if p_pass == p_pass2:
                print("Password successfully register")
                break
            else:
                print("Password does not match first password")
        v_stage = 0
        rec.append(str(p_id))
        rec.append(str(p_pass))
        rec.append(name)
        rec.append(str(age))
        rec.append(str(p_number))
        rec.append(vc_location)
        rec.append(vc)
        fh.write(":".join(rec)+"\n")
        rec2.append(str(p_id))
        rec2.append(vc)
        rec2.append(str(v_stage))
        with open("vaccination.txt", "a") as fh:
            fh.write(":".join(rec2)+"\n")

def gen_new_id(eid):
    with open("id.txt", "r") as fh:
        rec = fh.readline()
        if eid == "VCA":
            ind = 0
        elif eid == "VCB":
            ind = 1
        mylist = rec.split(":")
        nextid = mylist[ind]
        newid = str(int(nextid[3:])+1)
        if len(newid) == 1:
            nextid = nextid[:3] + "0000" + newid
        elif len(newid) == 2:
            nextid = nextid[:3] + "000" + newid
        elif len(newid) == 3:
            nextid = nextid[:3] + "00" + newid
        elif len(newid) == 4:
            nextid = nextid[:3] + "0" + newid
        elif len(newid) == 5:
            nextid = nextid[:3] + newid
        mylist[ind] = nextid
        rec = ":".join(mylist)
        with open("id.txt", "w") as fh:
            fh.write(rec)
        return(newid)

def Pmod_data(PID):
    with open ("patients.txt", "r") as fh:
        allrec = []
        for line in fh:
            mylist = line.strip().split(":")
            allrec.append(mylist)
    while True:
        print("\n\n")
        print("1 - Patient Name")
        print("2 - Contact number")
        print("3 - Exit")
        choice = input("Enter field to modify: ")
        if choice == "1":
            print("\n\n")
            print("Current name: ", allrec[PID][2])
            while True:
                new_name = input("Enter new name: ")
                if len(new_name.strip()) == 0:
                    print("Please input valid name.")
                else:
                    break
            while True:
                print("\n\n")
                print("Current name: ", allrec[PID][2])
                print("New name: ", new_name)
                d_com = input("Comfirm (Y/N): ")
                if d_com == "Y":
                    allrec[PID][2] = new_name
                    with open("patients.txt", "w") as fh:
                        for line in allrec:
                            fh.write(":".join(line)+"\n")
                        break
                elif d_com == "N":
                    print("No change made")
                    break
                else:
                    print("Invalid input")
        elif choice == "2":
            while True:
                print("\n\n")
                print("Current contact number: ", allrec[PID][4])
                try:
                    p_number = int(input("New contact number: "))
                    break
                except:
                    print("Invalid input")
            while True:
                print("\n\n")
                print("Current contact number: ", allrec[PID][4])
                print("New contact number: ", p_number)
                d_com = input("Comfirm (Y/N): ")
                if d_com == "Y":
                    allrec[PID][4] = str(p_number)
                    with open("patients.txt", "w") as fh:
                        for line in allrec:
                            fh.write(":".join(line)+"\n")
                        break
                elif d_com == "N":
                    print("No change made")
                    break
                else:
                    print("Invalid input")
        elif choice == "3":
            break
        else:
            print("Invalid choice")

#Patient function end here
'''----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
#Staff function starts here
def vc_statusview():
    with open("vaccination.txt", "r") as fh:
        allrec = []
        for line in fh:
            mylist = line.strip().split(":")
            allrec.append(mylist)
    no_of_rec = len(allrec)
    af = 0
    bv = 0
    cz = 0
    dm = 0
    ec = 0
    d0 = 0
    d1 = 0
    d2 = 0
    for i in range(no_of_rec):
        if allrec[i][1] == "AF":
            af = af + 1
        elif allrec[i][1] == "BV":
            bv = bv + 1
        elif allrec[i][1] == "CZ":
            cz = cz + 1
        elif allrec[i][1] == "DM":
            dm = dm + 1
        elif allrec[i][1] == "EC":
            ec = ec + 1
        if allrec[i][2] == "0":
            d0 = d0 + 1
        elif allrec[i][2] == "1":
            d1 = d1 + 1
        elif allrec[i][2] == "2":
            d2 = d2 + 1
    print("Total number of patient: ", no_of_rec)
    print("Total number of patient who haven't receive any dose: ", d0)
    print("Total number of patient waiting for dose 2: ", d1)
    print("Total number of patient who completed vaccination: ", d2)
    print("Total number of patient choose AF: ", af)
    print("Total number of patient choose BV: ", bv)
    print("Total number of patient choose CZ: ", cz)
    print("Total number of patient choose DM: ", dm)
    print("Total number of patient choose EC: ", ec)

def vc_admin():
    from datetime import date
    from datetime import datetime
    from datetime import timedelta
    with open("patients.txt", "r") as fh:
        allrec = []
        for line in fh:
            mylist = line.strip().split(":")
            allrec.append(mylist)
    with open("vaccination.txt", "r") as fh2:
        allrec2 = []
        for line in fh2:
            mylist2 = line.strip().split(":")
            allrec2.append(mylist2)
    no_of_rec = len(allrec)
    no_of_rec2 = len(allrec2)
    flg = 0#use to determine if ID found in patient.txt
    flg2 = 0#use to identify EC vaccine
    flg3 = 0#use to identify vc_status
    flg4 = 0#use to identify no. of dose
    while True:
        print("\n\n")
        search = input("Enter patient ID to search (Type exit to exit): ")
        for i in range (no_of_rec):
            if search == allrec[i][0]:
                j = i
                flg = 1
        if flg == 1:
            for k in range(no_of_rec2):
                if search == allrec2[k][0]:
                    l = k
            while True:
                print("\n\n")
                print("Patient ID: ", allrec[j][0])
                print("Name: ", allrec[j][2])
                print("Age: ", allrec[j][3])
                print("Vaccine centre choosen: ", allrec[j][5])
                print("Vaccine choosen ", allrec[j][6])
                try:
                    print("Vaccine time: ",allrec2[l][3])
                except:
                    print("Patient haven't been vaccine")
                try:
                    print("Dose1 date: ",allrec2[l][4])
                except:
                    pass
                try:
                    print("Dose2 date: ",allrec2[l][5])
                except:
                    pass
                print("\n\n")
                if allrec2[l][1] == "EC":
                    flg2 = 1
                if allrec2[l][2] == "0":
                    print("Pending for dose")
                    flg4 = 1
                elif allrec2[l][2] == "1":
                    print("Pending for second dose")
                elif allrec2[l][2] == "2":
                    print("All dose complete!")
                    exit(Smenu())
                print("1 - Sign up for vaccination")
                print("2 - Exit")
                choice = input("Enter your choice: ")
                if choice == "1":
                    print("Dose complete?")
                    while True:
                        vc_status = input("Y/N: ")
                        if vc_status == "Y":
                            flg3 = 1
                            if flg2 == 0:
                                allrec2[l][2] = str(int(allrec2[l][2])+1)
                            elif flg2 == 1:
                                allrec2[l][2] = str(2)
                            break
                        elif vc_status == "N":
                            print("No change is made")
                            flg3 = 0
                            break
                        else:
                            print("Invalid input")
                    if flg4 == 1 and flg3 == 1:
                        vc = allrec[j][6]
                        d_time = datetime.now().strftime("%H.%M")
                        d1_date = date.today()
                        if vc == "AF":
                            d2_date = d1_date + timedelta(days=14)
                        elif vc == "BV" or vc == "CZ":
                            d2_date = d1_date + timedelta(days=21)
                        elif vc == "DM":
                            d2_date = d1_date + timedelta(days=28)  
                        allrec2[l].append(str(d_time))
                        allrec2[l].append(str(d1_date))
                        try:
                            allrec2[l].append(str(d2_date))
                        except:
                            pass
                    with open("vaccination.txt", "w") as fh2:
                            for line in allrec2:
                                fh2.write(":".join(line)+"\n")
                    print("Vaccine status had been update")
                    exit(Smenu())
                elif choice == "2":
                    exit(Smenu())
                else:
                    print("Invalid choice")
        if search == "exit":
            exit(Smenu())
        else:
            print("Patient not found")

#Staff function end here
'''----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
#Login system starts here
def patient_login():
    allrec = []
    allrec2 = []
    with open("patients.txt", "r") as fh:
        for line in fh:
            mylist = line.strip().split(":")
            allrec.append(mylist)
    with open("vaccination.txt", "r") as fh:
        for line in fh:
            mylist2 = line.strip().split(":")
            allrec2.append(mylist2)
    no_of_user = len(allrec)
    no_of_user2 = len(allrec2)
    while True:
        flg_valid = 0
        user = input("Enter patient ID: ")
        password = input("Enter password: ")
        for i in range(no_of_user):
            if user == allrec[i][0] and password == allrec[i][1]:
                flg_valid = 1
                j = i
        if flg_valid == 1:
            for k in range(no_of_user2):
                if user == allrec2[k][0]:
                    l = k
                else:
                    print("Patient not found in vaccination.txt.")
                    print("Please contact staff.")
            print("Login successful")
            while True:
                print("\n\n")
                print("1 - Modify data")
                print("2 - View current status")
                print("3 - Exit (To refresh current data)")
                choice = input("Enter your choice: ")
                if choice == "1":
                    Pmod_data(j)
                elif choice == "2":
                    print("\n\n")
                    print("Patient ID: ", allrec[j][0])
                    print("Name: ", allrec[j][2])
                    
                    print("Vaccine centre choosen: ", allrec[j][5])
                    print("Vaccine choosen: ", allrec[j][6])
                    if allrec2[l][2] == "0":
                        print("Vaccine status: Pending for dose")
                    elif allrec2[l][2] == "1":
                        print("Vaccine status: Dose 1 complete, pending for dose 2")
                    elif allrec2[l][2] == "2":
                        print("Vaccine status: All dose complete.")
                    try:
                        print("Vaccine time: ",allrec2[l][3])
                    except:
                        pass
                    try:
                        print("Dose1 date: ",allrec2[l][4])
                    except:
                        print("Patient haven't been vaccine")
                    try:
                        print("Dose2 date: ",allrec2[l][5])
                    except:
                        pass
                elif choice == "3":
                    exit(Pmain_menu())
                else:
                    print("Invalid choice")
        else:
            print("Invalid user or password")
            exit(Pmain_menu())

def staff_login():
    allrec = []
    with open("staff.txt", "r") as fh:
        for line in fh:
            mylist = line.strip().split(":")
            allrec.append(mylist)
    no_of_user = len(allrec)
    while True:
        flg_valid = 0
        user = input("Enter username: ")
        password = input("Enter password: ")
        for i in range(no_of_user):
            if user == allrec[i][1] and password == allrec[i][2]:
                flg_valid = 1
        if flg_valid == 1:
            print("Login successful")
            Smenu()
        else:
            print("Invalid user or password")
            exit(Pmain_menu())

#Login system end here
'''----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
#Start program
Pmain_menu()
#code end
