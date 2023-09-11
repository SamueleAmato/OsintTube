from cmd import InformationGathering
import os
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    GREY = '\033[90m'



def IsId(id):
    if len(id) == 24:
        return True
    else:
        return False


ascii_art = bcolors.FAIL+r'''
   ___      _       _  _____      _          
  / _ \ ___(_)_ __ | ||_   _|   _| |__   ___ 
 | | | / __| | '_ \| __|| || | | | '_ \ / _ \
 | |_| \__ \ | | | | |_ | || |_| | |_) |  __/
  \___/|___/_|_| |_|\__||_| \__,_|_.__/ \___|

 version 0.0.1 - Developed by RedKatz'''+bcolors.ENDC


menu = f'''
 Type {bcolors.OKCYAN}'list'{bcolors.ENDC} to show all alloweds commands
 Type {bcolors.OKCYAN}'FILE=y'{bcolors.ENDC} to save results to files like {bcolors.OKCYAN}'<target username>_<command>.txt'{bcolors.ENDC}
 Type {bcolors.OKCYAN}'FILE=n'{bcolors.ENDC} to disable saving to files
''' 

command_list = f'''
- description   :{bcolors.GREY}Get the channel description{bcolors.ENDC}
- location      :{bcolors.GREY}Get the channel location{bcolors.ENDC}
- vidnumber     :{bcolors.GREY}Get the total number of channel videos{bcolors.ENDC}
- subnumber     :{bcolors.GREY}Get the number of subscribers {bcolors.ENDC}
- views         :{bcolors.GREY}Get the total number of channel views{bcolors.ENDC}
- duration      :{bcolors.GREY}Get the estimed video duration{bcolors.ENDC}
- joindate      :{bcolors.GREY}Get the channel join date{bcolors.ENDC}
- category      :{bcolors.GREY}Get the channel categoty{bcolors.ENDC}
- earnings      :{bcolors.GREY}Get the estimated value of the channel's earnings in one month{bcolors.ENDC}
- target <id>   :{bcolors.GREY}Set a new target{bcolors.ENDC}'''

def main(id):
    if IsId(id) == False:
        exit("Error: it seems you entered the username instead of the id, to find out how to get the id visit the documentation --> https://github.com/redkatz/OsintTube")
    print(ascii_art)
    print(menu)
    print(bcolors.OKGREEN+" Target --> "+bcolors.ENDC+InformationGathering.youtube_username(id))
    while True:
        command = input(bcolors.FAIL+"\n Run a command: "+bcolors.ENDC)
        if command == "list":
            print(command_list)
        elif command == "clear":
            os.system("clear")
            print(ascii_art)
            print(menu)
            print(bcolors.OKGREEN+" Target --> "+bcolors.ENDC+InformationGathering.youtube_username(id))

        elif command == "description" or command == "desc":
            print("\n"+InformationGathering.youtube_description(id))
        elif command == "earnings" or command == "earn":
            print("\n"+InformationGathering.youtube_estimate_earnings(id))
        elif command == "joindate":
            print("\n"+InformationGathering.youtube_channel_join_date(id))
        elif command == "vidnumber":
            print("\n"+InformationGathering.youtube_video_count(id))
        elif command == "location":
            print("\n"+InformationGathering.youtube_channel_location(id))
        elif command == "category":
            print("\n"+InformationGathering.youtube_channel_category(id))
        elif command == "subnumber":
            print("\n"+InformationGathering.youtube_subscriber_count(id))
        elif command == "views":
            print("\n"+InformationGathering.youtube_video_views_count(id))
        elif command == "duration":
            print("\n"+InformationGathering.youtube_video_duration(id))
        elif "target" in command.split(" "):
            id = command.split(" ")[1]
            os.system("clear")
            print(ascii_art)
            print(menu)
            print(bcolors.OKGREEN+" Target --> "+bcolors.ENDC+InformationGathering.youtube_username(id))

        else:
            print("\ncommand not found tipe list")
