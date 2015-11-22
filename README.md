# ics2task

A CLI tool to create ICS (RFC5455) event into task in TaskWarrior

## Install

    #> git clone https://github.com/Spredzy/ics2task.git
    #> cd ics2task
    #> python setup.py install

## Example

    #> ics2task /path/to/ics/file.ics
    #> task project:ics2task

or

    #> cat /path/to/ics/file.ics | ics2task
    #> task project:ics2task
