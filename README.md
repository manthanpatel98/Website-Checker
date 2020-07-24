# **Website-Checker**
Checking, is it a Phishing Website or not.




<img src="https://github.com/manthanpatel98/Website-Checker/blob/master/README-Resources/Website-Checker.jpg" width=600>

---

### **Web APP on Heroku**
<img src="https://github.com/manthanpatel98/Website-Checker/blob/master/README-Resources/Phishing.gif" width=600>

**[The Project on Heroku](https://websitechecker1.herokuapp.com/)**

---
## The Dataset
![](https://github.com/manthanpatel98/Website-Checker/blob/master/README-Resources/Dataset.png)
### **[Dataset](https://github.com/manthanpatel98/Website-Checker/blob/master/data.csv)**
---
## **Overview**
* The Dataset has **2453 rows** and **31 columns**.
* It has 31 **columns:**
'having_IP_Address', 'URL_Length', 'Shortining_Service',
 'having_At_Symbol', 'double_slash_redirecting', 'Prefix_Suffix',
       'having_Sub_Domain', 'SSLfinal_State', 'Domain_registeration_length',
       'Favicon', 'port', 'HTTPS_token', 'Request_URL', 'URL_of_Anchor',
       'Links_in_tags', 'SFH', 'Submitting_to_email', 'Abnormal_URL',
       'Redirect', 'on_mouseover', 'RightClick', 'popUpWidnow', 'Iframe',
       'age_of_domain', 'DNSRecord', 'web_traffic', 'Page_Rank',
       'Google_Index', 'Links_pointing_to_page', 'Statistical_report',
       'Result'
* From the Dataset, we have to predict is the website **Phishing** website or not.
* **ExtraTreesClassifier** has been used for Feature Selection.
* I have applied **Artificial Neural Network**, **Random Forest**, **Decision Tree**, **K-NN**, **Naive bayes classification**, **Logistic Regression** and **SVM** algorithms but at the end, **RandomForestClassifier** gave better results.

---
## **Machine Learning Pipelines:**
---
### **1> Feature Engineering:**
  
**a> Handling Missing Values:**
* Here, In this data, there is no requirement of handling missing values because already it is a complete dataset. 
    
**b> Feature Encoding:**   
* In this data, we do not have any categorical columns.

**c> Feature Scaling & Feature Transformation:**    
* Here the data is between -1 to 1. Hence, there is no need to do Scaling or Transformation.

---    
### **2> Feature Selection:**    
* There are various techniques for this but here i have used **ExtraTressClassifier**. For, this Project ExtraTressClassifier showed **4 columns** as most important **'Prefix_Suffix'**, **'web_traffic'**, **'URL_of_Anchor'** and **'SSLfinal_State'**.

![Feature Selection](https://github.com/manthanpatel98/Website-Checker/blob/master/README-Resources/Feature%20Selection.png)

---   

### **3,4&5> Model Selection**, **Model Creation**, **Testing**
    
* To get the proper accuracy and for the proper splitting of the train and test data, I have used **Cross Validation**.
    
* Here, I have tried many algorithms like **Artificial Neural Network**, **Random Forest**, **Decision Tree**, **K-NN**, **Naive bayes classification**, **Logistic Regression** and **SVM**. 
* Among these, **RandomForestClassifier** has  gaven the higher accuracy **(95%)**.
    
| **No** |  **Algorithms** | **Accuracy** |
| --- | ---- | ---- |
| 1 | RandomForestClassifier | 94.46% |
| 2 | Decision Tree | 94.46% |
| 3 | ANN | 94.13% |
| 4 | KNN | 92.5% |
| 5 | SVM | 92.5% |
| 6 | Naive Bayes | 91.3% |
| 7 | Logistic Regression | 92.13% |

---

* For detailed look at Project, go to **[Phishing.ipynb](https://github.com/manthanpatel98/Website-Checker/blob/master/Phishing.ipynb)** and **[model.py](https://github.com/manthanpatel98/Website-Checker/blob/master/model.py)**
