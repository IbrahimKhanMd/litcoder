def test_devices():
  given_time = int(input())
  devices = int(input())
  if given_time < 4:
    return "Invalid Input"
  devices_tested = given_time// 4
  remaining_devices = devices - devices_tested
  return devices_tested, remaining_devices

print(test_devices())

