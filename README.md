# Crime_Analysis
## Overview 

Crime Analysis dileniates a pattern between 2021 Crime Data in Austin, TX zip codes and several different segments within each zip code such as; median household income, food scarcity, and daily weather events. The data pipeline uses Python libraries for  ETL into the visualization deployment. Tableau and Unsupervised Machine Learning is implemented to deploy visualizations of trends, if any, between crime and other data points. 

## Data Analysis and Visualization Deployment

https://crime-ut-data-class.herokuapp.com


## Results 

### Machine Learning Clustering     

![Unsupervised Machine Leanring](https://github.com/ChristopheGarcia1/Crime_Analysis-/blob/65b9c8544752c5540e5f888390dd32f4b13f3279/CA_README_IMG/Screenshot%202022-01-29%20at%2011.01.38%20AM.png)

![Unsupervised Machine Learning](https://github.com/ChristopheGarcia1/Crime_Analysis-/blob/65b9c8544752c5540e5f888390dd32f4b13f3279/CA_README_IMG/Screenshot%202022-01-29%20at%2010.39.08%20AM.png)

![Unsupervised Machine Leanring](https://github.com/ChristopheGarcia1/Crime_Analysis-/blob/65b9c8544752c5540e5f888390dd32f4b13f3279/CA_README_IMG/Screenshot%202022-01-29%20at%2011.01.56%20AM.png)

### Informative Tableau Visualizations

I. The following vizulization counts criminals in each zip code by crime type gathered from the Austin Police Departments database, and shows median household income in each zip code, as well as which criminal populations suffer from food insecurity. THe Food insecurity status is color coded in this analysis and is defined as 1 in 4 of the specific criminal. 

    A. 

    https://public.tableau.com/app/profile/moez.khan8652/viz/AustinZipCodesthatare25orMoreFoodInsecurebasedonTypesofCrimeAvgHouseholdIncomein2021/Sheet1?publish=yes


II. The following vizualizations maps out the number of Family Violence and Violent Offenders in the criminal population as well as whether they live in food insecure zip codes or not. The results show more Violent and Family Violent Offenders in zip codes that suffer food scaricity.

    A. Family Violence
   
   https://public.tableau.com/app/profile/moez.khan8652/viz/ofFamilyViolenceOffendersinZipCodeswithFoodDesertsin2021/Sheet1?publish=yes

    
    B. Violent Crime 
   
    https://public.tableau.com/app/profile/moez.khan8652/viz/2021ViolentOffendersinFoodDeserts/Sheet1?publish=yes


III. Weather and Crime Types displays the crime counts in Austin zip codes based on the weather. It is evident that that most crimes are commited in Clear weather, second most in Cloudy weather, and third most in Rainy weather.  These two graphs make up a dashboard overview of the major weather conditions and crimes that take place in Austin, TX.

    A. The Weather Type and Temperature Overview shows the different weather conditions that are recorded by the City of Austin when an incident is recorded. This visualization shows an overview of all the incidents recorded and their corresponding temperature and the specific weather condition when they took place.

    https://public.tableau.com/app/profile/stuart.wilson2140/viz/WeatherandCrimeTypesDashboard/WeatherandCrimeTypesDashboard
    
    B. Below the Weather Type and Temperature Overview is a visualization that shows a breakdown of the major incidents that took place during specific weather conditions.

    https://public.tableau.com/app/profile/stuart.wilson2140/viz/CrimeTypeWeatherConditionFinal/CrimeTypeWeatherCondition
    
### Visualizations of Crime Type and Time of Day

According to the following two graphs, most crimes are committed at 12 PM and the second most at 12 AM. The following plotly graphs were tooled with the following two Python scripts: "px.line_polar" and "px.line". 

![Cimes By Time of Day](https://github.com/ChristopheGarcia1/Crime_Analysis-/blob/65b9c8544752c5540e5f888390dd32f4b13f3279/CA_README_IMG/Screenshot%20(379).png)


![Crime Count By Time of Day](https://github.com/ChristopheGarcia1/Crime_Analysis-/blob/65b9c8544752c5540e5f888390dd32f4b13f3279/CA_README_IMG/Screenshot%20(380).png)


## Conclusion 

The features in our data anlysis of crime in Austin, TX includes a closer look at violent crime types, including family violence and theft, while comparing data points of food scarcity by zip code as well as weather at the given time of day an incident occurs. Although there are no dependent variables in the relationships between the data points in this analysis,there are casual relationships that can be delineated and further visualized.  Overall, the patterns that were futher drawn from visualizations show some strong coorelations and provide usefull information to the public at large. The visualizations are able to tell us how and if weather, household income, and food insecure overlap in a cluster graph using unsupervised machine learning. Informative tableua visulizations provided patterns between crime types and food insecurity, along with weather types and total major crime counts. Lastly, the Plotly library visulization provides a look into crime counts by time of day and helps understand what time of day the most crime took place in 2021. Overall, there may not be a direct cooreleation between all crime types in any of the other variables researched, yet within certain crime types there are significant patterns detected. 


-------------------------------------------------------------------------------------------------------------