# async_trendymanga.py
async library for trendymanga.com
![20240101_132851](https://github.com/aminobotskek/trendymanga/assets/94906343/7fe07e64-2749-443e-b5da-8f93c1287567)
# Install
```
git clone https://github.com/aminobotskek/async_trendymanga
```

### Example
```python3
import async_trendymanga
import asyncio
async def main():
	client=async_trendymanga.AsyncTrendymanga()
	await client.login(email="", password="")
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
