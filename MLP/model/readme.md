# Understanding what is Neural Networks?

<table align="center">
<tr>
<td width="50%" style="vertical-align:middle; padding-right:20px;">

Artificial neural network work: We feed a set of input data and based on this input data the network will recognize patterns in it and make output predictions for new data.

</td>
<td width="50%" align="center">

<img 
src="readme_imgs/pic1.png" 
width="100%" 
style="border:3px solid #4CAF50; border-radius:12px;">

</td>
</tr>
</table>

## For Example

<table align="center">
<tr>

<td width="50%" style="vertical-align:middle; padding-right:20px;">
If we pass a set of apple and orange images into the network, the network will try to recognize patterns inside these images.
</td>

<td width="50%" align="center">
<img 
src="readme_imgs/pic2.png" 
width="100%" 
style="border:3px solid #4CAF50; border-radius:12px;">
</td>

</tr>
</table>

---

<table align="center">
<tr>

<td width="50%" style="vertical-align:middle; padding-right:20px;">
The network will then try to recognize patterns stored inside these images.
</td>

<td width="50%" align="center">
<img 
src="readme_imgs/pic3.png" 
width="100%" 
style="border:3px solid #4CAF50; border-radius:12px;">
</td>

</tr>
</table>

---

<table align="center">
<tr>

<td width="50%" style="vertical-align:middle; padding-right:20px;">
Based on the learned patterns, it will make predictions for new images that it has never seen before.
</td>

<td width="50%" align="center">
<img 
src="readme_imgs/pic4.png" 
width="100%" 
style="border:3px solid #4CAF50; border-radius:12px;">
</td>

</tr>
</table>

# What is neuron?

<table align="center">
<tr>

<td width="50%" align="center">
<img 
src="readme_imgs/pic5.png" 
width="100%" 
style="border:3px solid #4c53af; border-radius:12px;">
</td>

<td width="50%" style="vertical-align:middle; padding-left:20px;">
A neuron is a function that produces an output value. This output value can be anything, but it is usually small and between 0 and 1.
</td>

</tr>
</table>

<br>

<table align="center">
<tr>

<td width="50%" align="center">
<img 
src="readme_imgs/pic6.png" 
width="100%" 
style="border:3px solid #4c53af; border-radius:12px;">
</td>

<td width="50%" style="vertical-align:middle; padding-left:20px;">
Different neurons store different values inside them, and these different values are responsible for recognizing different patterns in different regions.
</td>

</tr>
</table>
 
## For example

There may be some neurons which hold some numbers that are responsable for recognizing red color in an image of apple. And there maybe some other neurons for recognizing orange color in the image of orange.

<p align="center">
  <img src="readme_imgs/pic7.png" width="45%" 
       style="border:3px solid #4c53af; border-radius:12px; margin-right:10px;">
  <img src="readme_imgs/pic8.png" width="45%" 
       style="border:3px solid #4c53af; border-radius:12px;">
</p>

So when we feed an image of apple some neurons get activated and when we feed an image of an orange other neurons will get activated!

Due to these activations on neurons **we can also call these neurons as activations** and as these are the functions **we can call them activation functions.**

<p align="center">
  <img src="readme_imgs/pic9.png" width="45%" 
       style="border:3px solid #4c53af; border-radius:12px; margin-right:10px;">
  <img src="readme_imgs/pic10.png" width="45%" 
       style="border:3px solid #4c53af; border-radius:12px;">
</p>

<hr>
<p align="center">
Collection of these neurons forms layers. A neural network is divided into three types of layers: input layer, hidden layer and output layer.
</p>

<p align="center">
  <img 
    src="readme_imgs/pic11.png" 
    width="55%"
    style="border: 3px solid #4c53af; border-radius: 12px;">
</p>


<table align="center">
<tr>

<td width="50%" align="center">
<img 
src="readme_imgs/pic13.png" 
width="100%" 
style="border:3px solid #4c53af; border-radius:12px;">
</td>

<td width="50%" style="vertical-align:middle; padding-left:20px;">
Input layer has the neurons which holds the value from the dataset. So number of neurons in the input layer will be equal to the number of features we have in our input data.</td>

</tr>
</table>

<table align="center">
<tr>

<td width="50%" style="vertical-align:middle; padding-left:20px;">
On this final output can only can be an apple or orange. Thus the output layer will have one neuron. Which holds a value between 0 to 1 showing the probability of an image an being apple or an orange.</td>

<td width="50%" align="center">
<img 
src="readme_imgs/pic14.png" 
width="100%" 
style="border:3px solid #4c53af; border-radius:12px;">
</td>

</tr>
</table>

<table align="center">
<tr>

<td width="35%" align="center">
<img 
src="readme_imgs/pic15.png" 
width="100%" 
style="border:3px solid #4c53af; border-radius:12px;">
</td>

<td width="50%" style="vertical-align:middle; padding-left:20px;">
The hidden layers are responsable for holding a patterns in them.
</td>
</tr>
</table>

- It is possible here that first layer is responsible for finding the shape of the content of the image
- And second layer might be recognizing the color in the central region. And some neurons will be activated for red color while the other with orange.

### Connection between every pair of neurons are called weights

There is one connection between every two pair of the neurons and we assign a weight value to every pair of the two neurons. We call them weights because they determine how much weight should we be puttin or how much emphasis should be given to a certain region or certain patterns that we recognizing.

<table align="center">
<tr>

<td width="60%" align="center">
<img 
src="readme_imgs/pic16.png" 
width="100%" 
style="border:3px solid #4c53af; border-radius:12px;">
</td>

<td width="50%" style="vertical-align:middle; padding-left:20px;">
This can be done with weighted sum. Weighted sum is when we multiply every wieght within every value of the neuron and take itself.</td>
</tr>
</table>

Let's say this neuron responsible for recognizing the color in the central region of the image. Now our wighted sum will be high if the color in the central 