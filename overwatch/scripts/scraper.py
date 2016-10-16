from overwatch import app
import xmltodict
import asyncio
import aiohttp

loop = asyncio.get_event_loop()
semaphore = asyncio.Semaphore(5)

def fetch_urls(urls, parser):
    async def fetch(url):
        with (await semaphore):
            response = await aiohttp.request('GET', url)
            content = await response.read()
            await asyncio.sleep(1)
            if app.debug:
                print('Fetch: {url} <Status {status}>'.format(url=url, status=response.status))
            return parser(content)

    urls_to_fetch = [fetch(url) for url in urls]
    parsed_urls = loop.run_until_complete(asyncio.gather(*urls_to_fetch))
    return parsed_urls


def parse_xml(url, params = []):
    if not params:
        urls = [url]
    else:
        urls = [url.format(**a) for a in params]
    return fetch_urls(urls, xmltodict.parse)
