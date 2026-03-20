
1. Create a virtual environment
python -m venv myenv

2. Activate the virtual environment
myenv\Scripts\activate


3. Create a .env file
Add your environment variables inside the .env file.

4. Install the required dependencies
pip install -r requirements.txt

5. change project dir.
cd first-fastapi

6. Run the FastAPI project
uvicorn main:app --reload

7. Run streamlit file
streamlit run streamlit.py