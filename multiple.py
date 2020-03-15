from pytube import YouTube

video_list = ( "https://www.youtube.com/watch?v=28W26QfiESs",xyz)
for i in video_list:
    yt = YouTube(i)
    dw = yt.streams.first()
    dw.download("E:/")
