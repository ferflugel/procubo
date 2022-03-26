from openrgb import OpenRGBClient
from openrgb.utils import RGBColor, DeviceType

client = OpenRGBClient()

client.clear()  # Turns everything off
motherboard = client.get_devices_by_type(DeviceType.MOTHERBOARD)[0]

motherboard.set_color(RGBColor(0, 255, 0))
