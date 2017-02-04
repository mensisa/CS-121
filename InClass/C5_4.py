print(format("Miles", "<15s"), format("Kilometers", "<15s"))
for i in range(1,11):
    print(format(i, "<15d"), format(1.609 * i, "<15.3f"))