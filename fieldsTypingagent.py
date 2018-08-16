#!/usr/bin/env python3
'''Field lists for Typingagent CSV upload files and must be
in the same folder as uploadTypingagent.py for it to function.
Running this alone prints a list of all fields to the terminal.
'''
def typingagentFields():
    #Required: 'location_id', 'location_name'
    fields = ['Class Code', 'Username', 'Last Name',
                'First Name', 'Password', 'Grade', 'Tag 1',
                'Tag 2', 'Action']
    return fields


def main():
    #Prints the fiels list to the terminal window one per line.
    print()
    print('Typingagent Fields')
    for field in typingagentFields():
        print(field)
    print()
    return

if __name__ == '__main__': main()
