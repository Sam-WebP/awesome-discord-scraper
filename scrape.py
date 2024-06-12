import re
import json
import os

def parse_readme(readme_content):
    communities = []
    community = None
    current_category = ""
    current_subcategory = ""

    lines = readme_content.splitlines()
    for line in lines:
        line = line.strip()
        print(f"Processing line: {line}")

        # Match category
        match = re.match(r'^##\s+(.*)', line)
        if match:
            current_category = match.group(1).strip()
            current_subcategory = ""  # Reset subcategory when a new category is found
            print(f"Matched category: {current_category}")  # Debugging statement
            continue

        # Match subcategory
        match = re.match(r'^###\s+(.*)', line)
        if match:
            current_subcategory = match.group(1).strip()
            print(f"Matched subcategory: {current_subcategory}")  # Debugging statement
            continue

        # Match server icon
        match = re.search(r'<img align="left" height="94px" width="94px" alt="Server Icon" src="(?P<icon>.*?)">', line)
        if match:
            icon_url = match.group('icon').strip()
            print(f"Matched icon: {icon_url}")  # Debugging statement
            continue

        # Match community name, invite link, official badge, homepage URL, and Git repository URL
        match = re.search(r'\[__(?P<name>.*?)__\]\((?P<invite_link>https://discord\.com/invite/(?P<invite_code>.*?))\)(?:\s*\[<img.*?alt="Official Badge".*?\]\(badges\.md#official-identification-badge\))?(?:\s*\[<img.*?alt="Homepage URL".*?\]\((?P<homepage>.*?)\))?(?:\s*\[<img.*?alt="Git Repository".*?\]\((?P<git>.*?)\))?', line)
        if match:
            if community:
                communities.append(community)
            community = {
                "name": match.group('name').strip(),
                "invite_code": match.group('invite_link').strip(),
                "official": False,  # Set initial value to False
                "homepage": match.group('homepage').strip() if match.group('homepage') else "",
                "git": match.group('git').strip() if match.group('git') else "",
                "notable_channels": [],
                "language": [],
                "icon": icon_url if 'icon_url' in locals() else "",
                "category": current_category,
                "subcategory": current_subcategory
            }
            print(f"Matched community: {community}")  # Debugging statement

            # Match official badge
            if re.search(r'\[<img.*?alt="Official Badge".*?\]\(badges\.md#official-identification-badge\)', line):
                community["official"] = True  # Set official to True if the official badge is found
                print(f"Marked as official: {community['name']}")  # Debugging statement

            # Reset icon_url for next community
            icon_url = ""
            continue

        if community:  # Ensure community is initialized before proceeding
            # Match notable channels
            match = re.search(r'Notable Channels: (?P<notable_channels>.*?)(?:\\|\n|$)', line)
            if match:
                notable_channels = re.split(r',\s*', match.group('notable_channels').replace('`', ''))
                community["notable_channels"] = [channel.strip() for channel in notable_channels]
                print(f"Matched notable channels: {community['notable_channels']} for {community['name']}")  # Debugging statement

            # Match language
            match = re.search(r'Language: (?P<language>.*)', line)
            if match:
                community["language"] = [lang.strip() for lang in match.group('language').split(',')]
                print(f"Matched language: {community['language']} for {community['name']}")  # Debugging statement

    if community:
        communities.append(community)

    return communities

# Path to the input file
input_file_path = 'data/input.md'

# Ensure the input file exists
if not os.path.exists(input_file_path):
    raise FileNotFoundError(f"{input_file_path} not found")

# Read the input file
with open(input_file_path, 'r', encoding='utf-8') as file:
    readme_content = file.read()

# Parse the input file content
communities = parse_readme(readme_content)

# Output file path
output_file_path = 'output.json'

# Convert to JSON and save
with open(output_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(communities, json_file, ensure_ascii=False, indent=4)

print(f"Data has been successfully extracted and saved to {output_file_path}")
