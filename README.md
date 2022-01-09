# Portfolio-Optimizer
This project has three files: two of them are python and one of them is excel. The way it works is you run the python script "Portfolio Builder.py" with stocks you want to create optimized portfolios for. For the Portfolio Builder.py file make sure pandas and yfinance are installed. 

This generates a stock_data comma seperate value file. Using powerquery pull the data from the stock_data csv. Then you run the portfolio builder vba file! It creates a minimum variance portfolio and tangency portfolio of the stocks you specified in Portfolio Builder.py! Make sure that you use a vba enabled spreadsheet and solver works with your vba. Also you will need to specify the ws1 variable for the spreadsheet you are applying the macro to.
