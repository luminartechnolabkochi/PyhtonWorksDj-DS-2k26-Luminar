



file_path="Errorhandling\\abc.txt"


try:
    fr= open(file_path,"r")

    for line in fr:

        print(line)
except Exception as e:
    
    print(e)

finally:
    fr.close()
print("db commit")

print("send email")
