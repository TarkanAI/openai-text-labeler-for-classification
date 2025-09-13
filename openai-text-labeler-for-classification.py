import openai
import pandas as pd
from tqdm import tqdm
import time

# Add your OpenAI API Key
OPENAI_API_KEY = "your_api_key_here"

# Initialize the OpenAI client
client = openai.Client(api_key=OPENAI_API_KEY)

# Input and output files
input_file = "data.csv"          # Input CSV file with a 'Content' column
output_file = "data_labeled.csv" # Output file with predictions

# Load the CSV
df = pd.read_csv(input_file)

# Define classification function
def classify_text(text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",   # You can switch to gpt-4o or another ChatGPT-compatible model
        messages=[
            {
                "role": "system",
                "content": "Label the text as Positive, Negative, or Neutral sentiment."
                # Change the prompt according to your classification task
            },
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content.strip()

# Process texts and collect results
results = []
for text in tqdm(df["Content"], desc="Processing", unit="row"):
    try:
        label = classify_text(text)
        results.append(label)
    except Exception as e:
        results.append("error")
        print(f"Error processing text: {str(e)}")

# Save results
df["Label"] = results
df.to_csv(output_file, index=False)

print(f"Results saved to {output_file}")
