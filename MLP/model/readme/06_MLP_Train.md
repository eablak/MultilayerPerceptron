# MLP Train

## Step 1: Initialize Parameters

- We need to initialize the W parameters randomly, and B with zeros
- And as our Deep Neural network has L layers, we will repeat it for L-1 times, from Wl to  (not considering the input layer)

<table align="center">
<tr>
<td align="center">
<img src="../readme_imgs/06_imgs/pic76.png" width="400" style="border:3px solid #4c53af; border-radius:12px;">
</td>
<td align="center">
<img src="../readme_imgs/06_imgs/pic75.png" width="400" style="border:3px solid #4c53af; border-radius:12px;">
</td>
</tr>
</table>

## Step 2: Forward Propagations

Softmax activation function will be used only at the last (output) layer, while we will use ReLU for hidden layers.

<table align="center">
<tr>
<td align="center">
<img src="../readme_imgs/01_imgs/pic30.png" width="300" style="border:3px solid #4c53af; border-radius:12px;">
</td>
<td align="center">
<img src="../readme_imgs/06_imgs/pic77.png" width="280" style="border:3px solid #4c53af; border-radius:12px;">
</td>
</tr>
</table>

For f(x), you can use either tanh or ReLU activation function. But also use the derivative of the same for Backpropagation as well.


## Step 3: Cost Function


<table align="center">
<tr>
<td align="center">
<img src="../readme_imgs/06_imgs/pic78.png" width="400" style="border:3px solid #4c53af; border-radius:12px;">
</td>
</tr>
</table>


## Step 4: Backward Propagation

- For last layer, dZL will be AL - Y
- Except for last layer, we use a loop to implement backprop for other layers

<table align="center">
<tr>
<td align="center">
<img src="../readme_imgs/06_imgs/pic80.png" width="400" style="border:3px solid #4c53af; border-radius:12px;">
</td>
<td align="center">
<img src="../readme_imgs/06_imgs/pic81.png" width="500" style="border:3px solid #4c53af; border-radius:12px;">
</td>
</tr>
</table>


## Step 5: Update Parameters

<p align="center">
  <img 
    src="../readme_imgs/06_imgs/pic82.png" 
    width="35%"
    style="border: 3px solid #4c53af; border-radius: 12px;">
</p>


## Complete Model

We need to initialie parameters once, and after that, we will run the following a loop:

- forward_prop(x, parameters)
- cost_function(aL, y)
- backword_prop(x, y, parameters, forward_cache)
- parameters = update_parameters(parameters, gradients, learning_rate)