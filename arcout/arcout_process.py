arcout_file = open("C:\\Users\luq\Desktop\\arcout\\arctest-c.txt", "r+")
arcout_file_modified = open("C:\\Users\luq\Desktop\\arcout\\arcout_modified.txt", "w")

counter = 0

for account in arcout_file:
    account_splitted = account.split(',')
    if account_splitted[4].startswith('"SWISS-DD"') \
        or account_splitted[4].startswith('"SWISS-DD-2"'):
            print("ok")
            counter += 1
            arcout_file_modified.write(account)
    else:
        print("not ok")

print(counter)
arcout_file.close()
arcout_file_modified.close()
