import time 

def start_stopwatch():
    start_time = time.time()
    input("Stopwasth started press enter to play")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(elapsed_time)

print("Welcome ro thle Python Stopwatch!")

while True:
    print("\nOptions")
    print("1 Start")
    print("2 exit")

    choice = input("Enter your choice (1-2): ")

    if choice == "1":
        print(f"Elapsed Time: {start_stopwatch()}")
    elif choice == "2":
        print("Exiting the stopwatch. Goodbye!")
        break
    else:
        print("Envalid choice. Please enter 1 or 2")