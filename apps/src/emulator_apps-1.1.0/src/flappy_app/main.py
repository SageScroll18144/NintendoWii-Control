import asyncio

from .src.flappy import Flappy

def run_flappy():
    asyncio.run(Flappy().start()) 

if __name__ == "__main__":
    asyncio.run(Flappy().start())
