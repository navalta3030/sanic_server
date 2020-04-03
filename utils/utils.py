import os

def isDevelopment():
  # verify if we have ENVIRONEMNT: PRODUCTION within our environment variables
  if os.getenv("ENVIRONMENT", None) == "PRODUCTION":
    return False
  return True