# unpopular
Looking for not so known bands by genres

# Create virtual environment and activate it:
virtualenv venv && . venv/bin/activate
# Install requirements:
python3 -m pip install -r requirements.txt
# Usage:

python parse_lib.py --help
Usage: parse_lib.py [OPTIONS]

Options:
  -t, --tag TEXT       tag is a requirement option  [required]
  -l, --limit INTEGER  The number of results to fetch per page.  [default: 10]
  -p, --page INTEGER   Number of pages to show  [default: 1]
  -a, --artists        Show artists names
  -i, --info           Show general info
  --help               Show this message and exit.

# Example:
python parse_lib.py -t stoner