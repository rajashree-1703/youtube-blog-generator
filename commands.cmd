@REM Install the python
@REM https://www.python.org/downloads/

python3 --version

@REM Create the Environment
python3 -m venv venv

@REM Activate the env
source venv/bin/activate

@REM Install package inside venv
pip install uv

@REM Initialize the project
uv init

@REM Add Packages from requirements.txt
uv add -r requirement.txt

@REM or
pip install -r requirements.txt

@REM @REM Create the venv
@REM uv venv

@REM @REM Activate the env
@REM source .venv/bin/activate

@REM To run the project
python3 app.py

@REM To run in langgraph studio or langsmith
langgraph dev