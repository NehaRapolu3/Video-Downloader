from pytube import YouTube
yt = YouTube("https://youtu.be/YuyrSDGk3N0")
#dw = yt.streams.get_by_itag(18)
#dw.download("E:/")
print(yt.streams.filter(only_audio=True).all())
