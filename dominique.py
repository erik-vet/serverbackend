import webbrowser

def open_youtube_link(link):
    webbrowser.open(link)
    return "is geopend"

youtube_link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
open_youtube_link(youtube_link)