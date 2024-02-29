## Module 4.2: Exploring Data with Pandas

### Overview

In this class, students will review the structure of a DataFrame, learn how to interact with elements within the DataFrame, and sort values in single and multiple columns, both in ascending and descending order. They will also learn how to use various Pandas functions, clean data, handle missing values within datasets, delete any unnecessary columns, and how to deal with inconsistencies in the data. Students will be introduced to NumPy and SciPy, libraries for Python that assist in statistical, numerical, and scientific functions. These libraries are used in determining measures of central tendency, variance, standard deviation, and outliers of numerical datasets. Lastly, students will explore the concept of correlation, and learn how to determine whether two variables are correlated.

### Class Objectives

By the end of today's class, the students will be able to:

* Sort values in a DataFrame.

* View Summary Statistics using Describe.

* Utilize mean, sum, nunique, value_counts, and more where appropriate.

* Utilize foundational Python concepts to explore data with Pandas.

---

### Instructor Notes

Welcome to this lesson on exploring data with Pandas. Today, we will dive into the exploration of data in Pandas, how to organize the data, and analysis of the data through NumPy and SciPy – two specialized Python libraries.

---

### Class Slides

The slides for this lesson can be viewed on Google Drive here: [Module 4.2 Slides](https://docs.google.com/presentation/d/1-diSxf0BKaQNPF1yL9RS-Xct5t2lcotpni7Wie-weno/edit?usp=sharing).

To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit).

**Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

---

### Time Tracker

| Start Time | Number | Activity                                           | Duration |
| ---------- | ------ | -------------------------------------------------- | -------- |
| 6:30 PM    | 1      | Instructor Do: Introduction to the Class           | 0:05     |
| 6:35 PM    | 2      | Student Do: DataFrame Review           | 0:10     |
| 6:45 PM    | 3      | Review: DataFrame Review           | 0:05     |
| 6:50 PM    | 4      | Instructor Do: Sorting Values           | 0:10     |
| 7:00 PM    | 5      | Instructor Do: Exploring Data           | 0:15     |
| 7:15 PM    | 6      | Student Do: Search for the Worst           | 0:20     |
| 7:35 PM    | 7      | Review: Search for the Worst           | 0:15     |
| 7:50 PM    | 8      | Break         | 0:15     |
| 8:05 PM    | 9      | Instructor Do: Intro to NumPy and SciPy         | 0:10     |
| 8:15 PM    | 10      | Instructor Do: Central Tendency         | 0:15     |
| 8:30 PM    | 11      | Instructor Do: Summary Statistics         | 0:15     |
| 8:45 PM    | 12      | Instructor Do: Intro to Quartiles and Outliers        | 0:15     |
| 9:00 PM    | 12      | Instructor Do: Quartiles and Outliers         | 0:15     |
| 9:15 PM    | 12      | Student Do: Summary Statistics         | 0:15     |
| 9:30 PM    | 13      | Review: Summary Statistics         | 0:10     |
| 9:40 PM    | 14      | Everyone Do: Pandas Recap      | 0:30     |
| 10:10 PM    | 15     | End Class                                          | 0:05     |

---

### 1. Instructor Do: Introduction to the Class (5 min)

Open the slide deck and use the first few slides to facilitate your welcome to the class. Cover the following points:

* Welcome the students to the second lesson, and explain that they will be exploring the manipulation of Python data within DataFrames, as well as analysis of the data, by viewing summary statistics of a DataFrame.

* Let students know that they will be using two additional libraries, NumPy and SciPy, which assist in data analysis and obtaining summary statistics of a DataFrame.

### 2. Student Do: DataFrame Review (10 min)

**Corresponding Activity:** [01-Stu_DataFrame-Review](Activities/01-Stu_DataFrame_Review)

Continue through the slides, using the next slides to accompany this activity.

This activity will give students an opportunity to use Pandas to find various pieces of information from a dataset on temperature readings from LAX airport.

### 3. Review: DataFrame Review (5 min)

**Corresponding Activity:** [01-Stu_DataFrame-Review](Activities/01-Stu_DataFrame_Review)

Open the solution and share the file with the students. Don’t review this line by line, but use the time to answer any specific questions that students may have.

If no questions are asked, review the following key points:

* To read in the CSV file provided and display the first five rows of the DataFrame, use the following code:

```python
# Import the data
file = "../Resources/lax_temperature.csv"
temperature_df = pd.read_csv(file)

# Show the first 5 rows
temperature_df.head()
```

* To rename the columns according to the constraints provided, use the following code:

```python
# Rename the columns

renamed_df = temperature_df.rename(columns = {
    "STATION": "station",
    "DATE": "date",
    "REPORT_TYPE": "report_type",
    "HourlyDryBulbTemperature": "hourly_temp"
})
Renamed_df
```

* To determine the answers for the various questions posed, use the following code:

```python
# How many reports are there of report type FM-16?

fm16_df = renamed_df.loc[renamed_df['report_type'] == 'FM-16']
len(fm16_df)
```

* There are 510 FM-16 report types.

```python
# How many readings measured a temp over 70?

over70_df = renamed_df.loc[renamed_df['hourly_temp'] > 70]
len(over70_df)
```

* There are 96 readings with a temperature over 70.

```python
# What was the temperature for the 276th reading?

renamed_df.iloc[275, 3]
```

* The 276th temperature reading is 61, but note that students might select index 276 instead of 275. Use this as an opportunity to talk about [off by one](https://en.wikipedia.org/wiki/Off-by-one_error) errors!

```python

# What were the dates and report types of rows 500 through 505?

renamed_df.iloc[500:506, 1:3]
```

* To display the last 10 rows of the DataFrame, use the following code:

```python
# Show the last 10 rows of the DataFrame
renamed_df.tail(10)

# Alternate
renamed_df.iloc[-10:]
```

### 4. Instructor Do: Sorting Values (10 min)

**Corresponding Activity:** [02-Ins_Sorting](Activities/02-Ins_Sorting)

Continue through the slides, using the next slides to accompany this activity.

Open the solution file within the Jupyter notebook, send the file to students, and go through the code with the class, discussing each cell as you cover the following talking points:

* It’s possible to sort the Vermont meals and rooms tax statistics data by using the values in different columns.

* To sort a DataFrame based on the values within a column, simply use the `df.sort_values` method and pass in the column name to sort by as a parameter.

  ```python
  # Sorting the DataFrame based on "Meals" column
  # Will sort from lowest to highest if no other parameter is passed
  meals_taxes_df = taxes_df.sort_values("Meals")
  meals_taxes_df.head()
  ```

* The "ascending" parameter is always marked as `True` by default. Therefore, the `sort_values` method will always sort from lowest to highest unless the parameter of `ascending=False` is also passed into the `sort_values` method:

  ```python
  # To sort from highest to lowest, ascending=False must be passed in
  meals_taxes_df = taxes_df.sort_values("Meals", ascending=False)
  meals_taxes_df.head()
  ```

* It’s also possible to sort the data based on values stored within multiple columns by passing a list of columns into the `sort_values` method as a parameter. The first column will be the primary sorting method, while the second column determines the row order when the first column has multiple rows with the same value.

  ```python
  # It is possible to sort based upon multiple columns
  meals_and_rent_count_df = taxes_df.sort_values(
      ["Meals Count", "Rent Count"], ascending=False)
  meals_and_rent_count_df.head(15)
  ```

  ![Sorting by meals and rent](https://static.bc-edx.com/ai/ail-v-1-0/m4/lesson_2/img/7-Census_Meals_Rent.png)

* This can be demonstrated by sorting on a different second column, "Alcohol Count," and comparing the order of the two rows where "Meals Count" has a value of "54" in each DataFrame.

  ```python
  # DataFrame with a second column sort on "Alcohol Count"
  # (Compare the order of the two "54" value Rent Count rows)
  meals_and_alcohol_count_df = taxes_df.sort_values(
      ["Meals Count", "Alcohol Count"], ascending=False)
  meals_and_alcohol_count_df.head(15)
  ```

  ![Sorting by meals and alcohol](https://static.bc-edx.com/ai/ail-v-1-0/m4/lesson_2/img/7-Census_Meals_Alcohol.png)

* An immensely helpful method when dealing with sorted DataFrames is the `df.reset_index` method. This method will recalculate the index for each row based on its position within the new DataFrame, and it will, therefore, allow for simpler row referencing in future.

* Passing `drop=True` into `df.reset_index()` will ensure that no new column is created when the index is reset as follows:

  ```python
  # The index can be reset to provide index numbers based on the new rankings.
  new_index_df = meals_and_alcohol_count_df.reset_index(drop=True)
  new_index_df.head()
  ```

Data Source: [Vermont Agency of Administration, Department of Taxes. Meals and Rooms Tax Statistics (2020 Multiple Periods Update, Calendar Year)](https://tax.vermont.gov/data-and-statistics/mrt)

### 5. Instructor Do: Exploring Data (15 min)

**Corresponding Activity:** [03-Ins_Exploring_Data](Activities/03-Ins_Exploring_Data)

Continue stepping through the slideshow, while you cover the following talking points:

When dealing with massive datasets, it’s difficult to understand the dataset yourself without doing

* Although these issues may seem insignificant, they can severely hinder the analysis and visualization of a dataset by skewing the data one way or another.

* Thankfully, Pandas includes methods for removing missing values, replacing duplicates, and changing values with relative ease.

* Open solution file within the Jupyter notebook, share the file, and run and discuss the code line by line with the class.

  * To delete a column of extraneous information from a DataFrame, use `del <DataFrame>[<Column>]`.

  * To figure out if any rows are missing data, simply run the `count()` method on the DataFrame and check that all columns contain equal values.

  * To drop rows with missing information from a DataFrame, use `<DataFrame>.dropna(how="any")`.

  * Sometimes, the rows containing "NaN" values should not be removed but should instead be filled with another value. In such cases, simply use the `<DataFrame>.fillna(value=<Value>)` method and pass the desired value into the parentheses.

  * To find similar or misspelled values, simply run the `value_counts()` method on the column in question and check the returned values.

  * To replace similar or misspelled values, simply run the `replace()` method on the column in question. Pass in a dictionary to the method. The keys will be searched for in the column and replaced with the values, as in the following image:

    ![Replace Values.](https://static.bc-edx.com/ai/ail-v-1-0/m4/lesson_2/img/M4-L2-replacing-values.png)

* To display a statistical overview of the DataFrame, use `df.describe()`.

* To calculate the individual aggregate functions per column, many functions are available. Show students the following examples:

```python
# We can calculate individual aggregate functions per column
print("AMOUNT:")
print(f"The count is {df['Amount'].count()}")
print(f"The minimum is {df['Amount'].min()}")
print(f"The maximum is {df['Amount'].max()}")
print(f"The mean is {df['Amount'].mean()}")
```

* Individual aggregates for the amount column are as follows:

```output
AMOUNT:
The count is 1818
The minimum is -1000
The maximum is 400000
The mean is 752.1276127612762
```

```python
# We can also calculate them for an entire DataFrame
df.max()
```

* df.max() reveals the maximum value from each column in the DataFrame.

```output
Name        ZWEIG, NATHANIEL
Employer                 ZWJ
City              ZANESVILLE
State                     WY
Zip              997230255.0
Amount                400000
dtype: object
```

Data Source: Federal Election Commission (2021). Contributions by individuals, 2021-2022. [Federal Election Commission](https://www.fec.gov/data/browse-data/?tab=bulk-data), extracted, reduced, and modified in Pandas.

-->

### 6. Student Do: Search for the Worst (20 min)

**Corresponding Activity:** [04-Stu_SearchForTheWorst](Activities/04-Stu_SearchForTheWorst)

Continue through the slideshow, using the next slides to accompany this activity.

This activity will help familiarize students with selecting data from a DataFrame, sorting it, and finding basic summary statistics.

In this activity, students will take a dataset on San Francisco Airport's utility consumption and answer questions based on the dataset.

-->

### 7. Review: Search for the Worst (15 min)

**Corresponding Activity:** [04-Stu_SearchForTheWorst](Activities/04-Stu_SearchForTheWorst)

Share the file and go over the solution with the class, answering whatever questions students may have.

Cover the following key points during the discussion:

* To collect a list of the unique values in the Utility DataFrame, use the following code:

```python
# Collect a list of all the unique values in "Utility"
consumption_df["Utility"].unique()
```

* To create a new DataFrame that only includes electricity usage for tenant-owned units, use the following code:

```python
# Create a new DataFrame that only includes electricity usage for tenant owned units.
electricity_df = consumption_df.loc[(consumption_df["Utility"] == "Electricity") &
                                    (consumption_df["Owner"] == "Tenant"), :]
electricity_df.head()
```

* To sort the DataFrame by the values in the “Usage” column to find the months with the highest usage, use the following code:

```python
# Sort the DataFrame by the values in the "Usage" column to find the months
# with the highest usage
electricity_df = electricity_df.sort_values(by="Usage", ascending=False)

# Reset the index so that the index is now based on the sorting locations
electricity_df = electricity_df.reset_index(drop=True)

electricity_df.head()
```

* To save all of the information collected on the highest-usage month, use the following code:

```python
# Save all of the information collected on the highest-usage month
highest_month = electricity_df.iloc[0, :]
highest_month
```

* To show basic summary statistics for the whole DataFrame:

```python
# Show some basic summary statistics for the whole DataFrame
electricity_df.describe()
```

* To find the average usage, use the following code:

```python

# Find the average usage
electricity_df['Usage'].mean()
```

To find the total usage from all Augusts on record, use the following code:

```python
# Find the total usage from all Augusts on record

electricity_df.loc[electricity_df['Month'] == 'Aug', 'Usage'].sum()
```

---

### 8. Break (15 minutes)

---

### 9. Instructor Do: Intro to NumPy and SciPy (10 min)

Continue using the slideshow to accompany this demonstration.

Explain to students the importance of statistics when it comes to AI and machine learning. AI and machine learning rely on large amounts of data, finding patterns within the data, and making predictions based on the data gathered. Statistics, the practice of collecting and analyzing numerical data, is foundational in the development, training, and evaluation of machine learning models. Metrics used within machine learning algorithms such as accuracy, precision, f-scores, z-scores, root mean squared errors, mean, median, and mode, are all part of statistical analysis, providing information on datasets.

Ensure that students understand that an expert knowledge of statistics isn’t required to use machine learning. Many machine learning models can be set up without any mathematical background at all! The key is that machine learning inputs and outputs are difficult to interpret without statistics. If you don’t understand the statistics, it’s likely that you will sometimes miss problems in your model or in the model’s results, which can lead to faulty conclusions. While training models without a background in math and statistics is becoming more and more common, the better you understand math and statistics, the better off you’ll be in every phase of your career.

#### NumPy

Explain that NumPy, which is short for Numerical Python, is a library in Python that is used for working with arrays and matrices, and is built on linear algebra. The arrays may have one dimension, which represents vectors; two dimensions, which represent matrices; and any further dimensions represent tensors. NumPy is also useful in performing high-level mathematical functions on arrays.

The standard Python library uses lists instead of arrays. However, NumPy’s arrays are considerably faster than Python’s lists, and the improvement in speed makes it perfect for its use in machine learning.

NumPy is imported as follows:

```python
import numpy as np
```

#### SciPy

Explain that SciPy, or Scientific Python, is a library in Python that relies on NumPy’s arrays to perform computations. SciPy contains optimized functions and provides algorithms for optimization, interpolation, algebraic equations, and statistics, to name a few.

SciPy is imported as follows:

```python
import scipy as sp
```

Answer any questions before moving on.

### 10. Instructor Do: Central Tendency (15 min)

Continue using the slideshow to accompany this demonstration.

* Begin by explaining that even the most sophisticated statistical methods can fail if we don't apply them correctly. Before conducting a final analysis, we gather basic information about the data, like the averages and ranges. These measures, known as **descriptive statistics**, provide a window into potential pitfalls, outliers, or insights that might exist for our data. People often refer to this process of getting to know the dataset as **exploratory data analysis (EDA)**.

* Use the slides to help you while covering the measures of central tendency.

* First, ask students to name a measure of central tendency.

* Explain that measures of central tendency try to identify the center of a dataset and that many variations exist.

  * Highlight the fact that the most common measures of central tendency are the **mean, median, and mode**.

  * The **mean** of a dataset is its arithmetic average. We calculate it by summing all the numbers in the dataset and then dividing that sum by the number of elements in the dataset.

  * The **median** of a dataset is the middle element. We calculate it by listing the data in numerical order and then selecting the middle element. For even-length datasets, the median is the average of the two center elements.

  * The **mode** of a dataset is the element that occurs the most frequently. We can use the mode for either numerical or categorical data. It’s possible for one dataset to have multiple modes.

* Python offers several ways to measure the central tendency of a dataset. But for this module, we’ll primarily use the NumPy and SciPy packages.

  * We’ll use NumPy to test for the mean and the median. Because NumPy doesn’t have a function for the mode, we'll use SciPy to test for that.

  * SciPy has functions for the mean, median, and mode, and was built as an extension to the NumPy codebase. However, NumPy is significantly faster than SciPy and more compatible with other libraries, like Pandas. So, we prefer NumPy when multiple options for the same function exist.

  * Explain that Pandas also provides functions to measure the central tendency. For instance, the students used the `mean` function on a `groupby` object in a previous module.

  * Tell students that we’ll now examine a few example datasets to find out how the mean, median, and mode can help us describe different data distributions.

* Explain to the students that the first example dataset contains the number of cup holders in 20 vehicles that were surveyed in a school parking lot.

  ![A screenshot depicts a normally distributed graph.](https://static.bc-edx.com/ai/ail-v-1-0/m4/lesson_2/img/M4-L2-measure-central-tendency-ex-1.png)

* In this example, all three measures of central tendency have about the same value.

* The mean is calculated by adding up the number of cup holders (82 in total) and dividing by the number of vehicles (20), which equals 4.1.

* The median is for as it is the central value of the number of cup holders.

* The mode is also 4, since it is the most frequent number of cup holders that the cars surveyed had.

  * Any of the three measures of central tendency effectively describes the center of the data.

* Explain that the second example dataset contains the 10 employee salaries at a small, family-owned car dealership, as the following image shows:

   ![A screenshot depicts a distribution that specifies the mean, median, and mode for the company salary dataset.](https://static.bc-edx.com/ai/ail-v-1-0/m4/lesson_2/img/M4-L2-measure-central-tendency-ex-2.png)

  * Point out that the mean of the dataset no longer effectively describes the center of the data.

  * Explain that the mean of a dataset is more susceptible to shifting compared to the mode and median because of extreme values.

  * In this example, the salaries of $100,000 and $200,000 are disproportionately larger than the rest of the salaries. We consider these salaries to be **outliers**.

* Outliers are data points that differ considerably from the rest of the observations.

  * Point out that the median salary is $24,500, which is more meaningful and descriptive than the mean.

  * Ask the students why the median can effectively describe the center of the data, but the mean can’t.

  * The reason is that the median considers only the center of a sorted dataset, whereas the mean considers every value in the dataset.

  * Explain that when a dataset is large or has no extreme values, the mean and the median are usually very close. When the dataset is smaller or has extreme values, the mean and the median usually differ.

* Explain that the third example dataset contains the amount of rainfall per month at an airport over the course of a year.

  * Ask students which measure of central tendency they believe best describes the center of the data and why.

  * This dataset contains rainfall amounts. And, an infinite number of possibilities exists for the amount of rainfall per month. It’s thus unlikely that any values repeat in the dataset. So, the mode will fail to describe the dataset.

  * We can use the mean or the median to describe the center of this dataset. Ask students how the interpretations of the two metrics might differ.

  * Emphasize that the mean will be more likely to be skewed by outliers while the median will be more resistant to outliers.

  * Explain that the median is typically the safest measure of central tendency to use when we’re uncertain about either the origin of the data or the questions that people want the data to answer. However, caution students that when people ask for the average of the data, they’re most likely referring to the mean.

* Ask students if they can define variance, standard deviation, and z-score.

* Explain that we use the variance, standard deviation, and z-score to help us understand two things about a dataset. The first concerns the differences and the amount of variation within a dataset. The second concerns whether a particular point in that dataset markedly differs from the other points.

* Continue using the slides as you cover the variance, standard deviation, and z-score.

  * Explain that the **variance** describes how far the values in a dataset are from the mean overall. It describes how much variation exists within the data.

    * Reassure students that it’s not critical to know how to manually calculate the variance. Almost all analytical tools and programming languages have functions to do that for us.

    * Explain that the most important takeaway from the equation is that the variance calculation considers the distance of each value in the dataset from the center of the data.

    * Point out that it doesn’t matter if a value is higher or lower than the mean of the dataset. Because the formula squares the difference, the variance is always positive.

  * Next, explain that in statistics, we use the **standard deviation** to interpret how spread out the data is from its mean.

    * Define standard deviation as simply the square root of the variance. Most analytical tools and programming languages have functions to directly calculate standard deviation.

    * Point out that by calculating the square root of the variance, the standard deviation describes the variability of the data by using the same unit as the mean (and the data itself).

  * Finally, explain that we can calculate the **z-score** of an individual data point to measure its distance from the mean in terms of standard deviations.

    * A z-score differs from the variance and the standard deviation in that we calculate it for a single point and not for the dataset as a whole.

#### 11. Instructor Do: Summary Statistics (15 min)

**Corresponding Activity:** [05-Ins_Summary_Statistics](Activities/05-Ins_Summary_Statistics/)

In this demonstration, you’ll use Python to calculate summary statistics.

To do this demo, complete the following steps:

1. Share your screen, and open the solution file.

2. Import the dependencies, and then read the data into Pandas, as the following code shows:

    ```python
    import numpy as np
    import pandas as pd
    import scipy.stats as sts

    temperature_df = pd.read_csv('../Resources/lax_temperature.csv')
    temperatures = temperature_df['HourlyDryBulbTemperature']
    ```

    * Explain to the students that this first dataset contains National Oceanic and Atmospheric Administration (NOAA) temperature measurements that were taken at the Los Angeles International Airport (LAX). This dataset has over 3,000 data points.

3. Use NumPy to calculate the mean and the median, and use SciPy to calculate the mode, as the following code shows:

    ```python
    mean_numpy = np.mean(temperatures)
    print(f"The mean temperature at the LAX airport is {mean_numpy}")

    median_numpy = np.median(temperatures)
    print(f"The median temperature at the LAX airport is {median_numpy}")

    mode_scipy = sts.mode(temperatures)
    print(f"The mode temperature at the LAX airport is {mode_scipy}")
    ```

    * Explain that to calculate the mode, the `scipy.stats` module returns two arrays: one for the mode values and the other for the frequency of each mode.

4. Use NumPy to calculate the variance and the standard deviation of the population, as the following code shows:

    ```python
    variance = np.var(temperatures)
    print(f"The population variance using the NumPy module is {variance}")

    stand_dev = np.std(temperatures)
    print(f"The population standard deviation using the NumPy module is {stand_dev}")
    ```

5. Use SciPy to calculate the z-scores of the temperatures, as the following code shows:

    ```python
    z_scipy = sts.zscore(temperatures)
    print(f"The z-scores using the SciPy module are {z_scipy}")
    ```

    * Remind the students that the z-score of a data point is the number of standard deviations that it is from the mean of the dataset.

    * Point out that `stats.zscore` will output a list of z-scores that’s equal in length to the list of temperatures. If we want to know the z-score for any value, we must first find the index of that value in the temperature list. We then use that index to find the z-score in the `stats.score` output list.

Send out the solution  file for the students to refer to later.

### 12. Instructor Do: Intro to Quartiles and Outliers (15 min)

**Corresponding Activity:** [06-Ins_Quartiles_and_Outliers](Activities/06-Ins_Quartiles_and_Outliers/)

Continue using the slideshow to accompany this demonstration.

* Now that you’ve covered the measures of central tendency, let students know that they'll learn about a few other summary statistics. These summary statistics&mdash;quantiles, quartiles, and outliers&mdash;will help them explore and describe a new dataset.

* Use the slides to help you cover this section.

* Explain to students the significance of why we are interested in quartiles, percentiles, and outliers. In an AI and machine learning context, it’s important to be able to identify and remove outliers in a dataset during the data cleaning and preprocessing phases. Since outliers are data points that differ significantly from the rest of the dataset, they have the tendency to skew the data. This may lead to less effective machine learning models. To begin identifying outliers, there are a few concepts that we need to understand.

* Begin this section by asking if anyone can define quantiles, quartiles, percentiles, and outliers.

  * **Quantiles** are values that divide sorted data into well-defined bins based on the position of each point. The two most commonly used quantiles are quartiles and percentiles.

  * **Quartiles** are the three values that divide the sorted data into four equally sized groups. Thus, 25% of the data values are less than the first quartile, 50% are less than the second quartile, and 75% are less than the third quartile. The second quartile is also the median.

  * **Percentiles** divide the sorted data into 100 equally sized groups. Each percentile is named for the percentage of data values that are less than that percentile. For example, 57% of the data values are less than the 57th percentile.

  * **Outliers** are extreme values in a dataset. Several methods exist to identify outliers, such as visual identification through scatter plots, box plot graphs, histograms, statistical tests, and the **interquartile range (IQR)** technique. For this course, we will focus on the IQR technique. This method involves finding values that are 1.5 &times; the IQR: either greater than the third quartile or less than the first quartile.

  * The **IQR** is the range between the first and the third quartile.

### 12. Instructor Do: Quartiles and Outliers Introduction (15 min)

In this demonstration, you’ll use Python to calculate quartiles and outliers.

To do this demo, complete the following steps:

1. Share your screen, and open the solution file.

2. Import the LAX temperatures dataset, and then save the HourlyDryBulbTemperature column to a variable.

    ```python
    temperature_df = pd.read_csv('../Resources/lax_temperature.csv')
    temperatures = temperature_df['HourlyDryBulbTemperature']

    ```

    * Explain that in this example, we're referring back to the LAX temperatures from NOAA.

    * Explain that we can also identify potential outliers by using Pandas.

    * Explain that with Pandas, we can easily calculate the IQR to generate the outlier boundaries.

3. Use Pandas to find potential outliers by calculating the IQR, as the following code shows:

    ```python
    # Use Pandas to find potential outliers by calculating the interquartile range (IQR)
    Q1 = temperatures.quantile(0.25)
    median = temperatures.quantile(0.5)
    Q3 = temperatures.quantile(0.75)
    IQR = Q3 - Q1

    print(f"The lower quartile of temperatures is: {Q1}")
    print(f"The upper quartile of temperatures is: {Q3}")
    print(f"The interquartile range of temperatures is: {IQR}")
    print(f"The the median of temperatures is: {median} ")

    lower_bound = Q1 - (1.5 * IQR)
    upper_bound = Q3 + (1.5 * IQR)
    print(f"Values below {lower_bound} could be outliers.")
    print(f"Values above {upper_bound} could be outliers.")
    ```

    * In the preceding code, show the students how to use the Pandas `quantile` function to calculate the first quartile, the median, and the third quartile. Point out that, by definition, the median is equivalent to the 0.5 quantile (otherwise known as the second quartile or the 50th percentile).

    * Point out that the Pandas `quantile` function requires decimal values between 0 and 1.

    * Point out that once we calculate the IQR, we can calculate the outlier boundaries. We can then quantitatively determine any potential outliers.

4. Use Pandas to create a DataFrame of rows that could be outliers.

    ```python
    # Create a DataFrame of rows that could be outliers
    outlier_df = temperature_df.loc[(temperature_df['HourlyDryBulbTemperature'] < 45) |
                                    (temperature_df['HourlyDryBulbTemperature'] > 69)]
    outlier_df.head()

5. Use the len function to determine how many outliers were identified.

    ```python
    # How many potential outliers are there in the dataset?
    len(outlier_df)
    ```

Send out the solution file for the students to refer to later.

Answer any questions before moving on.

### 12. Student Do: Summary Statistics (15 min)

**Corresponding Activity:** [07-Stu_Summary_Stats](Activities/07-Stu_Summary_Stats)

Continue through the slideshow, using the next slides as an accompaniment to this activity.

This activity will give students some practice in the calculation of the mean, median, and mode. Thereafter, they will import a CSV file, determine central tendency of a population, identify any outliers through code, create a DataFrame of the outliers, and find maximum and minimum values.

### 13. Review: Summary Statistics (10 min)

**Corresponding Activity:** [07-Stu_Summary_Stats](Activities/07-Stu_Summary_Stats)

Share and go over the solution file with the class, answering whatever questions students may have.

Cover the following key points during the discussion:

Open the solution file, and then step through the solution as follows:

1. Calculate the mean, median, and mode for the cups of coffee that are consumed daily per employee, as the following code shows:

    ```python
    print("Mean: ", np.mean(coffee_consumed.cups))
    print("Median: ", np.median(coffee_consumed.cups))
    print("Mode: ", sts.mode(coffee_consumed.cups))
    ```

    * Show that although the mean is around 1.5 cups of coffee per day, the mode shows that the largest group consists of those who don’t drink coffee. This analysis shows that instead of focusing on how much coffee to provide, this office might provide additional, non-coffee  options.

    * Emphasize that this is another example of why separately checking the mean, median, and mode is useful.

2. Read the California housing dataset into Pandas, as the following code shows:

    ```python
    california_data = pd.read_csv('../Resources/California_Housing.csv')
    california_data.head()
    ```

3. Calculate the mean, median, and mode of the population, and then create a histogram, as the following code shows:

    ```python
    print("Population Mean: ", california_data["Population"].mean())
    print("Population Median: ", california_data["Population"].median())
    print("Population Mode: ", california_data["Population"].mode())
    ```

    * Mention that the solved version of the notebook uses the Pandas functions for calculating the mean, median, and mode instead of using NumPy. Either method will return the same answers, but remind students that the Pandas functions  only work on Pandas objects.

    * Highlight the fact that housing sale data would normally be skewed right as there are a few houses that sell for much more money, so the median is arguably the most appropriate. A **skew** is an imbalance between the data on the right side and the data on the left side of the peak in a distribution. If the distribution stretches further to the right than to the left, we call the data **right skewed**.

    * Mention that we can verify that the data is skewed, because the mean and the median are far apart&mdash;1388 vs. 1153.

4. Determine if any potential outliers exist in the data for the average home occupancy in California, as the following code shows:

    ```python
    avg_occup = california_data["AveOccup"]
    Q1 = avg_occup.quantile(0.25)
    median = avg_occup.quantile(0.5)
    Q3 = avg_occup.quantile(0.75)
    IQR = Q3 - Q1

    print(f"The lower quartile of occupancy is: {Q1}")
    print(f"The upper quartile of occupancy is: {Q3}")
    print(f"The interquartile range of occupancy is: {IQR}")
    print(f"The median of occupancy is: {median} ")

    lower_bound = Q1 - (1.5 * IQR)
    upper_bound = Q3 + (1.5 * IQR)
    print(f"Values below {lower_bound} could be outliers.")
    print(f"Values above {upper_bound} could be outliers.")
    ```

    The preceding code produces the following output:

    ```text
    The lower quartile of occupancy is: 2.4250909806040477
    The upper quartile of occupancy is: 3.2974592743428355
    The interquartile range of occupancy is: 0.8723682937387878
    The the median of occupancy is: 2.81970199317512 
    Values below 1.116538539995866 could be outliers.
    Values above 4.606011714951017 could be outliers.
    ```

    * Explain that because the data is too vast to visually examine, we can use the 1.5 &times; IQR rule to identify potential outliers in the dataset.

5. Create a new DataFrame by filtering the original DataFrame to show only the outliers, as the following code shows:

    ```python
    outlier_occupancy = california_data.loc[(avg_occup < lower_bound) | (avg_occup > upper_bound)]
    outlier_occupancy
    ```

    * Once we have the lower and upper outlier bounds, we use Pandas to filter the data. Show the preceding code, which filters the DataFrame by using `loc`. Then show the output DataFrame of the outliers, as the following image shows:

      ![A screenshot depicts the filtered housing DataFrame.](https://static.bc-edx.com/ai/ail-v-1-0/m4/lesson_2/img/02-population_outlier_DataFrame.png)

    * Point out that 100 potential outliers exist in the average-occupancy data.

6. Find the minimum and maximum median-income values of all the potential outliers, as the following code shows:

    ```python
    print(f"The minimum median income of the potential outliers is {outlier_occupancy['MedInc'].min()}")
    print(f"The maximum median income of the potential outliers is {outlier_occupancy['MedInc'].max()}")
    ```

    * Point out that once we have the filtered DataFrame, we can use the `min` and `max` functions on the “MedInc” column (of median-income values) to determine the minimum and maximum values.

### 14. Everyone: Pandas Recap (30 minutes)

**Corresponding Activity:** [08-Evr_Pandas_Recap](Activities/08-Evr_Pandas_Recap)

Continue using the slideshow to accompany this demonstration.

Continue stepping through the slideshow, while you cover the following talking points for this section:

This activity will recap what we have covered in Pandas up to this point.

Open the unsolved notebook.

* Go through the cells within the unsolved version of the Jupyter notebook, and have the class help you create the code to accomplish the tasks listed within the comments.

* If students are struggling, feel free to refer to solution file to help keep the class on track.

* Upon reaching the final section, let the class know that this DataFrame has a small problem: The date and time columns are being stored as objects.

* A list of a DataFrame's data types can be checked by accessing its `dtypes` property, as captured in the following image:

  ![Pandas Recap - DataTypes.](https://static.bc-edx.com/ai/ail-v-1-0/m4/lesson_2/img/5-PandasRecap_DataTypes.png)

* With the date columns stored as objects, it is currently impossible to perform any form of calculation on any columns with date data. Luckily, Pandas includes a way to easily change a column's data type.

* To change a non-numeric column to a numeric column, use the `df.astype` method and pass in the desired data type as the parameter as the following code shows:

  ```python
  # Convert relevant date columns to datetime
  loss_df = loss_df.astype({"Alarm Date and Time": "datetime64",
                          "Arrival Date and Time": "datetime64",
                          "Last Unit Cleared Date and Time": "datetime64"})
  loss_df.dtypes
  ```

### 15. End Class (5 min)

Congratulate students on completing this lesson. Ask how they feel about data exploration up until this point.

Remind students what they learnt in this lesson: sorting values within a DataFrame, cleaning data, the use of certain functions, introduction to the NumPy and SciPy libraries, measures of central tendency and how to ascertain them, and the removal of outliers in DataFrames.

Let students know that, in the lesson that follows, they will learn how to perform mathematical operations on columns within a DataFrame, format and replace text, create new columns, and use the apply() feature to transform columns.

**Reflection and Feedback:** At the end of each day or module, encourage students to reflect on what they've learned and provide an avenue for them to give feedback. This could be a quick survey, a discussion forum, or an open-ended questionnaire.

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
