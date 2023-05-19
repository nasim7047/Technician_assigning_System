echo "BUILD START"
python3.9 -m pip install -r requirment.txt
python3.9 manage.py collectstatic --noinput --clear
echo "BUILD END"
