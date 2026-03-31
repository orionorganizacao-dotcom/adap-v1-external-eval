import hashlib

def calculate_sha256(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

ledger_file = "ledger.json"
hash_file = "ledger.sha256"

calculated_hash = calculate_sha256(ledger_file)

with open(hash_file, "r") as f:
    expected_hash = f.read().strip()

print("Computed:", calculated_hash)
print("Expected:", expected_hash)

if calculated_hash == expected_hash:
    print("VALID: Ledger íntegro")
else:
    print("INVALID: Ledger alterado")
