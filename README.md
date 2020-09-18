
providing the annotation files of kinetics mini100 and mini200

- the mini100 is the top100 classes of the original kinetics.
- the mini200 is the top200 classes of the original kinetics.


note: 

 - the train_old.csv and val_old.csv is filtered according the "processed kinectics400 dataset" provided by https://github.com/xiaolonw
 - we filtered the broken videos in this dataset. Broken videos is not too much, can be ignored (one or two for some categories).  The final annotation files is the train.csv and val.csv
 - to conduct ablation studies faster. we picked up top100 classes and top200 classes to form the mini100_train.csv and mini200_train.csv
 - Finally, for the task of "video based semi-supervised learning", we generated the 5% 10% 20% 50% and 100% labeled data for each category. you can find this in \*\*\_percent\_\*\*.csv
 
 
