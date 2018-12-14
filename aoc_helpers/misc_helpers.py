import time

# Print with a small delay so that the console output doesn't get mixed in with any error messages.
log = (lambda p: lambda *args, **kwargs: [p(*args, **kwargs), time.sleep(.01)])(print)
