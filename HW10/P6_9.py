def footToMeter(foot):
    return 0.305 * foot


def meterToFoot(meter):
    return meter / 0.305


print(format("Feet", "<10s"), format("Meters", "<10s") + "|\t",
      format("Meters", "<10s"), format("Feet", "<10s"), end="\n")
for i in range(1, 11):
    print(format(i, "<10.1f"), format(footToMeter(i), "<10.3f") + "|\t",
          format(5 * i + 15, "<10.1f"), format(meterToFoot(5 * i + 15), "<10.3f"))