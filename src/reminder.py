from dateutil.parser import parse


class PrefixedReminder:
    """This class acts as a base class for other types of reminders.
    Classes that subclass it should override the `self.text` property
    """

    def __init__(self, date: str, time: str, prefix="Hey, don't forget to "):
        self.prefix = prefix
        self.text = prefix + '<placeholder_text>'
        self.date = parse(f'{date} {time}')
        self.time = self.date.time()



class PoliteReminder(PrefixedReminder):
    def __init__(self, text, time: str, date: str):
        super().__init__(date, time, prefix='Please remember to: ')
        self.text = self.prefix + text

    def __iter__(self):
        return iter([self.text,
                     self.date.strftime("%d/%m/%Y"),
                     self.time.strftime('%H:%M %p')])

