# 📄 Automated Documentation Generator

The **Automated Documentation Generator** is a web application designed to automatically generate technical documentation from code. It parses source code, extracts relevant information, and creates well-structured documentation in real-time.

## ✨ Features

- **📝 Automatic Documentation**: Generate documentation for your code with just one click.
- **🌐 Supports Multiple Languages**: Works with various programming languages, thanks to flexible parsing logic.
- **💻 Web Interface**: Easy-to-use interface for viewing and managing generated documentation.
- **💾 Persistent Storage**: Documentation is stored in a database, allowing you to access it anytime.

## 🛠️ Technologies Used

- **🔙 Backend**: Flask, SQLAlchemy
- **🔛 Frontend**: React.js
- **🗄️ Database**: SQLite

## 🚀 Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Apatoma/automated-docs-generator.git
    cd automated-docs-generator
    ```

2. **Set up the backend**:
    ```bash
    cd backend
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python run.py
    ```

3. **Set up the frontend**:
    ```bash
    cd frontend
    npm install
    npm start
    ```

4. **Access the application**:
    - The backend will run on `http://localhost:5000`
    - The frontend will run on `http://localhost:3000`

## 🧑‍💻 Usage

- **🔧 Generate Documentation**: Send your code to the backend via the frontend interface to generate documentation.
- **📖 View Documentation**: Use the frontend to browse the generated documentation.
- **🗂️ Manage Documentation**: View, update, or delete documentation entries through the web interface.

## 🔮 Future Enhancements

- **📚 Support for More Languages**: Extend parsing capabilities to support additional languages.
- **🖨️ Customizable Output Formats**: Allow users to choose output formats like Markdown, PDF, or HTML.
- **🎨 Improved UI/UX**: Enhance the user interface with additional features like search and filter options.

## 📜 License

This project is licensed under the MIT License.
