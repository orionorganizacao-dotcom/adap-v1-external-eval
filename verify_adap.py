import hashlib

EXPECTED_HASH = "PENDENTE"

with open("adap_ledger.json", "rb") as f:
    computed_hash = hashlib.sha256(f.read()).hexdigest()

print("Computed hash:", computed_hash)

if computed_hash == EXPECTED_HASH:
    print("VALID: Ledger íntegro e não alterado.")
else:
    print("INVALID: Ledger foi modificado ou o hash não corresponde.")
