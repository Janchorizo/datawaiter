# datawaiter
Full and column-wise csv data and EDA serving made easy for fast prototyping.

![Logo](./logo.png)

1. Install the package
2. Launch the server with a prefetched _CSV_ file
3. Access the contents of the csv by column and retrieve basic exploratory analysis using Ajax calls
	from the browser, using __this package from a Python terminal/script__, or any other tool such as
	[curl]().

This package aims at facilitating prototyping for data visualization and analysis. Having a ready-to-go 
server for CSV files allow to design and implement prototypes in a decoupled manner, without the hasle of
setting the server. However, you can still make your hands dirty and manage the server manually; the 
`create_app` method in the `datawaiter.server` package allows to create a Flask app which you can extend,
configure and scale as you wish.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install _datawaiter_.

```bash
pip install datawaiter
```

## Usage

### 1. Launch the server
```bash
python -m datawaiter
```

Launch the server prefetching a file for a quicker setup.
```bash
python -m datawaiter
```

Make connections session-based 
```bash
python -m datawaiter
```

Change the temporal directory and remove automatic file deletion for persistent storage (__make
sure you are allowed to save the uploaded files__).
```bash
python -m datawaiter
```

Launch the _datawaiter_ server from within Python
```python
import os 
from datawaiter import server

# Default options
app = server.create_app(
        port=5000,
	use_sessions=False,
	data_folder=os.path.join(os.path.abspath(os.path.curdir), 'data'),
	persistent_data=False
    )

app.run()

### 2. Upload your data
Use command-line utilities
```bash
python -m datawaiter
```

Use AJAX calls in the browsers
```bash
python -m datawaiter
```

Use this package within Python
```Python
import datawaiter as dw

waiter = dw.call_waiter(port=5000) # default value

csv_path = ...
with open(csv_path, 'r') as file:
	waiter.put_dataset(file.read, name='dataset1')
```
Use the built in dashboard. Navigate to the `/` page and upload the dataset.

### 3. Retrieve the data

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
