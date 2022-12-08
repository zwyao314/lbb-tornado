import hashlib
import json
from app.exceptions import runtime_exception
from app.models.customer.account import Account as AccountEntity
from config import conf


def generate_account_hash(data: dict) -> str:
    hash_fields = [
        "customer_id",
        "currency_code",
        "balance",
        "shares",
        "points",
        "created_at"
    ]
    hash_values = {}
    for field in hash_fields:
        if field not in data:
            raise runtime_exception.RuntimeException(f"Calls function generateAccountHash failed: Missing {field}")
        match field:
            case "balance":
                hash_values[field] = "{:.2f}".format(data[field])
            case "shares":
                hash_values[field] = "{:.2f}".format(data[field])
            case "created_at":
                if data[field] is not None:
                    created_at = data[field]
                    # print(created_at)
                    hash_values[field] = str(int(created_at.timestamp()))
                else:
                    hash_values[field] = ''
            case _:
                hash_values[field] = str(data[field])

    hash_values = sorted(hash_values.items())
    hash_values = dict(hash_values)
    md5 = hashlib.md5(json.dumps(hash_values).encode())
    hash_code = md5.hexdigest()

    return hash_code


def verify_account(account: AccountEntity) -> bool:
    known_hash = account.hash_code
    user_hash = generate_account_hash(account.__data__)

    return user_hash == known_hash


def cache_lifetime() -> int:
    return 300