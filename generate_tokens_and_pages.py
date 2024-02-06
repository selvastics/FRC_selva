import os
import uuid

# Path to the participants folder
participants_folder = "participants"

# Path to the folder where token pages will be stored
pages_folder = "token_pages"

# Create the pages folder if it doesn't exist
if not os.path.exists(pages_folder):
    os.makedirs(pages_folder)

# List all files in the participants folder
participant_files = os.listdir(participants_folder)

# Generate token and create page for each participant file
for file in participant_files:
    token = str(uuid.uuid4())  # Generate a unique token
    page_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Token Page</title>
    </head>
    <body>
        <h1>Participant Token: {token}</h1>
        <p>This is the page for token {token}. Replace this text with the content specific to token {token}.</p>
        <p>Participant data for this token: {participants_folder}/{file}</p>
    </body>
    </html>
    """

    # Write the page content to a new HTML file
    with open(f"{pages_folder}/{token}.html", "w") as page_file:
        page_file.write(page_content)

    print(f"Generated token {token} and page for {file}")
