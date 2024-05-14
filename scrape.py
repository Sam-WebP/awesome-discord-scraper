import re
import json
import os

# Function to parse community data from README.md
def parse_readme(readme_content):
    communities = []
    
    # Regex pattern to match community sections in README.md
    pattern = re.compile(
        r'\[__(?P<name>.*?)__\]\((?P<invite_link>https://discord\.com/invite/(?P<invite_code>.*?)\)\).*?'
        r'Notable Channels: (?P<notable_channels>.*?) \\.*?'
        r'Language: (?P<language>.*?)\n\n',
        re.DOTALL
    )
    
    matches = pattern.finditer(readme_content)
    
    for match in matches:
        community = {
            "name": match.group('name').strip(),
            "invite_code": match.group('invite_code').strip(),
            "official": False,  # This would need to be determined separately
            "homepage": "",  # Add homepage if available
            "git": "",  # Add git link if available
            "notable_channels": [channel.strip() for channel in match.group('notable_channels').replace('`', '').split(', ')],
            "language": [lang.strip() for lang in match.group('language').replace('`', '').split(', ')]
        }
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
