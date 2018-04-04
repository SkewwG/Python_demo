import asyncio

print(dir(asyncio))
methods = ['ALL_COMPLETED', 'AbstractEventLoop', 'AbstractEventLoopPolicy', 'AbstractServer', 'BaseEventLoop',
           'BaseProtocol', 'BaseTransport', 'BoundedSemaphore', 'CancelledError', 'Condition', 'DatagramProtocol',
           'DatagramTransport', 'DefaultEventLoopPolicy', 'Event', 'FIRST_COMPLETED', 'FIRST_EXCEPTION', 'Future',
           'Handle', 'IncompleteReadError', 'InvalidStateError', 'IocpProactor', 'JoinableQueue', 'LifoQueue', 'Lock',
           'PriorityQueue', 'ProactorEventLoop', 'Protocol', 'Queue', 'QueueEmpty', 'QueueFull', 'ReadTransport',
           'SelectorEventLoop', 'Semaphore', 'StreamReader', 'StreamReaderProtocol', 'StreamWriter', 'SubprocessProtocol',
           'SubprocessTransport', 'Task', 'TimeoutError', 'TimerHandle', 'Transport', 'WriteTransport', '__all__',
           '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__',
           '__spec__', '_overlapped', 'as_completed', 'async', 'base_events', 'base_subprocess', 'constants', 'coroutine',
           'coroutines', 'create_subprocess_exec', 'create_subprocess_shell', 'events', 'futures', 'gather',
           'get_child_watcher', 'get_event_loop', 'get_event_loop_policy', 'iscoroutine', 'iscoroutinefunction', 'locks',
           'log', 'new_event_loop', 'open_connection', 'proactor_events', 'protocols', 'queues', 'selector_events',
           'selectors', 'set_child_watcher', 'set_event_loop', 'set_event_loop_policy', 'shield', 'sleep', 'sslproto',
           'start_server', 'streams', 'subprocess', 'sys', 'tasks', 'transports', 'wait', 'wait_for', 'windows_events',
           'windows_utils', 'wrap_future']

print(help(asyncio.get_event_loop))