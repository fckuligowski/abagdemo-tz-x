# Run the tests using pytest
export PYTHONPATH=`pwd`
pytest tests/$1 --setup-show 
# OR for less verbose output
# pytest -v