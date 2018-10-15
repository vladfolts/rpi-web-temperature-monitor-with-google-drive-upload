SCRIPTDIR=`dirname "$0"`
export PYTHONPATH=$SCRIPTDIR/..:$PYTHONPATH
pytest -s $@
