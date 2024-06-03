import feedparser
from ics import Calendar, Event
from dateutil.parser import parse

# http://www.uq.edu.au/events/rss/event_all_feed.php?cid=16
# http://www.uq.edu.au/events/rss/event_all_feed.php?cid=3

def main():
    uq_academic_calendar_rss = "http://www.uq.edu.au/events/rss/event_all_feed.php?cid=16"
    feed = feedparser.parse(uq_academic_calendar_rss)

    cal = Calendar()
    for entry in feed.entries:
        event = Event()
        event.name = entry.title
        event.begin = parse(entry.published)
        event.make_all_day()

        # print(entry.published+"\t"+entry.title)

        cal.events.add(event)

    with open('UQ Academic Calendar.ics', 'w') as f:
        f.write(cal.serialize())
    
if __name__ == "__main__":
    main()