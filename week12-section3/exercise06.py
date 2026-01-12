import re
from pydantic import BaseModel, Field
from pymongo import MongoClient


class Customer(BaseModel):
    identity: str = Field(
        ...,
        min_length=11,
        max_length=11,
        description="The identity of the customer."
    )
    full_name: str = Field(
        ...,
        min_length=3,
        description = "Full name of customer."
    )
    email: str = Field(
        ...
    )
    phone: str = Field(
        ...
    )

mongo_client = MongoClient("mongodb://localhost:27017")
crmdb = mongo_client["crmdb"]
customers_collection = crmdb["customers"]

phone_pattern = "\\d{3}-\\d{3}-\\d{4}"
email_pattern = "\\s*\\w+\\.?\\w*@\\w+\\.\\w{2,5}\\s*"
with open("resources/customers.csv", "rt") as file:
    for line in file.readlines():
        full_name,identity,phone,email = re.split("\\s*,\\s*",line)
        if not re.fullmatch(phone_pattern,phone):
            continue
        if not re.fullmatch(email_pattern,email):
            continue
        print(full_name,identity,phone,email, end="")
        customers_collection.insert_one({
            "identity": identity.strip(),
            "full_name": full_name.strip(),
            "email": email.strip(),
            "phone": phone.strip(),
        })