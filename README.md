
# Content Moderation Tool

This Python project provides a simple interface for moderating text and image-based content using OpenAI's moderation API. It allows users to detect and flag potentially harmful or inappropriate content.

## Features

- **Text Moderation**: Analyze text content for violations of content guidelines and flag inappropriate content with associated categories and confidence scores.
- **Text and Image Moderation**: Analyze both text and image content simultaneously for content moderation.
- **User-Friendly CLI Interface**: Simple console-based user interaction for moderation tasks.

## Prerequisites

Before using this tool, ensure you have the following installed:

1. **Python 3.8+**
2. **Pandas**:
   ```bash
   pip install pandas
   ```
3. **OpenAI Python Client**:
   ```bash
   pip install openai
   ```

## Setup

1. Clone or download this repository to your local machine.
2. Replace the `API_KEY` value in the `app.py` file with your OpenAI API key.

## Usage

Run the script using the command:

```bash
python app.py
```

Follow the on-screen instructions to moderate content:

1. **Option 1**: Enter text content for moderation.
2. **Option 2**: Enter both text content and an image URL for moderation.
3. **Option 3**: Exit the program.

## Key Functions

- **`moderate_text(input_text)`**:
  - Analyzes text content.
  - Returns flagged categories and their confidence scores if content violations are detected.
- **`moderate_content(input_text, image_url)`**:
  - Analyzes both text and image content together for violations.

## Example Output

### Input:
```plaintext
Option: 1
Enter the Text content: Example inappropriate text
```

### Output:
```plaintext
Found Flagged Content
Content Violation Category: {'violence', 'hate_speech'}
Confidence Scores per Violated Category: {'violence': 0.98, 'hate_speech': 0.75}
```

## Notes

- Ensure your API key has the necessary permissions for content moderation.
- Use valid URLs when moderating image content.
- This tool relies on the **"omni-moderation-latest"** model for the best results.

## Limitations

- Designed for educational or demonstration purposes.
- Requires an active internet connection for API calls.

## License

---
---

Feel free to customize the README further based on additional requirements or features.