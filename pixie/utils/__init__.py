import ujson

import aiohttp

from .errors import FailedHaste

# Our setup file
with open('../setup.json') as file:
    setup_file = ujson.load(file)

# Our user agent
user_agent = "Pixie (https://github.com/GetRektByMe/Pixie)"


async def hastebin(data: str):
    """
    data (str): The data wanted in the hastebin document
    """
    with aiohttp.ClientSession(headers={"User-Agent": user_agent}) as session:
        async with session.post("http://hastebin.com/documents", data=str(data)) as r:
            if r.status != 200:
                raise FailedHaste
            else:
                return "http://hastebin.com/{}.py".format(ujson.loads(await r.text())["key"])
