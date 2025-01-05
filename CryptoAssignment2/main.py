#   Ahmad Nazhan Haziq bin Ahmad Fuad (CA21060)
#   Muhammad Nur Aiman bin Ali (CA21062)
#   Muhammad Nurhidayat Bin Mohd Taufik (CA21073)
#   Title: Implementation Of Diffie-Hellman Key Exchange Using An Example
#   Run on Python 3.12 with PyCharm IDE

#--------------------------------------------------------------#
# Function to calculate modular exponentiation
def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

#--------------------------------------------------------------#
# Function to calculate the public key
def calculate_public_key(base, private_key, mod):
    return mod_exp(base, private_key, mod)

#--------------------------------------------------------------#
# Function to calculate the shared secret key
def calculate_shared_secret(public_key, private_key, mod):
    return mod_exp(public_key, private_key, mod)

#--------------------------------------------------------------#
# Diffie-Hellman key exchange example with specific private keys
if __name__ == "__main__":
    # Publicly agreed parameters
    p = 23  # Prime number
    g = 5   # Base

#--------------------------------------------------------------#
    # Nazhan's private key and public key calculation
    nazhan_private_key = 6
    nazhan_public_key = calculate_public_key(g, nazhan_private_key, p)
    print(f"Nazhan's Private Key: {nazhan_private_key}")
    print(f"Nazhan's Public Key: {nazhan_public_key}")

    # Hidayat's private key and public key calculation
    hidayat_private_key = 15
    hidayat_public_key = calculate_public_key(g, hidayat_private_key, p)
    print(f"\nHidayat's Private Key: {hidayat_private_key}")
    print(f"Hidayat's Public Key: {hidayat_public_key}")

    # Nazhan and Hidayat exchange their public keys
    # Nazhan calculates the shared secret key
    nazhan_shared_secret = calculate_shared_secret(hidayat_public_key, nazhan_private_key, p)
    print(f"\nNazhan's Shared Secret: {nazhan_shared_secret}")

    # Hidayat calculates the shared secret key
    hidayat_shared_secret = calculate_shared_secret(nazhan_public_key, hidayat_private_key, p)
    print(f"Hidayat's Shared Secret: {hidayat_shared_secret}")

    # Verify that both shared secrets are the same
    assert nazhan_shared_secret == hidayat_shared_secret, "Shared secrets do not match!"
    print("\nShared secrets match. Diffie-Hellman key exchange successful.")
