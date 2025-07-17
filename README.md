# Credit Card Number Generator

This program generates sentences with valid (Luhn-compliant) credit card numbers for testing purposes.  
Each sentence contains 15–20 words and may include either a credit card number or be a regular sentence for realism.

---

## 🔧 Prerequisites

1. **Python** must be installed on your system.  
   Download it from [https://www.python.org](https://www.python.org) if needed.
2. The file **`CreditCardNumberGenerator.py`** must be in your current working directory.

---

## 🚀 How to Run

1. Download or clone this repository.
2. Locate the `CreditCardNumberGenerator.py` file on your system.
3. Open **File Explorer** (Windows) or **Finder** (macOS).
4. Right-click the file.
5. Choose **"Open with" → "Python"**.
   - If Python is not listed, select **"Choose another app"** and navigate to your Python interpreter manually.

---

## 🛠 Troubleshooting

### ❌ "python is not recognized"
- Python might not be installed or its path isn't added to the system `PATH` variable.
- Solution: Reinstall Python from [python.org](https://www.python.org) and ensure "Add Python to PATH" is selected.

### ❌ "file not found"
- Ensure you are in the correct directory:
  - Use `dir` on Windows Command Prompt or `ls` on PowerShell/Linux/macOS to list files in the current folder.
- Confirm that `CreditCardNumberGenerator.py` is present.

---

## 📋 How to Use

When prompted:
- Enter a number between **100 and 200**.
- Press `Enter`.
- The program will generate that many sentences with a mix of:
  - Realistic fake credit card numbers (generated via the **Luhn algorithm**).
  - Regular, natural language sentences with no card number.

---

## 💡 Example Output


How many sentences to generate?: 5

My new credit card with the number 4532 1234 5678 9012 arrived in the mail yesterday afternoon.


The weather was absolutely perfect for taking a long walk in the beautiful city park.


Please use the credit card number 5555 1234 5678 9012 for processing the payment transaction.


The fluffy cat slept peacefully on the warm windowsill throughout the entire afternoon.


I carefully memorized my new credit card number: 6011 1234 5678 9012 for future reference.

---

## ⚠️ Safety Note

This program generates **fake credit card numbers** for **testing purposes only**.  
These numbers are **not real** and **cannot** be used for actual transactions or payment systems.

---

## 📂 File Structure
