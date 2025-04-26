import os
import subprocess

# Change directory to where app.py is located
app_dir = os.path.join(os.path.dirname(__file__), 'Streamlit_DDD', 'Streamlit_DDD')
os.chdir(app_dir)

# Run the Streamlit app
subprocess.run(["streamlit", "run", "app.py"])