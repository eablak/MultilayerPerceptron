# Cost Function

Cost function in machine learning is the error representation. It shows how our model is predicting compared to the actual values or output labels.

- Lesser the cost function more the accuracy
- Higher the cost function lesser the accuracy

## Different Cost function for different types of Problems

### 1) Regression or Linear Regression

Output can take any number.

<p align="center">
  <img 
    src="../readme_imgs/03_imgs/pic56.jpeg"
    width="90%"
    style="border: 3px solid #4c53af; border-radius: 12px;">
</p>

### 2) Binary Classification

<i>(Cost function for our project)</i>

Output can takes only 0 or 1 as its value.


<p align="center">
  <img 
    src="../readme_imgs/03_imgs/pic57.jpeg"
    width="90%"
    style="border: 3px solid #4c53af; border-radius: 12px;">
</p>

<i>For detailed explanation for how this function work you can check https://github.com/eablak/dslr/blob/main/readme_imgs/0002.jpg</i>

### 3) Multi-Class Classification




<table align="center">
<tr>
</td>
<td width="55%" align="center">

<img 
src="../readme_imgs/03_imgs/pic58.jpeg" 
width="100%" 
style="border:3px solid #4CAF50; border-radius:12px;">

</td>

<td width="50%" style="vertical-align:middle; padding-right:20px;">

Output can take many categories. Output label for the eighth observation are going to by given one-hot representation. One hot representation means there is a 1 at one position and 0 at the other positions.

</tr>
</table>

<p align="center">
  <img 
    src="../readme_imgs/03_imgs/pic59.jpeg"
    width="90%"
    style="border: 3px solid #4c53af; border-radius: 12px;">
</p>

### Summarization

<p align="center">
  <img 
    src="../readme_imgs/03_imgs/pic60.png"
    width="100%"
    style="border: 3px solid #4c53af; border-radius: 12px;">
</p>