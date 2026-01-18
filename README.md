Steps to run application

- Install "pyenv" / "pyenv-win" application to do Python version managment
- Install "poetry" application to work with code
- Open the root application folder
- Do:
    1. pyenv install 3.12.10
    2. pyenv which python -> the output will containt the path to the interpreter
    3. poetry env use *INTERPRETER_PATH*
    4. poetry install
    5. poetry run app

Briefly about application:

Simple model training using Keras library on a simple dataset with English letters.