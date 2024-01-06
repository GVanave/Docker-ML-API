
import pickle
from flask import Flask, request, render_template
from flasgger import Swagger
import numpy as np
import pandas as pd

with open('./rf.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

app = Flask(__name__)
swagger = Swagger(app)

from flask import render_template

from flask import render_template

@app.route('/')
def home():
    """Main page providing information about the project and why machine learning is important
    """
    project_purpose = (
        "<p>This project serves as a simple example to understand the working of Docker and how to create a Docker image.</p>"
        "<p>The primary focus is on demonstrating the process of containerizing a Flask application that includes a machine "
        "learning model. Docker allows for easy packaging and deployment, making it a valuable tool for building, shipping, "
        "and running applications across different environments.</p>"
        "<h3>Why Machine Learning is Important:</h3>"
        "<ul>"
        "<li>Machine learning enables computers to learn from data and make intelligent decisions.</li>"
        "<li>It is widely used in various fields such as healthcare, finance, marketing, and more.</li>"
        "<li>Machine learning models can analyze complex patterns, make predictions, and automate tasks.</li>"
        "<li>It improves efficiency and decision-making processes in diverse applications.</li>"
        "<li>This API demonstrates the power of machine learning with an example model for predicting outcomes.</li>"
        "</ul>"
        "<h4>Common Machine Learning Algorithms:</h4>"
        "<ul>"
        "<li>Linear Regression</li>"
        "<li>Random Forest</li>"
        "<li>Support Vector Machines (SVM)</li>"
        "<li>K-Nearest Neighbors (KNN)</li>"
        "<li>Gradient Boosting</li>"
        "</ul>"
        "<h3>Docker and Docker Image:</h3>"
        "<p>Docker is a platform for developing, shipping, and running applications in containers. A container is a lightweight, "
        "stand-alone, and executable software package that includes everything needed to run a piece of software, including "
        "the code, runtime, libraries, and system tools.</p>"
        "<p>A Docker image is a lightweight, standalone, and executable software package that includes the application code, libraries, "
        "dependencies, and other settings required to run the application. Docker images make it easy to deploy applications consistently "
        "across different environments and ensure that the application runs the same way in development, testing, and production.</p>"
        "<h4>Why Docker Images are Important:</h4>"
        "<ul>"
        "<li>Consistency: Ensures that the application runs the same way in any environment.</li>"
        "<li>Isolation: Keeps applications and their dependencies isolated from the host system.</li>"
        "<li>Portability: Allows easy distribution and deployment of applications across different systems.</li>"
        "<li>Efficiency: Lightweight containers have minimal overhead and fast startup times.</li>"
        "<li>Scalability: Enables easy scaling of applications by running multiple instances in containers.</li>"
        "</ul>"
        "<p><strong>Result:</strong> After training and testing different machine learning algorithms, it was found that Support Vector Machines (SVM) performed the best for the given task.</p>"
        "<h4>Thanks for visiting</h4>"
    )

    return render_template('template.html', project_purpose=project_purpose)




@app.route('/predict')
def predict_iris():
    """Example endpoint returning a prediction of iris
    ---
    parameters:
      - name: s_length
        in: query
        type: number
        required: true
      - name: s_width
        in: query
        type: number
        required: true
      - name: p_length
        in: query
        type: number
        required: true
      - name: p_width
        in: query
        type: number
        required: true
    """
    s_length = request.args.get("s_length")
    s_width = request.args.get("s_width")
    p_length = request.args.get("p_length")
    p_width = request.args.get("p_width")
    
    prediction = model.predict(np.array([[s_length, s_width, p_length, p_width]]))
    return str(prediction)

@app.route('/predict_file', methods=["POST"])
def predict_iris_file():
    """Example file endpoint returning a prediction of iris
    ---
    parameters:
      - name: input_file
        in: formData
        type: file
        required: true
    """
    input_data = pd.read_csv(request.files.get("input_file"), header=None)
    prediction = model.predict(input_data)
    return str(list(prediction))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
  
    
    
    
    
    
    
    
    
    
    
    
    
    
    