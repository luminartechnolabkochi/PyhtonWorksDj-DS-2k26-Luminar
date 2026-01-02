"""
✅ 3. Login System with Password and OTP

Task:
Ask for password.

If password is correct:

Ask for OTP

If OTP is correct → "Login successful"

Else → "Incorrect OTP"


Else → "Incorrect password"

"""

db_password ="access123"

db_otp=567

password = input("enter password")

if password==db_password:

    otp=int(input("enter otp"))

    if otp == db_otp:

        print("success")

    else:

        print("incorrect otp")

else:

    print("incorrect password")


# looping

    #while
    #for




