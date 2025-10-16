import re

def extract_emails(input_file, output_file):
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            text = file.read()

        # Find all email addresses
        emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

        # Remove duplicates
        unique_emails = sorted(set(emails))

        # Save to output file
        with open(output_file, "w", encoding="utf-8") as out_file:
            for email in unique_emails:
                out_file.write(email + "\n")

        print(f"✅ Extracted {len(unique_emails)} unique email(s) saved to '{output_file}'.")

    except FileNotFoundError:
        print("❌ Input file not found. Please check the file name.")
    except Exception as e:
        print(f"⚠️ Error: {e}")

# Example usage
if __name__ == "__main__":
    input_file = input("Enter input text file name (e.g., sample.txt): ")
    output_file = "emails_extracted.txt"
    extract_emails(input_file, output_file)
