secret_digit="4"
guess=""
try_limit = 3
try_count= 0
out_of_try = False
while guess != secret_digit and not(out_of_try):
    if try_count < try_limit:
     guess = input("enter guess: ")
     try_count += 1
    else:
        out_of_try = True
if out_of_try :
  print("you lose")
else:
 print("you win")