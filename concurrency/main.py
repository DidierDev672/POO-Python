import asyncio

async def fetch_data_from_api(api_name, delay):
    print(f"Starting request to {api_name}...")
    await asyncio.sleep(delay) #? Simualtes network I/O wait
    print(f"Received response from {api_name}")
    return f"Data from {api_name}"

async def fetch_user_profile(user_id):
    print(f"Fetching profile for user {user_id}...")
    await asyncio.sleep(1.5)
    print(f"Profile loaded for user {user_id}")
    return {"user_id": user_id, "name": "John Doe"}


async def main():
    results = await asyncio.gather(
        fetch_data_from_api("Weather API", 2),
        fetch_data_from_api("News API", 1),
        fetch_user_profile(1234)
    )
    print("\nAll operations completed!")
    print("Results: ", results)

asyncio.run(main())
