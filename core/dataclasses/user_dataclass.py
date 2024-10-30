from dataclasses import dataclass
from datetime import datetime


@dataclass()
class UserProfile:
    id: int
    name: str
    age: int
    phone: str
    created_at: datetime
    updated_at: datetime


@dataclass()
class User:

    id: int
    email: str
    password: str
    is_active: bool
    is_superuser: bool
    is_staff: bool
    role_type:str
    account_type:str
    created_at: datetime
    updated_at: datetime
    last_login: datetime
    profile: UserProfile
