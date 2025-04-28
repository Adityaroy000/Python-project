import json
import os
def load_data():
    # you have used try catch here bcz you needed a empty list if no any file is found
    try:
        curr_dir = os.path.dirname(__file__)
        file_path = os.path.join(curr_dir,"youtube.txt")
        with open(file_path,'r') as file:
            #here you will use json's "load" method , which goes in file and convert the data from string into json
            return json.load(file) 
    except FileNotFoundError:
        return []
    
def save_data_helper(video):
    # here you are not using try catch block
    curr_dir = os.path.dirname(__file__)
    file_path = os.path.join(curr_dir,"youtube.txt")
    with open(file_path,'w') as file:
        # here i will use jason's dump method ,which writes the data in given file. It takes two parameter: i) what to write ii) where to write
        json.dump(video,file)

def list_allVideos(video):
    # here you will use enumerate() so that it will list the videos according to its indexing
    print("\n")
    print("*" * 70)
    if not video:
        print("You do not have any youtube video listed yet! Add first.")
        
    for index,vid in enumerate(video,start = 1): #indexing will start with 1 not 0
        print(f"{index}. Video name: {vid['name']},Duration: {vid['time']}")
    print("\n")
    print("*" * 70)

def add_video(video):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    video.append({"name": name, "time": time}) #Appends (adds) this dictionary to the list called video
    save_data_helper(video)

def update_video(video):
    list_allVideos(video)
    index = int(input("Enter video number to update: "))
    if 1<=index <=len(video):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        video[index-1] = {'name':name,'time':time}
        save_data_helper(video)
    else:
        print("Invalid index selected")

def delete_video(video):
    list_allVideos(video)
    index = int(input("Enter the video number to be deleted: "))

    if 1<=index<=len(video):
        del video[index-1]
        save_data_helper(video)
    else:
        print("Invalid video index selected")

def main():
    video = load_data()
    while True:
        print("\nYoutube Manager | choose an option ")
        print("1. List all youtube video")
        print("2. Add a Youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")

        choice = input("Enter you choice: ")

        match choice:
            case '1':
                list_allVideos(video)
            case '2':
                add_video(video)
            case '3':
                update_video(video)
            case '4':
                delete_video(video)
            case '5':
                break
            case _:
                print("Invalid choice")

# this is used so that if there is any main function defined then it will get called and your application will start its execution from main function
if __name__ == "__main__":
    main() 