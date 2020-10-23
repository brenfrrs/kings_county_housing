# Kings County Housing Predictions

![Kings County](KClogo_LONG.png)

By, Brendan Ferris

## Overview

Using the Kings County Dataset and external zipcode data a predictive linear model was built in order to estimate home prices in Kings County, Washington. Through an initial inspection of the highest and lowest home prices in the county, it is clear that the northern region of the county was home the home of more affluent residents, while the lower portion of the county had the lowest valued homes:

![highest and lowest priced homes](highest_and_lowest_priced_homes.png)


![home price distribution](home_price_distribution.png)


While analyzing the data, I posed three questions:

1. Do areas that have more home renters have higher home prices?
2. Do houses built in the past after 2005 fetch higher prices than older houses?
3. Do the amount of available homes in an area have an effect on the price of the homes in that area?

My initial statistical analysis indicated that these were three significant features for housing prices.

Through non-linear modifications of my model features, I was able to improve my RMSE from a baseline score of 198822 to 122664. The polynomial features of my model sacrifice interpretability for accuracy.



![model residuals](model_residuals.png)


## Next Steps

I believe that with a RMSE hovering near $120,000-- my model performs well given the time constraints of the project. In the future, I believe I may be able to increase this score by including more of the aggregate zip-code data collected from [UnitedStatesZipCodes.org](https://www.unitedstateszipcodes.org).


### For More Information

To see out full analysis, please refer to the [Jupyter Notebook](Kings_County_Housing_Project.ipynb)

For additional info, contact <brendanfrrs@gmail.com>

### Repository Structure
<pre>
├── EDA
│   ├── Cities_and_Unincorporated_King_County___city_kc_area-shp
│   │   ├── Cities_and_Unincorporated_King_County___city_kc_area.cpg
│   │   ├── Cities_and_Unincorporated_King_County___city_kc_area.dbf
│   │   ├── Cities_and_Unincorporated_King_County___city_kc_area.prj
│   │   ├── Cities_and_Unincorporated_King_County___city_kc_area.shp
│   │   ├── Cities_and_Unincorporated_King_County___city_kc_area.shx
│   │   └── Cities_and_Unincorporated_King_County___city_kc_area.xml
│   ├── EDA_notebook.ipynb
│   ├── Kings_County_Housing_Project.ipynb
│   ├── Model\ 3.ipynb
│   ├── Model\ 4.ipynb
│   ├── Model_2.ipynb
│   ├── Test_Regressions_Notebook.ipynb
│   ├── __pycache__
│   │   └── scripts.cpython-36.pyc
│   ├── bedroomsfilled.csv
│   ├── extradata.xlsx
│   ├── housing_preds_Brendan_Ferris.csv
│   ├── lr_poly.pickle
│   ├── scripts.py
│   ├── y.csv
│   ├── zip_code_extra_data.csv
│   ├── zip_code_extra_data.numbers
│   ├── zip_code_extra_data_fixed.csv
│   ├── zip_code_extra_data_fixed.numbers
│   ├── zipcode_data_ex.ipynb
│   └── zipcode_data_feature_elimination.ipynb
├── KClogo_LONG.png
├── Kings_County_Housing_Project.ipynb
├── Predict_holdout.ipynb
├── README.md
├── kc_house_data_test_features.csv
├── kc_house_data_train.csv
├── king_county.jpg<pre>
