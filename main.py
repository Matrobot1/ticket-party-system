import random
import json
import PyQt6

# Subsystem
available_tickets = random.sample(range(1, 570), 100)
ticket_choose = []


while True:
    print("---------------------- Tickets Party ----------------------")
    print("1. Buy Tickets")
    print("2. Shell your Tickets")
    print("3. View the date of party")
    print("4. Exit")

    option = int(input("Choose your action (1-4): "))



    if option == 1:
        print("Tickets available:", available_tickets)
        select_ticket = int(input("Choose you ticket: "))
        available_tickets.remove(select_ticket)
        ticket_choose.append(select_ticket)
        if select_ticket in available_tickets:

            print("Your ticket has been purchased!!!")
        else:
            print("This ticket has already been purchased :( ")

    elif option == 2:
        if not ticket_choose:
            print("You don't have any tickets to sell.")
        else:
            print("Your tickets:", ticket_choose)
            shell_ticket = int(input("Which ticket do you want to sell? "))
            if shell_ticket in ticket_choose:
                ticket_choose.remove(shell_ticket)
                available_tickets.append(shell_ticket)
                print("You sold your ticket!!!")
            else:
                print("You don't own this ticket.")

    elif option == 3:
        print("View your tickets:", ticket_choose)
        view_date = int(input("Put yout ticket for view date: "))
        if view_date in ticket_choose:
            with open('dates.json', 'r') as files:
                files = json.load(files)
                random_dates = random.choice(list(files.values()))
                print("Data sorteada:", random_dates)
        else:
            print("You do not have tickets :( ")







