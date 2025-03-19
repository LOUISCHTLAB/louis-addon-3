import aioesphomeapi
import asyncio
from aioesphomeapi import APIConnectionError
# Thông tin kết nối ESPHome
HOST = "learn-ir-remote.local"
PORT = 6053
PASSWORD = "123123"  # Password gốc (nếu không dùng mã hóa)
NOISE_PSK = "1234567890MOHc8KPqk+xlHxC9jvSSjnz47uIcnvNpw="  # Thay bằng Noise PSK thực tế từ ESPHome

async def main():
    """Connect to an ESPHome device and wait for state changes."""
        # Tạo client API
    cli = aioesphomeapi.APIClient(
        address=HOST,
        port=PORT,
        password=PASSWORD,  # Dùng password nếu không có mã hóa
        noise_psk=NOISE_PSK if NOISE_PSK else None  # Dùng Noise PSK nếu thiết bị yêu cầu mã hóa
    )

    await cli.connect(login=True)

    def change_callback(state):
        """Print the state changes of the device.."""
        print(state)

    # Subscribe to the state changes
    cli.subscribe_states(change_callback)

loop = asyncio.get_event_loop()
try:
    asyncio.ensure_future(main())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    loop.close()