# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "pandas",
#     "seaborn",
#     "matplotlib",
#     "openai==0.28",
#     "chardet"
# ]
# ///


import os
import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import openai
import chardet
# Set the OpenAI API key
# AI Proxy details
#API_URL = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
API_TOKEN = os.getenv("API_TOKEN")



def load_data(file_path):
    """Load the dataset, handling encoding issues automatically."""
    try:
        # Step 1: Detect encoding
        with open(file_path, "rb") as f:
            raw_data = f.read(100000)  # Read a sample of the file for detection
            result = chardet.detect(raw_data)
            detected_encoding = result['encoding']
            print(f"Detected encoding: {detected_encoding}")

        # Step 2: Attempt to load the file with detected encoding
        try:
            data = pd.read_csv(file_path, encoding=detected_encoding)
        except UnicodeDecodeError:
            print("Detected encoding failed, retrying with fallback encoding...")
            data = pd.read_csv(file_path, encoding="ISO-8859-1")

        print(f"Dataset loaded successfully: {file_path}")
        return data

    except Exception as e:
        print(f"Error loading dataset: {e}")
        sys.exit(1)

    except Exception as e:
        print(f"Error loading dataset: {e}")
        sys.exit(1)

def analyze_data(data):
    """Perform general analysis on the dataset."""
    summary = {
        "Shape": data.shape,
        "Columns": data.dtypes.to_dict(),
        "Missing Values": data.isnull().sum().to_dict(),
        "Summary Statistics": data.describe(include='all').to_dict()
    }
    return summary

def visualize_data(data, output_dir):
    """Generate visualizations and save as PNG."""
    os.makedirs(output_dir, exist_ok=True)

    visuals = []

    # Correlation Heatmap
    if data.select_dtypes(include='number').shape[1] > 1:
        corr = data.corr(numeric_only=True)
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
        heatmap_path = os.path.join(output_dir, "correlation_heatmap.png")
        plt.savefig(heatmap_path, bbox_inches='tight')
        plt.close()
        visuals.append(heatmap_path)

    # Histogram for numeric columns
    for column in data.select_dtypes(include='number').columns:
        plt.figure(figsize=(8, 6))
        sns.histplot(data[column], kde=True, bins=30, color='blue')
        hist_path = os.path.join(output_dir, f"{column}_histogram.png")
        plt.savefig(hist_path, bbox_inches='tight')
        plt.close()
        visuals.append(hist_path)

    print(f"Visualizations saved in: {output_dir}")
    return visuals

def query_llm(prompt):
    """Send a prompt to the LLM and return the response."""
    try:
        # Set API base for AI Proxy
        openai.api_base = "https://aiproxy.sanand.workers.dev/openai/v1"
        openai.api_key = "API_TOKEN"
        # Make the API request
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7
        )
        return response["choices"][0]["message"]["content"]
    except openai.error.AuthenticationError:
        print("Authentication Error: Invalid API token. Please check your configuration.")
        return "Error: Authentication failed due to invalid API token."
    except openai.error.OpenAIError as e:
        print(f"OpenAI API Error: {e}")
        return "Error: Unable to generate a narrative due to an API issue."
    except Exception as e:
        print(f"General Error: {e}")
        return "Error: An unexpected issue occurred while generating the narrative."






def generate_narrative(data_summary, visuals):
    """Use LLM to generate a narrative."""
    prompt = (
        f"I analyzed a dataset with the following summary:\n{data_summary}\n"
        f"The following visualizations were created:\n{visuals}\n"
        "Please generate a detailed narrative for README.md that includes key insights and implications."
    )
    return query_llm(prompt)

def save_readme(output_dir, narrative):
    """Save the LLM-generated narrative as README.md."""
    if not isinstance(narrative, str) or narrative.strip() == "":
        narrative = "No narrative could be generated. Please review the analysis and retry."
    
    readme_path = os.path.join(output_dir, "README.md")
    with open(readme_path, "w") as f:
        f.write(narrative)
    print(f"Narrative saved in: {readme_path}")


def main():
    if len(sys.argv) != 2:
        print("Usage: uv run autolysis.py <dataset.csv>")
        sys.exit(1)

    file_path = sys.argv[1]
    output_dir = os.path.splitext(file_path)[0]

    # Load dataset
    data = load_data(file_path)

    # Analyze data
    data_summary = analyze_data(data)

    # Visualize data
    visuals = visualize_data(data, output_dir)

    # Generate narrative
    narrative = generate_narrative(data_summary, visuals)

    # Save narrative
    save_readme(output_dir, narrative)

if __name__ == "__main__":
    main()
