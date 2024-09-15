# Flask Media Server Application

Welcome to the **Flask Media Server Application**, a dynamic and user-friendly web application designed to help you share media content such as videos, images, and other files within your local home network. This project is ideal for families and friends who wish to share selected data without exposing everything to everyone, offering a streamlined and privacy-conscious approach to content sharing.

This application was primarily developed in response to the internet restrictions in Manipur, where staying connected and keeping track of life's moments became a challenge. With this server, there’s no need to repeatedly transfer data from one device to another. The media server makes your content accessible to all connected devices in your home network, simplifying the process of sharing files. It helps keep our memories and moments intact even when offline or when the internet is restricted.

## Author

- **Developer**: [Guang84](https://github.com/Guang84)
- **GitHub**: [https://github.com/Guang84](https://github.com/Guang84)
- **Email**: guangthuanlunggondaimeinss@gmail.com

## Features

- **Media Sharing within Local Network**: Seamless sharing of videos, images, and files across devices connected to the same home network.
- **Folder-based Navigation**: Automatically detects and lists media in folders and subfolders.
- **Responsive Media Playback**: Enjoy videos in fullscreen, with playback, pause, and download options.
- **No User Authentication**: A simple, secure application without the hassle of user accounts or logins.
- **Dynamic Pagination**: Easily browse through large directories with pagination.
- **Search Functionality**: Quickly search for any media file by name.
- **Download Support**: Download media files or entire folders as a ZIP archive.
- **No Repeated File Transfers**: Once media is added to the server, it’s accessible from any device on the network, eliminating the need to transfer files manually between devices.
- **Offline-Friendly**: Built for scenarios where internet access is limited or unavailable.
- **Responsive Design**: Works smoothly on desktops, tablets, and smartphones.

## Project Overview

This project allows users to set up a media server that can be accessed locally by family and friends. The application displays files stored in designated media directories and provides options for playing, downloading, and navigating the content.

### Real-Life Use Case

Designed primarily for a family setup, this application allows users to share specific media without giving access to all data, maintaining a balance between privacy and sharing. In Manipur, where internet access has been restricted, this application provides a way for families and close friends to stay connected by sharing photos, videos, and important files over a local network without the need for internet. Plus, once files are added to the server, they can be accessed by all connected devices, avoiding the hassle of transferring files repeatedly from one device to another.

## Project Structure

```bash
media_server/             # Main apllication Folder
│
├── media/                # Folder with your media files (e.g., videos, images, etc.)
│   ├── videos/
│   │   └── example_video.mp4
│   ├── images/
│   │   └── example_image.jpg
│   └── documents/
│       └── example_document.pdf
|           # add any folder according to your preference
│
├── app.py                # Flask application
├── requirements.txt      # List of dependencies
├── static/               # Folder for static files like CSS
│   └── styles.css        # CSS for styling
└── templates/            # HTML templates
    ├── index.html        # Template for listing media
    └── media_view.html   # Template for viewing media
```

## Installation

### Prerequisites

- **Python 3.x**: Make sure Python 3 is installed on your system.
- **Pip**: Ensure you have `pip`, the Python package installer.
- **Local Network**: For a real-life home network setup, ensure your devices are connected to the same network.

### Step-by-Step Installation Guide

1. **Clone the repository**:

   Clone the project repository to your local machine using Git.

   ```bash
   git clone https://github.com/Guang84/HomeMedia_Server.git
   cd HomeMedia_Server
   ```

2. **Create and activate a virtual environment** (optional but recommended):

   A virtual environment helps to isolate dependencies for this project.

   ```bash
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate

   # On Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**:

   Install the required Python packages using the `requirements.txt` file.

   ```bash
   pip install -r requirements.txt
   ```

4. **Add your media files**:

   Place your media files (videos, images, etc.) into the `media` folder. The application will list these files automatically.

5. **Run the application**:

   Start the Flask development server to host the application on your home network.

   ```bash
   python app.py
   ```

   By default, the application will be accessible in your browser at `http://127.0.0.1:5000/`. For home network use, change the host to `0.0.0.0` to allow access from other devices on your network.

   ```bash
   python app.py --host=0.0.0.0
   ```

   Now the app will be available at `http://<your-local-ip>:5000/`, and you can access it from any device on your home network.

## User Guide

### Accessing the Application

Once the application is running, open your browser and go to the local IP address assigned to the hosting device (e.g., `http://192.168.1.10:5000/`). You will see a list of all available media files from the `media` folder. Make sure you used the host IP to access in other divices.

### Viewing Media

- Click on any media file (e.g., video or image) to view or play it.
- For videos, use the provided controls to play, pause, or view in fullscreen.
- For images, you can view them in a larger size and download if needed.

### Downloading Media

- To download media files or entire folders, click the download button associated with the media or folder you wish to save.

### Adding More Media

- To add more media files, simply drop them into the `media` folder. Refresh the home page, and the app will list the newly added files.

## Supported File Types

This application supports the following file types:
- **Videos**: Plays media files like `.mp4`, `.avi`, etc.
- **Images**: Displays image files like `.jpg`, `.png`, `.gif`, etc.
- **Documents**: Provides access to documents like `.pdf`, `.docx`, etc.

## Extending the App

1. **Adding More File Formats**:
   - You can extend the app to support additional file types by modifying the Flask routes and adding relevant handling logic.

2. **Styling**:
   - Modify the CSS file located in `static/styles.css` to customize the look and feel of the app ( https://cdn.jsdelivr.net/npm/tailwindcss@2.0.3/dist/tailwind.min.css).
   - Add JavaScript for enhanced user interaction if needed.

3. **Using a Database**:
   - Consider using a database like SQLite to manage metadata or save progress, especially if you plan to add user-specific features in the future.

## Security Considerations

For a real-life home network setup, it’s recommended to:

- **Use a firewall**: Ensure that only devices on your home network can access the app.
- **HTTPS**: If you’re concerned about security, set up SSL certificates and serve the app over HTTPS, especially if you plan to access the application remotely.

## Troubleshooting

- **CSS Not Loading**: Make sure your `static` folder contains the `styles.css` file, and the file paths are correctly referenced in the HTML templates using `{{ url_for('static', filename='styles.css') }}`.
- **Application Not Starting**: Ensure you’ve installed all dependencies using `pip install -r requirements.txt`. Also, check that Flask is properly installed by running `pip show Flask`.
- **File Not Supported**: If a file format is not supported, ensure the file extension is recognized in the code. Add more handling logic if needed.

## Contribution

Contributions are welcome! If you’d like to improve the project, feel free to fork the repository and submit a pull request. Here’s how you can contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

Please make sure your code follows best practices and includes relevant documentation.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.