import asyncio


async def foo():
    return 42


async def bar():
    return 55


async def main():
    task = set()
    task.add(asyncio.create_task(foo()))
    task.add(asyncio.create_task(bar()))
    done, pending = await asyncio.wait(task, return_when=asyncio.FIRST_COMPLETED)

    print(done)
    print(pending)
    print(task)


asyncio.run(main())
