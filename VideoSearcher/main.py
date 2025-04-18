import os, cv2, datetime

# variables to store total amount of seconds and videos
total_seconds = 0
total_videos = 0

# dict where will be stored path to folder and amount of videos in it as a key:value
most_videos = {}

# function to iterate throught all subfolders of given folder
#  parameters: 
#               fodler: path to start folder
#               videos_per_folder: needed amount of videos in folder to log it
#               logging: log path of each video on console or not
def iterate_dir(folder, videos_per_folder=10, logging=False):
    global total_seconds, total_videos

    videos_in_folder = 0

    # try to open folder
    try:
        elements_in_folder = os.listdir(folder)     # get all elements of current folder

        for element in elements_in_folder:                      # iterate throught all elements in that folder
            element_path = os.path.join(folder, element)            # get path of element

            if os.path.isfile(element_path):                        # check if it is file
                if element_path.endswith('.mp4'):                       # check if file is video
                    if logging:                                 
                        print(element_path)                             # print video's path on console if logging

                    total_seconds += get_duration(os.path.abspath(element_path))    # add duration of current video in total_seconds variable
                    videos_in_folder += 1
                    total_videos += 1

        # add folder in dict if it has needed amount of videos
        if videos_in_folder >= videos_per_folder:                       
            most_videos[folder] = videos_in_folder
            
        # iterate throught same folder again,
        #   now start finding videos in subfolders using recursion
        for element in elements_in_folder:
            element_path = os.path.join(folder, element)                # get path of element

            if os.path.isdir(element_path):                                 # check if it is folder/directory
                iterate_dir(element_path, videos_per_folder, logging)           # call iterate_dir and start searching recursively

    # skip folder if permission denied
    except PermissionError:
        pass

# function to get duration of video in seconds
#  parameters:
#               file_path: path to actual video
def get_duration(file_path):
    video = cv2.VideoCapture(file_path)                 # process video using opencv

    frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)       # get total frames of video
    fps = video.get(cv2.CAP_PROP_FPS)                       # get fps(Frame Per Second) of video

    # try to calculate duration
    try:
        return int(frame_count/fps)
    
    # return 0 if zero division error
    except ZeroDivisionError:
        return 0

if __name__ == '__main__':
    # get start path
    main_folder = input('Please enter path of folder to find videos: ')

    # search videos
    iterate_dir(main_folder, videos_per_folder=1, logging=True)

    # convert seconds into more human like format
    converted_seconds = datetime.timedelta(seconds=total_seconds)

    # ask user if he wants to clear terminal
    answ = input('Clear Terminal?[n if no]: ').lower()

    if answ != 'n':
        os.system('clear')  

    # log info on console
    print('-----------------INFO-----------------')

    print(f'Total Videos: {total_videos} | All Videos Total Duration: {converted_seconds} | In Seconds: {total_seconds}s')

    print('Most Videos In:')

    # sort dict by length of its keys and print folder : video amount
    for name, count in sorted(most_videos.items(), key=lambda x: len(x[0])):
        print(f'{name} : {count} videos')
