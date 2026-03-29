import hashlib

EXPECTED_HASH = "4cf7f0460b8334e0b9df94c5610ef90ebc163985900b4d1ecb29799367538919"

with open("adap_ledger.json", "rb") as f:
    computed_hash = hashlib.sha256(f.read()).hexdigest()

print("Computed hash:", computed_hash)

if computed_hash == EXPECTED_HASH:
    print("VALID: Ledger íntegro e não alterado.")
else:
    print("INVALID: Ledger foi modificado ou o hash não corresponde.")
