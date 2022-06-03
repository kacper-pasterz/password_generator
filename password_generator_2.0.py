import random
import string

# predfined password's lenght is 10

password = "".join((random.choice(string.ascii_letters + string.punctuation + string.digits) for _ in range(10)))

print("\n"+password+"\n")