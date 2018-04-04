# new_event_loop

import asyncio
new_loop = asyncio.new_event_loop()
new_loop.call_soon_threadsafe()