import random
import csv
import datetime
import time

def print_with_delay(text, delay=20):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def entry_animation():
    print(end=' ')
    print_with_delay("-----------------WELCOME TO LAVISH AIRLINES--------------- ", delay=0.1)
if __name__ == "__main__":
    entry_animation()



AD_US=input("Enter as 1.ADMIN\n   2.PASSENGER\n ")
if AD_US=='1':
        def Add_flight_details():
            data=[]
            FLIGHT_NO=int(input("Enter the flight number:"))
            year=int(input('Enter the year of boarding(YYYY):'))
            month=int(input('Enter the month of boarding(MM):'))
            day=int(input('Enter the day of boarding(DD):'))
            hour=int(input('Enter the hour of departure(HH)'))
            mint=int(input('Enter the minute of departure(MM)'))
            sec=int(input('Enter the second of departure(SS)'))
            hour1=int(input('Enter the hour of arrival(HH)'))
            mint1=int(input('Enter the minute of arrival(mm)'))
            sec1=int(input('Enter the second of arrival(ss)'))
            date_and_time_of_departure=datetime.datetime(year,month,day,hour,mint,sec)
            date_and_time_of_arrival=datetime.datetime(year,month,day,hour1,mint1,sec1)
            
            # Assuming you have a cursor named cursor you want to execute this query on:
            AIRLINES=input('Enter the airlines:')
            from_city=input('Enter the city of departure')
            to_city=input('Enter the city of arrival')
            flight_status=input("Enter the status(Scheduled,delayed,cancelled) of the flight")
            data=[FLIGHT_NO,date_and_time_of_departure,date_and_time_of_arrival,AIRLINES,from_city,to_city,flight_status]
            f_object=open('event.csv', 'a')
            writer_object = csv.writer(f_object)
            writer_object.writerow(data)
            f_object.close()
            print("THE FLIGHT HAS BEEN ADDED")
            MENU()
        def display_flight_details():
            print('The list of all the flights available today are')
            print("1.LAVISH AIRLINES")
            
            print()
            with open("event.csv", 'r') as f_object:
                csvreader = csv.reader(f_object)
                for row in csvreader:
                    print(row)
            MENU()   

        
        def MENU():
            print("Welcome to Flight Management Record")
            print("Press ")
            print("1 to ADD/UPDATE FLIGHTS")
            print("2 to VIEW FLIGHTS")
           
            print("3 to Exit")
            # Taking choice from user
            ABC = input("Enter your Choice ")
            if ABC=='none':
                MENU()
            elif ABC =='1':
                Add_flight_details()
            elif ABC == '2':
                display_flight_details()
            
            elif ABC== '3':
                exit(0)
            else:
                print("Invalid Choice")
                MENU()
        MENU()
    
elif AD_US=='2':
        def Passenger_booking():
              totl_seniors_price = 0
              totl_adults_price = 0
              totl_childrens_price = 0
              totl_price = 0
              totl_passengers=0
              return_date= 'none'
              fare=0  
              print("which trip would you like to make?")
              print(" 0.exit")
              print(" 1. One-way trip")
              

              triptype=input('Please enter your choice: ')
              if triptype=='0':
                  exit(0)
              elif triptype =='1':
                   output = open('flight.csv', 'wb')
                   Ticket_no=random.randint(1,10000000)
                   Airlines=input("Enter name of the Airlines:")
                   from_city=input("Enter the city of departure:")
                   to_city=input("Enter the city of arrival:")
                   print('The total flights available today are:')
                   year=int(input('Enter the year of boarding(YYYY):'))
                   month=int(input('Enter the month of boarding(MM):'))
                   day=int(input('Enter the day of boarding(DD):'))
                   hour=int(input('Enter the hour of departure(HH)'))
                   mint=int(input('Enter the minute of departure(MM)'))
                   sec=int(input('Enter the second of departure(SS)'))
                   hour1=int(input('Enter the hour of arrival(HH)'))
                   mint1=int(input('Enter the minute of arrival(mm)'))
                   sec1=int(input('Enter the second of arrival(ss)'))
                   date_and_time_of_departure=datetime.datetime(year,month,day,hour,mint,sec)
                   date_and_time_of_arrival=datetime.datetime(year,month,day,hour1,mint1,sec1)
                   Flight_num=input("Enter the flight number of the flight that you want to travel in from the list of available flights:")
                   print("The age groups are:")
                   print("(a) Adult(>12yrs)&(<60yrs)  ")
                   print("(b) Child(2-12yrs) ")
                   print("(c) Infant(<2yrs)  ")
                   print("(d) Senior citizens(>60yrs")
                   print()
                   print(
                          "Note: Long distance travelling through air is not recommended for infants & senior citizens to avoid possible health complications during flight")
                   print()
                   adult = int(input("Enter number of adults                                   :    "))
                   print()
                   child = int(input("Enter number of children                                 :    "))
                   print()
                   infant = int(input("Enter number of infants( if travelling else enter 0)     :    "))
                   print()
                   senior = int(input("Enter the number of senior citizens travelling           :    "))
                   print()
                   print("Please note that if the passenger is a senior citizen(>60yrs)  It is mandatory to produce proof of Date of Birth at the airport,")
                   print("without which prevailing fares will be charged.")

        
                   print(" TRAVEL CLASSES")
                   print("1. Economy")
                   print("2. Premium Economy")
                   print("3. Business")
                   print()
                   ch = int(input("Please choose the travel class"))

                   print("1. Regular fares")
                   print()
                   print("2. Armed forces :  ")
                   print(
                       "Applicable for serving and retired personnel of Armed Forces and Paramilitary Forces, their recognised dependants like")
                   print(
                       "spouses and children, and war widows.It is mandatory to show a valid ID or dependant card at the airport, without which boarding ")
                   print("might be denied.")
                   print()
                   print("3. Student fares :  ")
                   print(
                         "Only students above 12 years of age are eligible for special fares and/or additional baggage allowances. Carrying valid student ID")
                   print(
                         "cards and student visas (where applicable) is mandatory, else the passenger may be denied boarding or asked to pay for extra baggage.")
                   print()
                   fares = int(input("Please select fare type    :    "))
                   print()

                   # fare calculation for economy
                   if ch == 1:
                      if (senior > 0):
                          fare = (senior * 5000)
                          disp = (fare * 20) / 100
                          totl_seniors_price = fare - disp

                      if (adult > 0):
                              adultfare = (adult * 5000)
                              adultdisp = 0
                              if (adult > 9):
                                  adultdisp = (adultfare * 15) / 100

                      totl_adults_price = adultfare - adultdisp

                      if (child > 0):
                          childfare = child * 3500
                          childdisp = 0
                      if (child > 6):
                          childdisp = (childfare * 6) / 100
                      totl_childrens_price = childfare - childdisp

                      totl_price = totl_seniors_price + totl_adults_price + totl_childrens_price

                      # discount calculation for Regular
                      if fares == 1:
                          totl_price = totl_price + 0

                      # discount calculation for Armed forces
                      if fares == 2:
                          fares_disc = 5000
                          totl_price = totl_price - fares_disc

                      # discount calculation for Students
                      if fares == 3:
                          fares_disc = 2000
                          totl_price = totl_price - fares_disc

                 # fare calculation for premium economy
                   if ch == 2:
                       if (senior > 0):
                         fare = (senior * 6000)
                         disp = (fare * 20) / 100
                         totl_seniors_price = fare - disp

                       if (adult > 0):
                         adult_fare = (adult * 6000)
                         adult_disp = 0
                         if (adult > 9):
                             adult_disp = (adult_fare * 15) / 100
                         totl_adults_price = adult_fare - adult_disp

                       if (child > 0):
                           childfare = child * 4500
                           childdisp = 0
                           if (child > 6):
                               childdisp = (childfare * 6) / 100
                           totlChildrensPrice = childfare - childdisp

                       totl_price = totl_seniors_price + totl_adults_price + totl_childrens_price

                       # discount calculation for Regular
                       if fare == 1:
                           totl_price = totl_price + 0

                       # discount calculation for Armed forces
                       if fare == 2:
                           fares_disc = 5000
                           totl_price = totl_price - fares_disc

                       # discount calculation for Students
                       if fare == 3:
                           fares_disc = 2000
                           totl_price = totl_price - fares_disc

                    # fare calculation for business
                   if ch == 3:
                       if (senior > 0):
                           fare = (senior * 8000)
                           disp = (fare * 20) / 100
                           totl_seniors_price = fare - disp

                       if (adult > 0):
                           adultfare = (adult * 8000)
                           adultdisp = 0
                           if (adult > 9):
                               adultdisp = (adultfare * 15) / 100
                           totl_adults_price = adultfare - adultdisp

                       if (child > 0):
                           childfare = child * 5500
                           childdisp = 0
                           if (child > 6):
                               childdisp = (childfare * 6) / 100
                           totl_childrens_price = childfare - childdisp

                       totl_price = totl_seniors_price + totl_adults_price + totl_childrens_price

                       # discount calculation for Regular
                       if fares == 1:
                           totl_price = totl_price + 0

                       # discount calculation for Armed forces
                       if fares == 2:
                           fares_disc = 5000
                           totl_price = totl_price - fares_disc

                       # discount calculation for Students
                       if fares == 3:
                           fares_disc = 2000
                           totl_price = totl_price - fares_disc
                   data=[Ticket_no, Flight_num, Airlines, date_and_time_of_departure, date_and_time_of_arrival, from_city, to_city, totl_price] 
                   print("The Ticket No.:", Ticket_no)
                   print("The Flight No.:", Flight_num)
                   print("The Airlines Name:", Airlines)
                   print("The Date and Time of Departure:", date_and_time_of_departure)
                   print("The Date and Time of Arrival:", date_and_time_of_arrival)
                   print("Departure City:", from_city)
                   print("Arrival City:", to_city)
                   print("Total Fare of Ticket:", totl_price, "$")
                   
                   f_object=open('flight.csv', 'a')
                   writer_object = csv.writer(f_object)
                   writer_object.writerow(data)
                   f_object.close()
                   print("Passenger_booking details Added Successfully ")
                   Menu()
             
             

        def display_passenger_booking_details():
            print('YOUR FINAL FLIGHT DETAILS ARE READY')
            print()
            with open("flight.csv", 'r') as output:
                csvreader = csv.reader(output)
                for row in csvreader:
                    print(row)
            output.close()
            Menu()
        def cancel_flight():
                    print('TO CANCEL YOUR FLIGHT TICKET')
                    ticket_no=input("Enter your ticket number:")
                    with open('flight.csv', 'wb+') as output:
                        writer = csv.writer(output)
                        CSVREADER=csv.reader(output)
                        for row in CSVREADER:
                            if row == ticket_no:
                                writer.writerow(row)
                    output.close()
                    print("your flight is cancelled")

                    
                    Menu()
        def Menu():
                print("Welcome to Passenger Management Record")
                print("Press ")
                print("1 to Book flights")
                print("2 to Display flights")
                print("3 to Cancel flight")
                print("4 to Exit")
                # Taking choice from user
                ABC = input("Enter your Choice ")
                if ABC=='none':
                    Menu()
                elif ABC =='1':
                    Passenger_booking()
                elif ABC == '2':
                    display_passenger_booking_details()
                elif ABC== '3':
                    cancel_flight()
                elif ABC== '4':
                    exit(0)
                else:
                    print("Invalid Choice")
                    Menu()
        Menu()
        
def generate_ticket(ticket_data):
    ticket_file = 'ticket.csv'

    with open(ticket_file, 'a', newline='') as f_object:
        writer_object = csv.writer(f_object)
        writer_object.writerow(ticket_data)

    print("Ticket generated successfully.")
def Passenger_booking():
    # ... (existing code)

    # Assuming you have collected necessary details for the ticket
    ticket_data = [Ticket_no, Flight_num, Airlines, date_and_time_of_departure, date_and_time_of_arrival, from_city, to_city, totl_price]

    # Generate ticket
    generate_ticket(ticket_data)

    print("Passenger_booking details Added Successfully ")
    Menu()
