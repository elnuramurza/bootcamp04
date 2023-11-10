class Video:
    views_count = 0
    likes = 100
    subscribe = []
    is_published = True
    def __init__(self,video_name, is_published =True):
        self.name = video_name
        self.is_published = is_published
    def watch(self):
        self.views_count +=1
    def subscribe(self,  human_object):
        self.subscribers.append(human_object)
        
class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age   
    def __repr__(self):
        return self.name
        #video obiekti
    a_am_at_zoo = Video("I zoo") 
    video_2 = Video('urok 16. konstruktor') 
    #podpisvaemza
    asan  

