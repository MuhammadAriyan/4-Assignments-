import time

def countdown(t):
    while t:
        mins,secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('Time is up!')
print('Countdown Timer')


countdown(int(timeinput:=input('Enter the Time in seconds: ')))
print('Time:', time, 'seconds')
print('Countdown started!')