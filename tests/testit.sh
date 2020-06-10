# Run the tests using pytest
export PYTHONPATH=`pwd`
source venv/bin/activate
pytest --setup-show 
# OR for less verbose output
# pytest -v