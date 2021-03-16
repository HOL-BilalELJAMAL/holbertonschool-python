#!/usr/bin/python3
import sys
import traceback

def trace_calls(frame, event, arg):
    if event != 'call': # We only want function calls!
        return
    co = frame.f_code
    func_name = co.co_name
    if func_name != FUNCTION: # We only want function calls of THIS function
        return
    func_line_no = frame.f_lineno
    func_filename = co.co_filename
    caller = frame.f_back
    caller_line_no = caller.f_lineno
    caller_filename = caller.f_code.co_filename
    if 'main' in caller_filename: # Ignore any calls made in the main
        return
    sys.stderr.write('Call to {} on line {} of {} from line {} of {}\n'
                     .format(func_name,
                             func_line_no,
                             func_filename,
                             caller_line_no,
                             caller_filename))

if __name__ == '__main__':
    count_words = __import__(sys.argv[3]).count_words
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'"
              .format(sys.argv[0]))
    else:
        if len(sys.argv) == 5:
            FUNCTION = sys.argv[4]
            sys.settrace(trace_calls)
        result = count_words(sys.argv[1], [x for x in sys.argv[2].split()])
