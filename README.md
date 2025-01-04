# PatientConnect_AI

**PatientConnect_AI** is a Python-based application designed for efficient backend API handling and frontend UI. It leverages Flask for backend API development and Streamlit for a user-friendly interface. The application focuses on providing mental and physical health assistance using AI.

## Requirements

Ensure the following Python dependencies are installed before running the application.

### `requirements.txt`
```plaintext
python-dotenv
groq
requests
Flask
Flask-Cors
langchain==0.1.16
langchain-core
langchain-groq
```

## Installation

Follow these steps to set up and run the project on your local system:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/PatientConnect_AI.git
   cd PatientConnect_AI
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure your `.env` file with the necessary environment variables (e.g., API keys).

## Running the Application

The application consists of two main components:

1. **Backend API** (`backend.py`): Handles user queries and communicates with the AI model.
2. **Frontend UI** (`frontend.py`): Provides an interactive interface for users.

Both components need to run simultaneously for full functionality.

### Running the Backend API (`backend.py`):

1. Start the API:
   ```bash
   python backend.py
   ```

2. Access the API endpoints via tools like Postman or directly through the frontend. The backend runs at:
   ```
   http://localhost:5000
   ```

### Running the Frontend UI (`frontend.py`):

1. Start the Streamlit UI:
   ```bash
   streamlit run frontend.py
   ```

2. Open your browser to view the interface. Streamlit will provide a URL, typically:
   ```
   http://localhost:8501
   ```

## Features

- **Mental Health Mode**: Provides compassionate AI responses to mental health-related queries.
- **Physical Health Mode**: Offers guidance for physical health issues.
- **Adaptive Conversations**: Ensures the mode aligns with the type of user query.
- **Conversation History**: Allows users to view previous interactions during a session.

## Notes

- Ensure `backend.py` and `frontend.py` are running simultaneously for full functionality.
- Use the `.env` file for sensitive configurations like API keys or other credentials.
- Test the API endpoints using tools like Postman before integrating with the frontend.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests for improvements, new features, or bug fixes.

## License

This project is licensed under the [Infosys License](LICENSE).
