print(format("Miles", "<13s"), format("Kilometers", "<13s") + "|   " +
      format("Kilometers", "<13s"), format("Miles", "<13s"))
for i in range(1,11):
    print(format(i, "<13d"), format(1.609 * i, "<13.3f") + "|   " +
          format(5 * i + 15, "<13d"), format((5 * i + 15) * 0.6215, "<13.3f"))
