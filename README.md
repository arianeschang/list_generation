# List Generation

## 1. Set up configs:
Open config.py, change variables according to what should fill in each drop down. Make sure spelling / capitalization matches. 

## 2. Install requirements: 
```python
pip install selenium
```

## 3. Run
a. Launch a new web browser that will navigate to the page. Log-in and navigate to Turf List. Select the turfs you are generating list numbers for and click Generate List Number > Next. 
```python
python generate.py
```

b. Once you're at the page "Generate X List Numbers". 
```python
python attach.py
```
c. Once it has finished, select the next set of turfs to generate, and repeat step b. 
