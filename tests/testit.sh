# Run the tests using pytest
export PYTHONPATH=`pwd`
pytest tests/$1 --setup-show $2 $3 $4 $5 $6 $7 $8 $9
# OR for less verbose output
# pytest -v