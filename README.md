# 🦈 Shark Attacks 🦈
![elgif](https://c.tenor.com/Yf2CEdBk__YAAAAC/finding-nemo-sharks.gif)


[🎹](https://www.youtube.com/watch?v=XqZsoesa55w&ab_channel=PinkfongBabyShark-Kids%27Songs%26Stories)
## Introduction:
This project is aimed to study reported shark attacks. To do so we are using a Data Base sorted in kaggle, you can find it [here](https://www.kaggle.com/teajay/global-shark-attacks).

Excited to know all about shark attacks? How many shark attacks are reported per year? How has this rate evolved during history? 

Where is it more likely for a shark to attack you? (Spoiler, no shark attacks in the coasts of Northern Norway, safe to swim over there🥶)

And what are the features that make you more appetizing to a Shark?

## Hipotizing🤔:
Here are my hypotesis:
1. The gorwth during history will increase At some point we are going to observe a huge growth, as most cases weren't reported in the past, and at some point humans considered reporting this data, for some reason, interesting. Also, it will probably correlated with the global population growth. 

2. I belive most of the attacks will be near the tropics.

3. Men in between their 20's and their 40's are going to be the most common prey. 

This is a summary, for further information go to [0.Exploring](https://github.com/Pomilusky/data-cleaning-pandas/blob/Pomilusky/Code/0.Exploring.ipynb).


## 👩‍💻My code👨‍💻:
I have numbered all the notebooks so it is eassier to follow the code. 

There is one of the files that is not numbered, the functions file. I haven't numbered it because it is use in both cleaning and visualisation files. It is simply a gathering of most of the functions I am using during my code. I have written a description of most functions so the reader doesn't have to actually go to the functions.py file. 

The code is little commented, but I think is pretty easy to read. If there are any quastions you can contact me and I will try to explain further. 

The Data used in the files is not in the repository, you can download the orignial file and run the code to obtain it. 

## Results
The code in the file [2.visualisation](https://github.com/Pomilusky/data-cleaning-pandas/blob/Pomilusky/Code/2.visualization.ipynb), yields some figures as a result. This figures are pretty self explanatory and confirm or not each of the hypothesis. However here you have some commments that summarize the obtained results:
1. It is, in deed, confirmed that Shark Attacks have increased with history. In the past very few were registered, but from 1850's the registers increased exponentially, we can see this evolution in the [second figure](https://github.com/Pomilusky/data-cleaning-pandas/blob/Pomilusky/Images/2.Shark_attack_trendline.png). The increase of the global population is also exponential, thus we can confirme the first of the hypothesis. 
2. To study the second I have created a global map with different colors for different ranges in the number of Shark attacks. This map is not ideal as I haven't been able to modify the colors for each range so it is crucial to read the legend. The observation of this map confirms my hypotesis that Shark attacks are concentred in the tropics, actually according to this data most of the attacks happen in the United States of America or in Australia, I'd say it is very viased, so maybe to study if my hypotesis was true we should check it with other, more reliable, data sources. 
3. To end with the results let's omment on the study of the target victim. According to this data the vast majority of victims, as predicted, are men. Most of them are in their Teen's and their name starts with a J if they are men and with an M if they are women. I'd, now, like for you to google what are the most common names, and you will have prove of why correlation doesn't imply causality. 

## Sources,
### Libraries:
* [Pandas](https://pandas.pydata.org/)
* [Numpy](https://numpy.org/doc/1.18/)
* [Plotly](https://plotly.com/python/)
* [Geopandas] (https://geopandas.org/en/stable/)
* [ReGex](https://docs.python.org/3/library/re.html)
* [Matplotlib](https://matplotlib.org/)
### Source of the data:
*[Kaggle](https://www.kaggle.com/)


