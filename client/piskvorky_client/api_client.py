from enum import auto
import requests
from requests.auth import HTTPBasicAuth
from typing import Optional



class ApiClient:
    addr : str
    auth : HTTPBasicAuth

    def __init__(self, addr:str, username:str, password:str):
        self.addr = "http://" + addr
        self.auth = HTTPBasicAuth(username, password)
    
    @staticmethod
    def register(addr:str, username:str, password:str):
        requests.post(f"http://{addr}/account/{username}", data=password)
        return ApiClient(addr, username, password)


    def validate_credentials(self) -> bool:
        return requests.get(f"{self.addr}/validate-credentials", auth=self.auth).status_code == 200

    def delete_account(self):
        return requests.delete(f"{self.addr}/account/{self.auth.username}", auth=self.auth).status_code==200




API_CLIENT: Optional[ApiClient] = None