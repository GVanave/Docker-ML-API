# Flask Dockerized ML API

## Overview

This project demonstrates how to containerize a Flask application with a machine learning model using Docker. The API provides endpoints for predicting outcomes based on a trained machine learning model.

## Getting Started

### Prerequisites

- Python 3.9 or higher
- Docker

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/GVanave/Docker-ML-API.git
    ```

2. **Change into the project directory:**

    ```bash
    cd Docker-ML-API
    ```

3. **Build the Docker image:**

    ```bash
    docker build -t Docker-ML-API .
    ```

4. **Run the Docker container:**

    ```bash
    docker run -p 5000:5000 Docker-ML-API
    ```

5. **Access the API at [http://localhost:5000](http://localhost:5000)**

## API Endpoints

- **/predict:** Endpoint for predicting outcomes with query parameters.
- **/predict_file:** Endpoint for predicting outcomes with a CSV file.

## Machine Learning Models

The project includes an example machine learning model (e.g., Random Forest) for predicting outcomes.

## Additional Information

- Explore the `template.html` file for the HTML template used on the main page.
- The `rf.pkl` file contains the serialized machine learning model.

## Acknowledgments

This project is inspired by the need to understand Docker, Flask, and machine learning integration. Special thanks to the open-source community for valuable resources and tools.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Extended Description

### Project Features

- **Containerization:** Learn how to package a Flask application and a machine learning model into a Docker container for easy deployment.
- **API Endpoints:** Discover how to create API endpoints for predicting outcomes using both query parameters and CSV files.
- **Machine Learning Integration:** Explore the integration of a machine learning model (Random Forest) for predictive analysis.
- **Additional Resources:** Access HTML templates (`template.html`) and serialized machine learning models (`rf.pkl`) included in the project.

### Use Cases

- **Educational Purposes:** Ideal for individuals learning Docker, Flask, and machine learning integration.
- **Prototype Development:** A starting point for developing and deploying Flask applications with integrated machine learning models.
- **API Design Example:** Explore a practical example of designing API endpoints for machine learning applications.

### Future Enhancements

- **Support for Additional Models:** Extend the project to include support for different machine learning models.
- **User Authentication:** Implement user authentication for more secure API access.
- **Improved Documentation:** Enhance documentation for better understanding and contribution.

Feel free to contribute, provide feedback, or use this project as a foundation for your Flask and Docker-based machine learning applications.
