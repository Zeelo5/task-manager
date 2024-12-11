
from decouple import config

SECRET_KEY = config('SECRET_KEY', default='default_key')
print(SECRET_KEY)

import decouple
print(decouple.__file__)

