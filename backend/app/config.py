'''这个文件后期写docker再写'''

import os

class Config:

    @staticmethod
    def env(val:str='')->str:
        return os.getenv(val,'')
    
    email = {
        'host':env('emailh'),
        'user':env('emailu'),
        'password':env('emailpsw')
    }

