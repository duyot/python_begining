

try:
    streams = open("Test.py")
    for item in streams:
        print("Item: " + item)
    streams.close()
    print()
    with open("Test.py") as row:
        print(row.read())
    #item = 1/0
except Exception as ex:
    print(ex)
    # streams.close()
    # err = sys.exc_info()
    # for i in err:
    #     print(i)
# except OSError as error:
#     print(str(error))
