import time 
seconds = int(input("Enter the time in Seconds : "))

while seconds > 0:
    print(seconds)
    time.sleep(1.5)  # Wait for 1 second
    seconds -= 1

print("Time is Up...")
