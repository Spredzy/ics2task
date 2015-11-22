# Copyright 2015 Yanis Guenane  <yanis@guenane.org>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from icalendar import Calendar
from ics2task import utils
from taskw import TaskWarrior

import fileinput
import sys


def _build_annotation(event):

    possible_items = ['LOCATION', 'SUMMARY', 'ATTENDEE', 'DESCRIPTION']
    annotation = '\n\n'

    for item in possible_items:
        if item == 'ATTENDEE':
            annotation += '%s: %s\n' % (item.capitalize(),
                                        ', '.join(str(x) for x in event[item]))
        else:
            annotation += '%s: %s\n' % (item.capitalize(), event[item])

    annotation += '\n'

    return annotation


def taskerize(tw, event):
    """Create a new task for an iCalendar event"""
    if event['ORGANIZER']:
        organizer = ' (%s)' % event['ORGANIZER']
    else:
        organizer = ''

    tid = tw.task_add('%s%s' % (event['SUMMARY'], organizer),
                      project='ics2task', due=event['DTSTART'].dt)

    _build_annotation(event)
    tw.task_annotate(tid, _build_annotation(event))


def _parse_event(event):
    """Parse event"""
    formatted_event = {
        'ATTENDEE': [],
        'DESCRIPTION': None,
        'DTSTART': None,
        'LOCATION': None,
        'ORGANIZER': None,
        'SUMMARY': None,
    }

    for item in formatted_event.keys():
        if item in event:
            if item == 'ATTENDEE':
                for attendee in event[item]:
                    formatted_event[item].append(utils._clean_string(attendee))
            elif item == 'DTSTART':
                formatted_event[item] = event[item]
            else:
                formatted_event[item] = utils._clean_string(event[item])

    return formatted_event


def parse_input():
    """Parse input and return array of calendar

    A user can either pass the calendar via the stdin or via one or several
    icalendar files. This method will parse the input and return an array
    of valid icalendar
    """
    input_data = ''
    calendars = []

    for line in fileinput.input():
        if 'BEGIN:VCALENDAR' in line:
            calendars.append(input_data)
            input_data = line
        else:
            input_data += line
    calendars.append(input_data)

    return calendars[1:]


def main():
    tw = TaskWarrior()

    raw_calendars = parse_input()
    for raw_calendar in raw_calendars:
        calendar = Calendar.from_ical(raw_calendar)
        for event in calendar.subcomponents:
            l_event = _parse_event(event)
            taskerize(tw, l_event)
