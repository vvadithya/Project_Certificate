# Made by Vedula Venkata Adithya and Arjun Singh

# Importing the necessary modules
import PySimpleGUI as sg
import time
import calendar
import webbrowser
from fpdf import FPDF 
import datetime
import string
import random
# functions to write data to pdf
def resident_write_pdf(name , day , month , year , address , image, nation , gender):
                pdf = FPDF(orientation = 'L' , format = 'Legal')
                pdf.add_page()
                pdf.set_font("Arial", 'BU' , 40)                
                title = "Royal Oman Police"
                pdf.cell(200, 15, txt = title, ln = 1, align = 'L') 
                pdf.set_font("Arial", size=14)               
                name = "Name: " + str(name)
                pdf.cell(200, 15, txt = name, ln = 2, align = 'L') 
                address = "Address: " + str(address)
                pdf.cell(200, 15, txt = address, ln = 3, align = 'L')
                gender = "Gender: " + str(gender)
                pdf.cell(200, 15, txt =gender , ln=4 , align = 'L')
                date_of_birth = "Date of Birth: " + str(day) + " " + month + " " + str(year)
                pdf.cell(200, 15, txt = date_of_birth , ln = 5 , align = 'L')                 
                date_of_issue = "Date of Card Issue: "  + str(today.day) + " "  + str(calendar.month_name[today.month]) + " " + str(today.year)            
                pdf.cell(200, 15, txt = date_of_issue , ln=6 , align = 'L')
                date_of_expiry = "Date of Card Expiry: " + str(today.day) + " "  + str(calendar.month_name[today.month]) + " " + str(today.year + 2)
                pdf.cell(200, 15, txt = date_of_expiry , ln=7 , align = 'L')
                nationality = "Nationality: " + str(nation)
                pdf.cell(200, 15, txt = nationality , ln=8 , align = 'L')
                code = []
                for i in range(int(17)):
                    value = random.choice(characters)
                    
                    code.append(str(value))                 
                code = "ID Code: " + "".join(code)
                pdf.cell(200, 15, txt = code , ln=9 , align = 'L')
                pdf.image(image , 250 , 50 , w=120)
                pdf.image("qrcode.png" , 280 , 150 , w=60)
                pdf.set_font("Arial", size=16)                  
                pdf.cell(200, 15, txt = "Verify this card by scanning the QR Code" , ln=14 , align = 'C')                
                pdf.output("Resident.pdf")   
                sg.Popup('Completed,saved resident card as "Resident.pdf"')     
def birth_write_pdf(name , day , month , year , nation , father , mother , gender):
                pdf = FPDF(orientation = 'L' , format = 'Legal')
                pdf.add_page()
                pdf.set_font("Arial", 'BU' , 40)                
                title = "Royal Oman Police"
                pdf.cell(200, 15, txt = title, ln = 1, align = 'L') 
                pdf.set_font("Arial", size=14)               
                name = "Name: " + str(name)
                pdf.cell(200, 15, txt = name, ln = 2, align = 'L') 
                gender = "Gender: " + str(gender)
                pdf.cell(200, 15, txt =gender , ln=3 , align = 'L')
                date_of_birth = "Date of Birth: " + str(day) + " " + month + " " + str(year)
                pdf.cell(200, 15, txt = date_of_birth , ln = 4 , align = 'L')                 
                nationality = "Nationality: " + str(nation)
                pdf.cell(200, 15, txt = nationality , ln=5 , align = 'L')
                father = "Name of Father: " + str(father)
                pdf.cell(200, 15, txt = father , ln=6 , align = 'L')
                mother = "Name of Mother: " + str(mother)
                pdf.cell(200, 15, txt = mother , ln=7 , align = 'L')
                code = []
                for i in range(int(17)):
                    value = random.choice(characters)
                    
                    code.append(str(value))                 
                code = "ID Code: " + "".join(code)
                pdf.cell(200, 15, txt = code , ln=8, align = 'L')
                pdf.set_font("Arial", size=16)                  
                pdf.output("birth_certificate.pdf")   
                sg.Popup('Completed,saved birth certififcate as "birth_certificate.pdf"')  
# Important set of data used later in the program
# Today's date,this is used for the date of issue of the card
today = datetime.datetime.now()
# The Characters to be used for making the code number of the card
characters = string.ascii_uppercase + string.digits
# list of nationalities(197 countries in this list)
nationalities = ['Afghan', 'Albanian', 'Algerian', 'American', 'Andorran', 'Angolan', 'Antiguans', 'Argentinean', 'Armenian', 'Australian', 'Austrian', 'Azerbaijani', 'Bahamian', 'Bahraini', 'Bangladeshi', 'Barbadian', 'Barbudans', 'Batswana', 'Belarusian', 'Belgian', 'Belizean', 'Beninese', 'Bhutanese', 'Bolivian', 'Bosnian', 'Brazilian', 'British', 'Bruneian', 'Bulgarian', 'Burkinabe', 'Burmese', 'Burundian', 'Cambodian', 'Cameroonian', 'Canadian', 'Cape Verdean', 'Central African', 'Chadian', 'Chilean', 'Chinese', 'Colombian', 'Comoran',  'Congolese', 'Costa Rican', 'Croatian', 'Cuban', 'Cypriot', 'Czech', 'Danish', 'Djibouti', 'Dominican', 'Dutch', 'Dutchman', 'Dutchwoman', 'East Timorese', 'Ecuadorean', 'Egyptian', 'Emirian', 'Equatorial Guinean', 'Eritrean', 'Estonian', 'Ethiopian', 'Fijian', 'Filipino', 'Finnish', 'French', 'Gabonese', 'Gambian', 'Georgian', 'German', 'Ghanaian', 'Greek', 'Grenadian', 'Guatemalan', 'Guinea-Bissauan', 'Guinean', 'Guyanese', 'Haitian', 'Herzegovinian', 'Honduran', 'Hungarian', 'I-Kiribati', 'Icelander', 'Indian', 'Indonesian', 'Iranian', 'Iraqi', 'Irish', 'Israeli', 'Italian', 'Ivorian', 'Jamaican', 'Japanese', 'Jordanian', 'Kazakhstani', 'Kenyan', 'Kittian and Nevisian', 'Kuwaiti', 'Kyrgyz', 'Laotian', 'Latvian', 'Lebanese', 'Liberian', 'Libyan', 'Liechtensteiner', 'Lithuanian', 'Luxembourger', 'Macedonian', 'Malagasy', 'Malawian', 'Malaysian', 'Maldivan', 'Malian', 'Maltese', 'Marshallese', 'Mauritanian', 'Mauritian', 'Mexican', 'Micronesian', 'Moldovan', 'Monacan', 'Mongolian', 'Moroccan', 'Mosotho', 'Motswana', 'Mozambican', 'Namibian', 'Nauruan', 'Nepalese', 'Netherlander', 'New Zealander', 'Ni-Vanuatu', 'Nicaraguan', 'Nigerian', 'Nigerien', 'North Korean', 'Northern Irish', 'Norwegian', 'Omani', 'Pakistani', 'Palauan', 'Panamanian', 'Papua New Guinean', 'Paraguayan', 'Peruvian', 'Polish', 'Portuguese', 'Qatari', 'Romanian', 'Russian', 'Rwandan', 'Saint Lucian', 'Salvadoran', 'Samoan', 'San Marinese', 'Sao Tomean', 'Saudi', 'Scottish', 'Senegalese', 'Serbian', 'Seychellois', 'Sierra Leonean', 'Singaporean', 'Slovakian', 'Slovenian', 'Solomon Islander', 'Somali', 'South African', 'South Korean', 'Spanish', 'Sri Lankan', 'Sudanese', 'Surinamer', 'Swazi', 'Swedish', 'Swiss', 'Syrian', 'Taiwanese', 'Tajik', 'Tanzanian', 'Thai', 'Togolese', 'Tongan', 'Trinidadian or Tobagonian', 'Tunisian', 'Turkish', 'Tuvaluan', 'Ugandan', 'Ukrainian', 'Uruguayan', 'Uzbekistani', 'Venezuelan', 'Vietnamese', 'Welsh', 'Yemenite', 'Zambian', 'Zimbabwean']
# list of genders
genders_list = ["Male" , "Female"]
# list of Months
months_list = ["January", "February", "March", "April" , "May" , "June" , "July" , "August" , "September" , "October" , "November" , "December"]
# The main process to convert the data to a pdf certificate
def birth_certificate():
        # setting the window theme to 'TealMono'
        sg.theme("TealMono")
        # The layout for the theme
        layout = [
        # some text 
        [sg.Text('Enter the Name: ')],
        #Input of the persons name,the key of this input is 'name' 
        [sg.InputText(key='name')],
        # some text
        [sg.Text('Choose the Gender: ')],
        # asking user to choose Gender , the key of this input is 'gender' 
        [sg.Combo(genders_list , size=20  , key='gender')],
        # some text
        [sg.Text('Enter the year they were born in: ')],
        # asking user to enter the year they were born,key is 'year'
        [sg.InputText(key='year')],
        # some text
        [sg.Text('Choose the month they were born in: ')], 
        # asking user to choose the month they were born,key is 'month'    
        [sg.Combo(months_list , size=20  , key='month')],     
        # some text  
        [sg.Text('Enter the day they were born(if person was born on 8th- 8 , if person was born on 25th - 25): ')],
        # asking user to input the day they were born,key is 'day'
        [sg.InputText(key='day')],   
        # some text
        [sg.Text('Choose their nationality: ')],            
        # asking user to choose their nationality,key is 'nation' 
        [sg.Combo(nationalities , size=20  , key='nation')],         
        # some text  
        [sg.Text("Enter the Father's name ")],
        # asking user to input father name,key is 'father'
        [sg.InputText(key='father')], 
        # some text  
        [sg.Text("Enter the Mother's name ")],
        # asking user to input father name,key is 'father'
        [sg.InputText(key='mother')],                  
        # a button which shows Generate a birth certificate,with dimensions given in a tuple
        [sg.Submit('Generate a Birth Certificate' , size=(15,5))]               
        ]                       
        # creating a window,title = 'Royal Oman Police , design = layout , size given below and alllowing the window to be resizable
        mainwindow = sg.Window('Birth Certificate' , layout , size = (700,700) , resizable = True)    
        # while loop
        while True:
            # no. of errors in code is 0
            errors = 0
            # an errors_list,which gives useful information on the error
            errors_list = []
            # Taking all the actions , input values from the graphical part of the program 
            event, values = mainwindow.read()
            # saving the name entered to a variable 'name'
            name = values['name']
            # saving the nation chosen state to a variable 'nation'
            nation = values['nation']
            # saving the gender chosen to a variable 'gender'
            gender = values['gender']
            mother = values['mother']
            father = values['father']
            
            if gender not in genders_list or gender == '':
                # incrementing the number of errors
                errors = errors + 1
                # adding the error to the errors_list
                errors_list.append("You have typed a gender which is not present in the list")
            # saving the year they were born to a variable 'year'
            year = values['year']
            # tries to convert if the year is an integer,if not runs the code under except: 
            try:
                year = int(year)
            except:
                # if above code is unsuccessful,this code is run
                # incrementing the number of errors
                errors = errors + 1  
                # adding the error to the errors_list
                errors_list.append("You must provide a year in numeral form(like 2022 not two thousand twenty two")              
            # saving the month they chose they were born to a variable 'month'
            month = values['month']
            # checks if month is an invalid input
            if month not in months_list or month == '':
                # incrementing the number of errors
                errors = errors + 1
                # adding the error to the errors_list
                errors_list.append("You must choose a month from the following options")
            # saving the day they were born to a variable day
            day = values['day']
            # tries to convert day to an integer
            try:
                day = int(day)
                # checks if day is an invalid input
                if day > 31 or day <= 0:
                    # incrementing the number of errors
                    errors = errors + 1
                    # adding the error to the error_list
                    errors_list.append('A month cannot have less than zero days or more than 31 days')
            # if above code is unsuccessful,this code is run
            except:
                # incrementing the number of errors
                errors = errors + 1
                # adding the error to the error_list
                errors_list.append("You must provide a day in numeral form(like 14,not fourteen ) and also ensure the number of days you have entered is less than or equal to 31")                                
            # checking if the nation entered is valid
                

                
            # if number of errors = 0, then the function to write pdf with parameters is called
            if errors == 0:
                birth_write_pdf(name , day , month , year , nation , father , mother , gender)
            # if there are more than 0 errors,then the below code is run
            if errors > 0:                
                # pausing the program for a second
                time.sleep(1)               
                # the message to be displayed to the user  
                text = "There are {} error/errors in your data.".format(errors) + str(errors_list)
                # showing the message in a popup window
                sg.Popup(text)                    
                    
            # Closes/Exits the Program if either stopped from command line or from the window
            if event == sg.WIN_CLOSED or event == 'Cancel': 
                break            
            
        #  Closes the main window at the end of the program

                    
        mainwindow.close()    
# Graphical Window for the resident card
def resident_window():
        # setting the window theme to 'TealMono'
        sg.theme("TealMono")
        # The layout for the theme
        layout = [
        # some text 
        [sg.Text('Enter the Name: ')],
        #Input of the persons name,the key of this input is 'name' 
        [sg.InputText(key='name')],
        # some text
        [sg.Text('Enter the Address: ')],
        # address of the person, the key of this input is 'address'
        [sg.InputText(key='address')],
        # some text
        [sg.Text('Choose the Gender: ')],
        # asking user to choose Gender , the key of this input is 'gender' 
        [sg.Combo(genders_list , size=20  , key='gender')],
        # some text
        [sg.Text('Enter the year they were born in: ')],
        # asking user to enter the year they were born,key is 'year'
        [sg.InputText(key='year')],
        # some text
        [sg.Text('Choose the month they were born in: ')], 
        # asking user to choose the month they were born,key is 'month'    
        [sg.Combo(months_list , size=20  , key='month')],
        # some text
        [sg.Text('Choose their nationality: ')],            
        # asking user to choose their nationality,key is 'nation' 
        [sg.Combo(nationalities , size=20  , key='nation')],      
        # some text  
        [sg.Text('Enter the day they were born(if person was born on 8th- 8 , if person was born on 25th - 25): ')],
        # asking user to input the day they were born,key is 'day'
        [sg.InputText(key='day')],   
        # some text
        [sg.Text('Choose the image for the card(Only .jpg): ')],
        # asking user to select a .jpg image for the user,key is "image"
        [sg.FileBrowse(key = "image")],
        # a button which shows Generate a resident card,with dimensions given in a tuple
        [sg.Submit('Generate a Resident Card' , size=(15,5))]               
        ]                       
        # creating a window,title = 'Royal Oman Police , design = layout , size given below and alllowing the window to be resizable
        mainwindow = sg.Window('Resident Card' , layout , size = (700,700) , resizable = True)    
        # while loop
        while True:
            # no. of errors in code is 0
            errors = 0
            # an errors_list,which gives useful information on the error
            errors_list = []
            # Taking all the actions , input values from the graphical part of the program 
            event, values = mainwindow.read()
            # saving the name entered to a variable 'name'
            name = values['name']
            # saving the nation chosen state to a variable 'nation'
            nation = values['nation']
            # saving the address entered to a variable 'address' 
            address = values['address']
            # saving the gender chosen to a variable 'gender'
            gender = values['gender']
            # checking if the gender is an invalid input or if gender is empty
            if gender not in genders_list or gender == '':
                # incrementing the number of errors
                errors = errors + 1
                # adding the error to the errors_list
                errors_list.append("You have typed a gender which is not present in the list")
            # saving the year they were born to a variable 'year'
            year = values['year']
            # tries to convert if the year is an integer,if not runs the code under except: 
            try:
                year = int(year)
            except:
                # if above code is unsuccessful,this code is run
                # incrementing the number of errors
                errors = errors + 1  
                # adding the error to the errors_list
                errors_list.append("You must provide a year in numeral form(like 2022 not two thousand twenty two")              
            # saving the month they chose they were born to a variable 'month'
            month = values['month']
            # checks if month is an invalid input
            if month not in months_list or month == '':
                # incrementing the number of errors
                errors = errors + 1
                # adding the error to the errors_list
                errors_list.append("You must choose a month from the following options")
            # saving the day they were born to a variable day
            day = values['day']
            # tries to convert day to an integer
            try:
                day = int(day)
                # checks if day is an invalid input
                if day > 31 or day <= 0:
                    # incrementing the number of errors
                    errors = errors + 1
                    # adding the error to the error_list
                    errors_list.append('A month cannot have less than zero days or more than 31 days')
            # if above code is unsuccessful,this code is run
            except:
                # incrementing the number of errors
                errors = errors + 1
                # adding the error to the error_list
                errors_list.append("You must provide a day in numeral form(like 14,not fourteen ) and also ensure the number of days you have entered is less than or equal to 31")                                
            # checking if the nation entered is valid
            if nation not in nationalities or nation == '':
                errors = errors + 1
                errors_list.append("You must choose a month from the following options")            
            # getting the path of the image
            image = values['image']
            # checking if the image is .jpg
            if image.endswith(".jpg") == False:
                # incrementing the number of errors
                errors = errors + 1
                # adding the error to the errors_list
                errors_list.append("Invalid image format,only .jpg and .png allowed")
                

                
            # if number of errors = 0, then the function to write pdf with parameters is called
            if errors == 0:
                resident_write_pdf(name , day , month , year , address , image, nation , gender)
            # if there are more than 0 errors,then the below code is run
            if errors > 0:                
                # pausing the program for a second
                time.sleep(1)               
                # the message to be displayed to the user  
                text = "There are {} error/errors in your data.".format(errors) + str(errors_list)
                # showing the message in a popup window
                sg.Popup(text)                    
                    
            # Closes/Exits the Program if either stopped from command line or from the window
            if event == sg.WIN_CLOSED or event == 'Cancel': 
                break               #  Closes the main window at the end of the program

                    
    

# The Main Graphical window for the User
def Main():
    
    sg.theme("TealMono") 
    layout = [
        [sg.Text('Made By Vedula Venkata Adithya and Arjun Singh'),],
        [sg.Button('Documentation' , key='doc')],
        [sg.Button('Resident Card' , key='res' ,size=(15,10))],
        [sg.Button('Birth Certificate' , key='birth' , size=(15,10))]          
        ]
    # Makes a window,gives it a title 'Certificate Generator' and a layout of variable 'layout1'.
    # Defines the window size of x=600 , y = 600 and allows resizing of the window.
    mainwindow = sg.Window('Certificate Generator', layout , size=(600,600) , resizable=True)

    # While loop
    while True:
        # Taking all the actions , input values from the graphical part of the program 
        event, values = mainwindow.read()
        # when aadhar button is clicked
        # when pan button is clicked
        if event == 'res':
            resident_window()
        if event == 'birth':
            birth_certificate()
        # When the 'documentation' button is clicked 
        if event == 'doc':
            # opens the Github Repository for documentation
            webbrowser.open('https://github.com/vvadithya/Certificate_Generator' , new=2)
        # Closes/Exits the Program if either stopped from command line or from the window
        if event == sg.WIN_CLOSED or event == 'Cancel': 
            break
        
    # Closes the main window at the end of the program
    mainwindow.close()


# calling the main function
Main()