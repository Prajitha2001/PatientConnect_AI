# MediTrainAI

MediTrainAI is a Python-based application designed for efficient backend API handling and frontend UI. The application leverages Flask for API development and Streamlit for UI. 

## Requirements

The application requires the following Python dependencies. Make sure you install them before running the application.

### `requirements.txt`
```
python-dotenv
groq
requests
Flask_cors
Flask
langchain==0.1.16
langchain-core
langchain-groq
```

## Installation

Follow the steps below to set up and run the project on your local system:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/MediTrainAI.git
   cd MediTrainAI
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your `.env` file with the required environment variables.

## Running the Application

This application consists of two components:

1. **Backend API** (`app2.py`): Accessible via Postman or other API testing tools.
2. **Frontend UI** (`ui.py`): Accessible via a web browser.

Both components can run simultaneously.

### Running the Backend API (`app2.py`):

1. Start the API using Flask:
   ```bash
   python app2.py
   ```

2. Access the endpoints via Postman or your preferred API client. The backend runs at:
   ```
   https://xyz.com
   ```

### Running the Frontend UI (`ui.py`):

1. Start the UI using Streamlit:
   ```bash
   streamlit run ui.py
   ```

2. Open the browser to view the application. Streamlit will provide a URL, typically something like:
   ```
   http://localhost:8501
   ```

## Notes

- Make sure both `ui.py` and `app2.py` are running at the same time to ensure full functionality.
- Use the `.env` file for sensitive configurations such as API keys or database connections.

## Contributing

Feel free to fork the repository and submit pull requests for improvements or bug fixes.

## License

This project is licensed under the [MIT License](LICENSE).
