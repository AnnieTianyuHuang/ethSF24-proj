# story_connections.py
from sqlalchemy.orm import sessionmaker, Session
from your_project.database import engine, Story
from story_integration import initiate_licensing_agreement

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def connect_stories(origin_story_id: int, linked_story_id: int):
    """
    Manages the connections between stories by initiating licensing agreements using the Story Protocol.
    This function handles the linkage of two stories, ensuring the original creators are compensated or acknowledged through licensing agreements.

    Parameters:
    origin_story_id (int): The ID of the origin story being linked.
    linked_story_id (int): The ID of the story to which the origin is being linked.

    Returns:
    dict: The result of the licensing agreement initiation, including success status and any relevant agreement details.
    """
    db: Session = SessionLocal()
    origin_story = db.query(Story).filter(Story.id == origin_story_id).first()
    linked_story = db.query(Story).filter(Story.id == linked_story_id).first()
    
    if not origin_story or not linked_story:
        return {"error": "One or both stories not found"}
    
    licensing_response = initiate_licensing_agreement(origin_story.ip_asset_id, linked_story.ip_asset_id)
    
    if licensing_response.get('success', False):
        log_story_connection(db, origin_story_id, linked_story_id, licensing_response['agreement_id'])
        return {"message": "Stories connected with licensing agreement", "agreement_details": licensing_response}
    else:
        return {"error": "Failed to establish licensing agreement"}

def log_story_connection(db: Session, origin_id: int, linked_id: int, agreement_id: str):
    # Implement logging logic depending on application architecture
    pass
