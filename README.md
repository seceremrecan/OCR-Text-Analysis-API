# OCR-Text-Analysis-API

This project involves a service where users can upload an image via an API, and the service can analyze the text in the image, extract sensitive information, and provide a response. Additionally, it enables caching of previously uploaded images to provide a fast response directly from the cache when the same image is uploaded again.

## Features

- Image Upload: An endpoint for users to upload images to the API.
  
- Text Analysis: Processing the text in the uploaded image to identify sensitive information.
  
- Sensitive Data Types: Detection of specified sensitive data types (phone numbers, ID numbers, credit card numbers, etc.).
  
- Caching: Caching of previously uploaded images to provide rapid responses for subsequent uploads.

## Technologies Used

- Python 3.11: The programming language used to write the project's code.
  
- FastAPI: A Python web framework utilized to create and manage the API.
  
- Docker Compose: A container management tool used to swiftly deploy and run the project.
  
- Poetry: A tool employed to manage project dependencies and virtual environments.
  
- Redis: A database system used for caching purposes.

## Docker Installation

1. Clone the project: git clone `https://github.com/user/project-name.git`
 
2. Navigate to the project directory: `cd project-name`

3. Install dependencies: `poetry install`

4. Start Docker containers: `docker-compose up --build`

5. Open your web browser and access the application at `http://localhost:8000`.
