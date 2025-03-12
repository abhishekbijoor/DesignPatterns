import time
def wrapper(func):
    def logger(*args, **kwargs):
        print(f"The function {func.__name__} starts with {args} and {kwargs}")
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"The function {func.__name__} executed with {args} and {kwargs}")

        print(f"The function execution completed in {end-start:0.4f} seconds")
        return result
    return logger
@wrapper
def fetch_data(api_url):
    time.sleep(2)  # Simulating API call delay
    return {"data": "Sample API Response"}

# Using the decorated function
response = fetch_data("https://example.com/api")
print(response)