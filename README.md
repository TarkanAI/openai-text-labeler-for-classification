# OpenAI Text Labeler for Classification

This repository provides a simple pipeline to **automatically label text data** using the OpenAI API.  
It reads raw text from a CSV file, applies a custom classification prompt, and saves the labeled results back into a CSV file.  

---

## 📦 Features
- Reads text data from CSV (one text per row)  
- Uses OpenAI GPT models for classification or labeling  
- Easily configurable for different tasks:  
  - Sentiment analysis  
  - Topic categorization  
  - Custom labels (defined by the user)  
- Exports results into a new CSV file with predicted labels  

---

## 🛠️ Installation

Install required packages:
```
pip install openai pandas tqdm
```

---

## 📂 Input Format

Prepare a CSV file with at least one column named `Content` (or adjust in script).  

Example (`data.csv`):
```
Content
The building collapsed completely
This product is amazing
Floods affected the northern area
The system is safe and stable
```

---

## ▶️ Usage

1. Add your OpenAI API key in the script:
   ```python
   OPENAI_API_KEY = "your_api_key_here"
   ```

2. Adjust the **system prompt** in the script according to your labeling needs.  

### 🔑 Example Prompts
- **Sentiment Analysis**
  ```python
  {"role": "system", "content": "Label the text as Positive, Negative, or Neutral sentiment."}
  ```

- **Topic Categorization**
  ```python
  {"role": "system", "content": "Classify the text into one of the following topics: Technology, Health, Sports, Politics."}
  ```

- **Custom Labels**
  ```python
  {"role": "system", "content": "Classify the text as Spam or Not Spam."}
  ```

3. Choose your model:
   - Works with **gpt-4o-mini**, **gpt-4o**, or any other ChatGPT-compatible model available in your OpenAI account.
   - Example:
     ```python
     response = client.chat.completions.create(
         model="gpt-4o-mini",
         messages=[ ... ]
     )
     ```

4. Run the script:
```
python openai-text-labeler-for-classification.py
```

5. The script will:
   - Process each row of text  
   - Add a new column with the predicted label  
   - Save results into a new CSV file  

---

## 📂 Output Example

Input (`data.csv`):
```
Content
The building collapsed completely
This product is amazing
```

Output (`data_labeled.csv`):
```
Content,Label
The building collapsed completely,Damage
This product is amazing,Positive
```

---

## ⚠️ Notes
- This repository does **not** provide any real dataset.  
- Replace `data.csv` with your own file to test.  
- Labels depend entirely on how you design the system prompt.  
- Any ChatGPT-compatible model can be used (e.g., gpt-4o-mini, gpt-4o).  

---

## 📜 License
MIT License
