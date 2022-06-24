from pytube import YouTube

while True:
    URL = input("Input a url:\n")
    video = YouTube(URL)

    print("Title:" + video.title)

    video = video.streams.get_highest_resolution()

    Ans = input("Would you like to download this video [Y/n]")
    if Ans == "Y".lower():
        video.download()
    elif Ans == "N".lower():
        exit()
    else:
        print("invalid answer")

