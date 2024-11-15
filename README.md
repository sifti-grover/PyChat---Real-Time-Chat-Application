# PyChat - Real-Time Chat Application

*PyChat* is a Python-based, real-time chat application that allows users to communicate instantly over a network. It includes a server module, a command-line client, and a GUI client for an enhanced user experience. Built using Python sockets, this project is a practical example of networking principles and socket programming.

## Features

- **Real-Time Messaging**: Instantly send and receive messages.
- **Multi-User Support**: Multiple clients can connect and communicate through the server.
- **Graphical User Interface (GUI)**: Includes a GUI-based client for a more user-friendly experience.
- **Command-Line Client**: Lightweight and quick for users who prefer command-line interaction.
- **Python Socket Programming**: Uses Python’s built-in libraries to establish and manage connections.

## Project Structure

- `server.py`: Manages the chat server, handling connections from multiple clients and relaying messages.
- `client.py`: Command-line client allowing users to connect to the server and chat.
- `GUI_client.py`: Graphical client interface built using Tkinter for a more visual experience.

## Technologies Used

- **Python**: Main programming language.
- **Sockets**: For real-time, network-based communication.
- **Tkinter**: Python’s GUI library for the graphical client.

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/sifti-grover/PyChat---Real-Time-Chat-Application.git
   ```

2. **Install Dependencies**:
   This project relies only on standard Python libraries, so no additional installation is needed.

3. **Run the Server**:
   ```bash
   python server.py
   ```

4. **Run the Client**:
   - For the command-line client:
     ```bash
     python client.py
     ```
   - For the GUI client:
     ```bash
     python GUI_client.py
     ```

## Usage

1. Start the server to allow clients to connect.
2. Run either `client.py` or `GUI_client.py` on each client device.
3. Begin chatting in real-time!

## Future Enhancements

- **User Authentication**: Add login/sign-up functionality for secure access.
- **Persistent Chat History**: Store chat logs for future access.
- **Enhanced GUI**: Add additional features such as emojis, file sharing, and themes.

## Contributing

Contributions are welcome! Feel free to fork this repository, make your changes, and submit a pull request.

## Contact

For questions or suggestions, reach out via GitHub:

- **GitHub**: [sifti-grover](https://github.com/sifti-grover)
