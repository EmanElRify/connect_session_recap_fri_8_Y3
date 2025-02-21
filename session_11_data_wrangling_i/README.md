# Session 11: Data Wrangling I

Welcome to Session 11! 🚀 <mark>This directory is your starting point for diving into the world of data wrangling, where the art of data gathering begins.</mark> Dealing with data turns the attention to learn about **<a href = "#datatype"><u>data types</u></a>**. I tried to include the most important points we discussed in the connect session. Hope you find this useful 😄


#### [Activity 11](https://docs.google.com/document/d/1RvZlvIKKEwLhtz-nHu-GfkDVNcJik9Ml/edit#heading=h.3dy6vkm)



#### Important modules and libraries to deal with data: <br>
- Numeric Data: Utilize `numpy` for numerical computations.
- ZIP Files: Manage compressed files with `zipfile`.
- Dataframes: Organize and analyze data using `pandas`. 

#### <span id = "datatype">Data types </span>
- zip 
- csv 
- images
- text files
- JSON
- Databases files


#### zipfile module 
> This module provides tools to create, read, write, append, and list a ZIP file
- To import the module : `import zipfile`
- To create a ZipFile object and open the file:<br> `zipfile_object = zipfile.ZipFile("filepath","mode")`
    - ***filepath***: the address where a file is stored on your computer
    - ***mode***: 
       - “r” : read an existing file.
       - “w”: write to a new file.
       - “x”: Exclusively create a new file (fails if the file already exists).
       - “a”: Append to an existing file.
- To extract all files from the zip file: <br>
`zipfile_object.extractall("path_of_extraction")`
    - ***path_of_extraction***: the address in which you want to extract files 
- You need to close the file after working on it : <br>
`zipfile_object.close()`
- Alternatively, you can use `with` statement to automatically close the file:<br>
```python
import zipfile
with zipfile.ZipFile("filepath", "mode") as zip_object:
    zip_object.extractall("path_of_extraction")
```
- to extract a specific file:
```python
import zipfile
with zipfile.ZipFile("filepath", "mode") as zip_object:
    zip_object.extract("file_to_extract_path", "path_of_extraction")
```
    
#### Some [Text Files extensions](https://www.file-extensions.org/filetype/extension/name/text-files):
- .txt
- .log
- .csv
- .md
- .JSON
- .yml
#### Important Documentation and resources:
| <img src="./images_and_icons/pandas.png" width = 70 > | <img src="./images_and_icons/zipfiles.png" width = 70 > |
| ----------- | ----------- |
| [Data Analysis with Pandas]("https://www.w3schools.com/python/pandas/pandas_analyzing.asp") | [ZipFile Object](https://docs.python.org/3/library/zipfile.html#zipfile-objects) |
| [Cleaning Empty Cells](https://www.w3schools.com/python/pandas/pandas_cleaning_empty_cells.asp) | [unzip compressed files](https://docs.python.org/3/library/zipfile.html#zipfile-objects:~:text=ZipFile.extract(member%2C%20path%3DNone%2C%20pwd%3DNone)%C2%B6') |
|[Cleaning Duplicates](https://www.w3schools.com/python/pandas/pandas_cleaning_duplicates.asp)|-|

#### Data Quality Assessment 
- Completeness
- Accuracy
- Validity
    - To search for data based on a condition (constraints):
    ```python
    sum(df[df["height"] < 100])
    ```
    - To drop these data:
    ```python
    df = df.drop(df[df['height'] < 100].index)
    ```
- Duplicates
    - To check if there are duplicated rows:
    ```python
    sum(df.duplicated())
    ```
    - To drop duplicated rows:
    ```python
    df.drop_duplicates(inplace=True)
    ```
    or 
    
    ```python
    df = df.drop_duplicates()
    ```
- Consistency

#### Research Keywords
- Read json files with Python
- Image analysis with Python (Image Processing - Computer Vision)
- Difference between DBMS and Spreadsheet





