class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        """
        метод start переработан в соответствии с доп. заданием
        """
        finishers = {}
        place = 1

        while self.participants:
            winers = {}  # содержит словарь победителей, пришедших одновременно
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    winers[participant.speed] = participant  # в роли ключа используем скорость участника

            if len(winers) == 1:  # условия для одного победителя
                finishers[place] = winers.pop(max(winers))
                self.participants.remove(finishers[place])
                place += 1
            elif len(winers) > 1:   # условия для нескольких победителей, побеждает тот
                while winers:       # чья скорость (ключ словаря) выше
                    finishers[place] = winers.pop(max(winers))
                    self.participants.remove(finishers[place])
                    place += 1
        return finishers

    # def start(self):  # оригинальная функция с GitHub
    #     finishers = {}
    #     place = 1
    #     while self.participants:
    #         for participant in self.participants:
    #             participant.run()
    #             if participant.distance >= self.full_distance:
    #                 finishers[place] = participant
    #                 place += 1
    #                 self.participants.remove(participant)
    #     return finishers
