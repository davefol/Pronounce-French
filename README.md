# Pronounce (French)
This is a simple program that I wrote to quickly acquire pronounciation for french words for use in my Anki flash cards. I may or may not add a simple GUI for the less tech savy in a future version. Feel free to send pull requests and add issues.


## Installing and Using
If you are running on Mac OSX, you can simply use the ```pronounce``` executable in the ```dist``` folder by dragging it to your desired folder then running it as you would any other executable, ie ```./pronounce vivant```.  Otherwise, follow the instructions below.

To install, create an python 3 virtual environment in the same directory named "env"
```python3 -m venv env```

Then install the required libraries to the virtual environment using either the requirmenets file.

```./env/bin/pip install -r requirements.txt ```

Now you can either run the ```pronounce``` script, which is just a BASH script or ```python pronounce.py myword``` from your virtual environment. 
