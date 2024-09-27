This is a submission for thoughtful AI's coding challenge. It's a quick implementation using openai's structured outputs and run in the cli. Just chat with the bot by running:

```bash
pip install -r requirements.txt
python3 main.py
```


# Example Output - Demonstrating with and without FAQ sourcing
```
% python main.py
Thoughtful AI Solution GPT
---


---
You: hi gpt!


---
GPT: Hello! How can I assist you today?


--------------------------------------------------


---
You: what does EVA do?


---
GPT: EVA is designed to automate the verification of a patient's eligibility and benefits information in real-time. This helps eliminate manual data entry errors and reduces the chances of claim rejections.


---
From our FAQ:
- What does the eligibility verification agent (EVA) do?
- EVA automates the process of verifying a patient’s eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections.
```