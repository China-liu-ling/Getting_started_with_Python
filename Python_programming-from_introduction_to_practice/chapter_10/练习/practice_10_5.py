while True:
    reason = input("Why do you like programming? (q to quit): ")
    if reason == 'q':
        break
    with open('reasons.txt', 'a') as f_0:
        f_0.write(f"{reason}\n") 