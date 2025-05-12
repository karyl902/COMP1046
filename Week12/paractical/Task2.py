#Academix Integrity statement
#Name: Zhenyi He
#Student ID: 521332
#Email: 521332@learning.eynesbury.edu.au
#This program is my own work as defined by the Academic Integrity

class NewspaperHeadlines:
    def __init__(self):
        self.headlines = []
        self.subscribers = []

    def latestHeadline(self):
        return self.headlines[-1]

    def addHeadline(self, headline):
        self.headlines.append(headline)
        self.notifySubscribers()

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def notifySubscribers(self):
        latest_headline = self.latestHeadline()
        for subscriber in self.subscribers:
            subscriber.update(latest_headline)


class NewspaperSubscriber:
    def __init__(self, newspaper):
        self.newspaper = newspaper
        self.newspaper.subscribe(self)

    def update(self, headline):
        print(f"New Headline: {headline}")


h = NewspaperHeadlines()
s = NewspaperSubscriber(h)
h.addHeadline("Severe weather warning for tomorrow.")
h.addHeadline("Sever weather warning cancelled.")
    