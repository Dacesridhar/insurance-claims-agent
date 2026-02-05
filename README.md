Autonomous Insurance Claims Processing Agent

 Overview
This project automates insurance claim processing. It reads claim files (text or PDF), extracts required fields, validates data, and routes claims based on rules.

 Features
- Field extraction from PDF / text
- Data validation
- Routing of claims
- Modular architecture

 Tech Stack
- Python 3.14
- Libraries: pandas, PyPDF2, etc.

 Project Structure
 insurance-claims-agent/
│── README.md
│── requirements.txt
│── data/
│── src/
│ ├── main.py
│ ├── pdf_reader.py
│ ├── field_extractor.py
│ ├── validator.py
│ └── router.py

 How to Run
1. Clone the repo:
git clone https://github.com/Dacesridhar/insurance-claims-agent.git

2.Go to project folder:
cd insurance-claims-agent

3.Install dependencies:
pip install -r requirements.txt

4.Run the project:
python src/main.py
