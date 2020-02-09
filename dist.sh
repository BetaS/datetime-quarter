#!env/bin/activate

rm dist/*
python3 setup.py sdist bdist_wheel
python3 -m twine upload --repository datetime-quarter dist/*
