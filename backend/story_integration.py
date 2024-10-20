# story_integration.py
import requests

def register_story_as_ip(nft_contract, token_id, metadata_uri, metadata_hash):
    """
    Registers a story as an intellectual property asset on the Story Protocol blockchain.
    This function sends a POST request to the Story Protocol API to register the provided story details as an IP asset.

    Parameters:
    nft_contract (str): The NFT contract address that will hold the IP asset.
    token_id (str): A unique identifier for the story, typically the database ID.
    metadata_uri (str): The URI pointing to the metadata of the story.
    metadata_hash (str): A hash of the metadata for verification purposes.

    Returns:
    dict: The response from the Story Protocol API, typically containing success status and IP asset details.
    """
    url = "https://api.storyprotocol.net/register_ip"
    headers = {
        "X-CHAIN": "story-testnet",
        "X-API-Key": "4CWuPKSRTTxC7WvjPNsaZlAqJmrGL7OhNniUrZawdu8"
    }
    payload = {
        "nftContract": nft_contract,
        "tokenId": token_id,
        "ipMetadataURI": metadata_uri,
        "ipMetadataHash": metadata_hash,
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()
