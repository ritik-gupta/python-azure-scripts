from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient

from os import environ as env

# Environment Variables
TENANT_ID = env.get("TENANT_ID", "")
CLIENT_ID = env.get("CLIENT_ID", "")
CLIENT_SECRET = env.get("CLIENT_SECRET", "")

KEYVAULT_NAME = env.get("AZURE_KEYVAULT_NAME", "")
KEYVAULT_URI = f"https://{KEYVAULT_NAME}.vault.azure.net/"

_credential = ClientSecretCredential(
    tenand_id=TENANT_ID,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
)

_sc = SecretClient(vault_url=KEYVAULT_URI, credential=_credential)

# Demo secrets
DEMO_NAME = _sc.get_secret("NAME").value
DEMO_PASSWORD = _sc.get_secret("PASSWORD").value