import os
import cv2
import json
import time
import datetime

# add or remove video formats here
VIDEO_FORMATS = ('.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv')

# path to the json file in which will be stored duration of each video
#  so we will not spend time to calculate duration again if code folder was proccessed once
CACHE_FILE = 'VideoSearcher/cache_file.json'                                           
cache = {}                          # prepare to get cache

# variables to store total amount of seconds and bytes
total_seconds = 0
total_bytes = 0

# dictionaries/objects that will save longest and largest videos
longest_video = {'path': 'None', 'duration': 0, 'size': 0}
largest_video = {'path': 'None', 'duration': 0, 'size': 0}

# dict where will be stored path to folder and amount of videos in it as a key:value
most_videos = {}

# set to track visited folders
visited_folders = set()

if os.path.exists(CACHE_FILE):                      # check if file exsists before opening it
    try:
        with open(CACHE_FILE, 'r') as f:
            cache = json.load(f)                        # get data and save it in prepared variable
    except:
        cache = {}

# function to iterate throught all subfolders of given folder
#  parameters: 
#               fodler: path to start folder
#               videos_per_folder: needed amount of videos in folder to log it
#               logging: log path of each video on console or not
def iterate_dir(folder, videos_per_folder=10, logging=False):
    if folder in visited_folders:       # 'skip' folder if it was visited
        return []
    
    visited_folders.add(folder)         # add in set if it was not visited

    # array that will stores all videofiles's path that will be founded
    folder_videos = []

    videos_in_folder = 0

    # try to open folder
    try:
        elements_in_folder = os.listdir(folder)     # get all elements of current folder

        for element in elements_in_folder:                      # iterate throught all elements in that folder
            element_path = os.path.join(folder, element)            # get path of element

            if os.path.isfile(element_path) and os.path.splitext(element_path)[-1] in VIDEO_FORMATS:        # check if file is video
                if logging:                                 
                    print(f'Finded Video: {element_path}')          # print video's path on console if logging
                folder_videos.append(element_path)                  # add duration of current video in folder_videos array
                videos_in_folder += 1

        # add folder in dict if it has needed amount of videos
        if videos_in_folder >= videos_per_folder:                       
            most_videos[folder] = videos_in_folder
            
        # iterate throught same folder again,
        #   now start finding videos in subfolders using recursion
        for element in elements_in_folder:
            element_path = os.path.join(folder, element)                # get path of element

            if os.path.isdir(element_path):                                 # check if it is folder/directory
                subfolder_videos = iterate_dir(element_path, videos_per_folder, logging)    # call iterate_dir and start searching recursively
                folder_videos.extend(subfolder_videos)                      # add all paths that were found to the parent folder 

    # skip folder if permission denied
    except PermissionError as e:
        print(f'Error While Opening Folder: {e}')

    return folder_videos

# function to get duration of video in seconds
#  parameters:
#               file_path: path to actual video
def get_duration(file_path):
    # get absolute path of video
    absolute_path = os.path.abspath(file_path)

    if absolute_path in cache:                      # get duration of video from cache if it was proccessed earlier(if it's path is in cache)
        return cache[absolute_path]

    video = cv2.VideoCapture(file_path)                 # process video using opencv

    frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)       # get total frames of video
    fps = video.get(cv2.CAP_PROP_FPS)                       # get fps(Frame Per Second) of video

    # try to calculate duration
    try:
        duration = int(frame_count/fps)
        cache[absolute_path] = duration
        return duration
    
    # return 0 if zero division error
    except ZeroDivisionError:
        cache[absolute_path] = 0
        return 0

# function to proccess video anf get info from it
#  parameters:
#               file_path: path to actual video
def proccess_video(file_path):
    global total_seconds, total_bytes, longest_video, largest_video
    # try to proccess folder
    try:

        # get duration and size of video in seconds and bytes
        video_duration = get_duration(file_path)
        video_size = os.path.getsize(file_path)

        # add info to the total seconds and bytes variables
        total_seconds += video_duration
        total_bytes += video_size

        # reasing longest video object if new longest video were found
        if video_duration > longest_video['duration']:
            longest_video = {'path': file_path, 'duration': video_duration, 'size': video_size}

        # reasing largest video object if new largest video were found
        if video_size > largest_video['size']:
            largest_video = {'path': file_path, 'duration': video_duration, 'size': video_size}
    
    # log error on console if any error
    except PermissionError as e:
        print(f'Error While Proccessing: \n{file_path}\n{e}')

# simple function to convet seconds into more human like format
def convert_seconds(seconds):
    return datetime.timedelta(seconds=seconds)

# simple function to convet bytes into more human like format
def convert_bytes(bytes):
    if bytes < 1024: return f'{bytes} B'
       
    elif bytes < 1024*2: return f'{bytes / 1024:.2f} KB'
        
    elif bytes < 1024**3: return f'{bytes / (1024**2):.2f} MB'
        
    else: return f'{bytes / (1024**3):.2f} GB'

if __name__ == '__main__':
    
    main_folder = input('Please enter path of folder to find videos: ')     # get start path

    # track and calculate estimated time to search videos
    code_start_time = time.time()

    videos_list = iterate_dir(main_folder, videos_per_folder=1, logging=True)         # search videos

    time_searched = time.time() - code_start_time

    print(f'Founded {len(videos_list)} Videos. Proccessing!')

    # track and calculate estimated time to proccess videos
    proccessing_start_time = time.time()

    for video_path in videos_list:
        proccess_video(video_path)

    time_proccessed = time.time() - proccessing_start_time

    print(f'Proccessing Done!')

    # calculate averages of duration and size
    average_duration = int(total_seconds/len(videos_list)) if videos_list else 0
    average_size = int(total_bytes/len(videos_list)) if videos_list else 0

    # ask user if he wants to clear terminal
    answ = input('Clear Terminal?[n if no]: ').lower()

    if answ != 'n':
        os.system('clear')  

    # track and calculate estimated time to save cache
    cache_start_time = time.time()

    with open(CACHE_FILE, 'w') as f:
        json.dump(cache, f)

    time_cache_saved = time.time() - cache_start_time

    print('-----------------INFO-----------------')

    print(f'Total Time Code Worked: {time_searched + time_proccessed + time_cache_saved:.2f}')
    print(f'Time to Search Videos: {time_searched:.2f}')
    print(f'Time to Proccess Videos: {time_proccessed:.2f}')
    print(f'Time to Save Cache: {time_cache_saved:.2f}')
    print(f'Total Videos: {len(videos_list)}')
    print(f'Total Duration: {convert_seconds(total_seconds)}')
    print(f'Total Size: {convert_bytes(total_bytes)}')
    print(f'Average Duration: {convert_seconds(average_duration)}')
    print(f'Average Size: {convert_bytes(average_size)}')
    print('Most Videos In:')
    for name, count in sorted(most_videos.items(), key=lambda x: len(x[0])):
        print(f'{name} : {count} videos')

    print('-------------LONGEST VIDEO------------')
    print(f'Video Name: {os.path.basename(longest_video['path'])}')
    print(f'Video Path: {longest_video['path']}')
    print(f'Video Duration: {convert_seconds(longest_video['duration'])}')
    print(f'Video Size: {convert_bytes(longest_video['size'])}')

    print('-------------LARGEST VIDEO------------')
    print(f'Video Name: {os.path.basename(largest_video['path'])}')
    print(f'Video Path: {largest_video['path']}')
    print(f'Video Duration: {convert_seconds(largest_video['duration'])}')
    print(f'Video Size: {convert_bytes(largest_video['size'])}')

    # ask user if he wants to save info as a json file
    save_answ = input('Save Information into the json file?[y if yes]: ').lower()

    if save_answ == 'y':

        # iterate throught both dictionaries
        for video_info in (longest_video, largest_video):
            # format duration and size of each object/dict
            video_info['duration'] = str(convert_seconds(video_info['duration']))
            video_info['size'] = convert_bytes(video_info['size'])

        # create dict with all output information
        output_info = {
                'total_videos': len(videos_list),
                'total_duration': convert_seconds(total_seconds),
                'total_size': convert_bytes(total_bytes),
                'longest_video': longest_video,
                'largest_video': largest_video,
                'average_duration': convert_seconds(average_duration),
                'average_size': convert_bytes(average_size)
        }

        # create new json file and write info on it
        with open('VideoSearcher/search_information.json', 'w') as f:
            json.dump(output_info, f, indent=4)