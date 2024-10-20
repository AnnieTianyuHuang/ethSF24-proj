# story_submission.py
from sqlalchemy.orm import sessionmaker, Session
from your_project.database import engine, Story
from story_integration import register_story_as_ip

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def submit_story(user_id: int, story_content: str, location: dict, metadata_uri: str, metadata_hash: str):
    """
    Handles the submission of a story by a user, saves it in the database, and registers it as an IP asset on the Story Protocol.
    This function creates a new story record in the database and then calls register_story_as_ip to secure IP rights on the blockchain.

    Parameters:
    user_id (int): The ID of the user submitting the story.
    story_content (str): The content of the story.
    location (dict): A dictionary containing latitude and longitude of the story location.
    metadata_uri (str): The URI for the story's metadata.
    metadata_hash (str): The hash of the story's metadata.

    Returns:
    dict: The registration result from the blockchain and details of the newly created story.
    """
    db: Session = SessionLocal()
    new_story = Story(
        author_id=user_id,
        content=story_content,
        latitude=location['latitude'],
        longitude=location['longitude']
    )
    db.add(new_story)
    db.commit()
    db.refresh(new_story)

    ip_response = register_story_as_ip(
        nft_contract="0xYourNFTContractAddress",
        token_id=str(new_story.id),
        metadata_uri=metadata_uri,
        metadata_hash=metadata_hash
    )
    
    if ip_response.get('success', False):
        new_story.ip_asset_id = ip_response['ipId']
        db.commit()
        return {"message": "Story registered successfully on blockchain", "story_details": new_story}
    else:
        db.rollback()
        return {"error": "Failed to register story on blockchain"}
