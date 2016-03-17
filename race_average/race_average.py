import re


class RaceAverage(object):

    @staticmethod
    def average(times):
        if not isinstance(times, list):
            raise TypeError('times must be a list')

        if 0 == len(times) or len(times) >= 50:
            raise ValueError('times length out of range')

        times_length = len(times)
        regex = re.compile(r"^[0-1][0-9]:[0-5][0-9] (A|P)M, DAY [1-9][0-9]?$")
        minutes = 0

        for time in times:
            if not isinstance(time, str) or regex.match(time) is None:
                raise ValueError('invalid string time format')

            minutes += RaceAverage._time_to_minutes(time)

        avg_minutes = minutes / times_length

        if minutes / float(times_length) - avg_minutes >= .5:
            avg_minutes += 1

        return avg_minutes

    @staticmethod
    def _time_to_minutes(time):
        parts = time.split(', ')
        clock_part = parts[0]
        day_part = parts[1]
        parts = clock_part.split(' ')
        period = parts[1]
        parts = parts[0].split(':')
        hour = int(parts[0]) if parts[0] != '12' else 0
        minute = int(parts[1])
        day = int(day_part.split(' ')[1])

        total_minutes = -480
        total_minutes += 720 if period == 'PM' else 0
        total_minutes += int(minute)
        total_minutes += int(hour) * 60
        total_minutes += (day - 1) * 60 * 24

        # assumption: 1 min is the fastest time possible
        if not total_minutes > 0:
            raise ValueError("time was an early start")

        return total_minutes




