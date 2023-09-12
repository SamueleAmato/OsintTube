from cmd import InformationGathering, utility
import os
import sys

os.system("clear")

try:
    id = sys.argv[1]
    save = ""
    if utility.IsId(id) == False:
        exit("Error: it seems you entered the username instead of the id, to find out how to get the id visit the documentation --> https://github.com/redkatz/OsintTube")
    print(utility.ascii_art)
    print(menu)
    print(bcolors.OKGREEN+" Target --> "+bcolors.ENDC+InformationGathering.youtube_username(id))
    while True:
        command = input(bcolors.FAIL+"\n Run a command: "+bcolors.ENDC)
        if command == "list":
            print(command_list)
        elif command == "clear":
            os.system("clear")
            print(utility.ascii_art)
            print(utility.menu)
            print(utility.bcolors.OKGREEN+" Target --> "+bcolors.ENDC+InformationGathering.youtube_username(id))

        elif command == "description" or command == "desc":
            print("\n"+InformationGathering.youtube_description(id))
            if save == "y":
                save_text(InformationGathering.youtube_description(id), InformationGathering.youtube_username(id)+"_"+command, InformationGathering.youtube_username(id))
        elif command == "earnings" or command == "earn":
            print("\n"+InformationGathering.youtube_estimate_earnings(id))
            if save == "y":
                save_text(InformationGathering.youtube_estimate_earnings(id), InformationGathering.youtube_username(id)+"_"+command, InformationGathering.youtube_username(id))

        elif command == "joindate":
            print("\n"+InformationGathering.youtube_channel_join_date(id))
            if save == "y":
                save_text(InformationGathering.youtube_estimate_earnings(id), InformationGathering.youtube_username(id)+"_"+command, InformationGathering.youtube_username(id))
    if utility.IsId(id) == False:
        exit("Error: it seems you entered the username instead of the id, to find out how to get the id visit the documentation --> https://github.com/redkatz/OsintTube")
    print(utility.ascii_art)
    print(utility.menu)
    print(utility.bcolors.OKGREEN+" Target --> "+bcolors.ENDC+InformationGathering.youtube_username(id))
    while True:
        command = input(bcolors.FAIL+"\n Run a command: "+bcolors.ENDC)
        if command == "list":
            print(command_list)
        elif command == "clear":
            os.system("clear")
            print(utility.ascii_art)
            print(utility.menu)
            print(utility.bcolors.OKGREEN+" Target --> "+bcolors.ENDC+InformationGathering.youtube_username(id))

        elif command == "description" or command == "desc":
            print("\n"+InformationGathering.youtube_description(id))
            if save == "y":
                save_text(InformationGathering.youtube_description(id), InformationGathering.youtube_username(id)+"_"+command, InformationGathering.youtube_username(id))
        elif command == "earnings" or command == "earn":
            print("\n"+InformationGathering.youtube_estimate_earnings(id))
            if save == "y":
                save_text(InformationGathering.youtube_estimate_earnings(id), InformationGathering.youtube_username(id)+"_"+command, InformationGathering.youtube_username(id))

        elif command == "joindate":
            print("\n"+InformationGathering.youtube_channel_join_date(id))
            if save == "y":
                save_text(InformationGathering.youtube_channel_join_date(id), InformationGathering.youtube_username(id)+"_"+command, InformationGathering.youtube_username(id))

        elif command == "vidnumber":
            print("\n"+InformationGathering.youtube_video_count(id))
            if save == "y":
                save_text(InformationGathering.youtube_video_count(id), InformationGathering.youtube_username(id)+"_"+command, InformationGathering.youtube_username(id))

        elif command == "location":
            print("\n"+InformationGathering.youtube_channel_location(id))
            if save == "y":
                save_text(InformationGathering.youtube_channel_location(id), InformationGathering.youtube_username(id)+"_"+command, InformationGathering.youtube_username(id))

        elif command == "category":
            print("\n"+InformationGathering.youtube_channel_category(id))
            if save == "y":
                save_text(InformationGathering.youtube_channel_category(id), InformationGathering.youtube_username(id)+"_"+command, InformationGathering.youtube_username(id))

        elif command == "subnumber":
            print("\n"+InformationGathering.youtube_subscriber_count(id))
            if save == "y":
                save_text(InformationGathering.youtube_subscriber_count(id), InformationGathering.youtube_username(id)+"_"+command, InformationGathering.youtube_username(id))

        elif command == "views":
            print("\n"+InformationGathering.youtube_video_views_count(id))
            if save == "y":
                save_text(InformationGathering.youtube_video_views_count(id), InformationGathering.youtube_username(id)+"_"+command, InformationGathering.youtube_username(id))

        elif command == "duration":
            print("\n"+InformationGathering.youtube_video_duration(id))
            if save == "y":
                save_text(InformationGathering.youtube_video_duration(id), InformationGathering.youtube_username(id)+"_"+command, InformationGathering.youtube_username(id))

        elif "target" in command.split(" "):
            id = command.split(" ")[1]
            os.system("clear")
            print(utility.ascii_art)
            print(utility.menu)
            print(utility.bcolors.OKGREEN+" Target --> "+bcolors.ENDC+InformationGathering.youtube_username(id))
        elif "FILE" in command.split("="):
            save = command.split("=")[1]
            print("\nInfo saving = "+save)


        elif command == "vidnumber":
            print("\n"+InformationGathering.youtube_video_count(id))
            if save == "y":
                save_text(InformationGathering.youtube_video_count(id), InformationGathering.youtube_username(id)+"_"+command, InformationGathering.youtube_username(id))

        elif command == "location":
            print("\n"+InformationGathering.youtube_channel_location(id))
            if save == "y":
                save_text(InformationGathering.youtube_channel_location(id), InformationGathering.youtube_username(id)+"_"+command, InformationGathering.youtube_username(id))

        elif command == "category":
            print("\n"+InformationGathering.youtube_channel_category(id))
            if save == "y":
                save_text(InformationGathering.youtube_channel_category(id), InformationGathering.youtube_username(id)+"_"+command, InformationGathering.youtube_username(id))

        elif command == "subnumber":
            print("\n"+InformationGathering.youtube_subscriber_count(id))
            if save == "y":
                save_text(InformationGathering.youtube_subscriber_count(id), InformationGathering.youtube_username(id)+"_"+command, InformationGathering.youtube_username(id))

        elif command == "views":
            print("\n"+InformationGathering.youtube_video_views_count(id))
            if save == "y":
                save_text(InformationGathering.youtube_video_views_count(id), InformationGathering.youtube_username(id)+"_"+command, InformationGathering.youtube_username(id))

        elif command == "duration":
            print("\n"+InformationGathering.youtube_video_duration(id))
            if save == "y":
                save_text(InformationGathering.youtube_video_duration(id), InformationGathering.youtube_username(id)+"_"+command, InformationGathering.youtube_username(id))

        elif "target" in command.split(" "):
            id = command.split(" ")[1]
            os.system("clear")
            print(utility.ascii_art)
            print(utility.menu)
            print(utility.bcolors.OKGREEN+" Target --> "+bcolors.ENDC+InformationGathering.youtube_username(id))
        elif "FILE" in command.split("="):
            save = command.split("=")[1]
            print("\nInfo saving = "+save)

except IndexError:
	print("Usage: main.py <youtube id>\n")
