# adsk
This builds a wheel out of the stub located  on your computer that you can then install with pip to get auto correct.


### Build and install
You need to have Fusion 360 installed, tested on mac might/should work on windows.

### Wheel
Download the wheel located in releases and `pip install path_to_wheel`


### From Source
#### github
```
pip install https://github.com/Jerakin/adsk-stub.git
```

#### Locally
```
git clone https://github.com/Jerakin/adsk-stub.git  
cd adsk-stub
python setup.py bdist_wheel  
pip install ./dist/<built_package>
```
