
class Video:
    def __init__(self,views=0, likes=100, subscribers= None, is_published=True):
        self.views = views
        self.likes = likes
        self.subscribers = subscribers if subscribers is not None else[]
        self.is_published = is_published

    def subscribe(self):
        print("Vy uspeshno podpisyny")


my_video = Video()
Aleks_video = Video(views=10, likes=500, subscribers=['podpischik1''podpischik2'], is_published=True)
Maksim_video = Video(views=45, likes=700, subscribers=["podpischik3"], is_published=False)
my_video.subscribe()
Aleks_video.subscribe()
Maksim_video.subscribe()


