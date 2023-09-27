# Understanding behavior of various parameters of gradient descent algorithm
- I use AutoGrad Library [https://github.com/HIPS/autograd] to implement Gradient Descent
- The goal here is to study how:
    - Gradient Descent behaves when certain parameters are varied. Focus is on # of iterations and learning rate.
    - How to use Momentum to optimize or speed-up Gradient Descent.

#### Data
- x and y axis show the weights and contour surface shows the value of cost function.
- Convex function we are trying to minimize: g = lambda w: (a1 + np.dot(b1.T,w) + np.dot(np.dot(w.T,C1),w))[0]

#### Variation of learning rate

    Plot 1 for alpha = 0.01



    
![png](Gradient_Descent_files/Gradient_Descent_5_1.png)
    


    Plot 2 for alpha = 0.05



    
![png](Gradient_Descent_files/Gradient_Descent_5_3.png)
    


    Plot 3 for alpha = 0.1



    
![png](Gradient_Descent_files/Gradient_Descent_5_5.png)
    


    Plot 4 for alpha = 0.5



    
![png](Gradient_Descent_files/Gradient_Descent_5_7.png)
    


    Plot 5 for alpha = 1



    
![png](Gradient_Descent_files/Gradient_Descent_5_9.png)
    


## Observations:
1. Plot:1-If the learning rate is low the gradient descent takes a long time to reach the minimum <br>

2. Plot:3- As the learning rate is increasing we see zig-zag behavior of gradient descent 
    - zig-zag behavior slows learning down as it takes longer to reach the minimum. 
    - Plot-4: Learning rate of 1 is so high that GD completely diverges leading to very high cost function values as seen on y axis  <br>

#### Variation of # of iterations

    Plot 6 for # of iterations = 50



    
![png](Gradient_Descent_files/Gradient_Descent_8_1.png)
    


    Plot 7 for # of iterations = 100



    
![png](Gradient_Descent_files/Gradient_Descent_8_3.png)
    


    Plot 8 for # of iterations = 500



    
![png](Gradient_Descent_files/Gradient_Descent_8_5.png)
    


    Plot 9 for # of iterations = 1000



    
![png](Gradient_Descent_files/Gradient_Descent_8_7.png)
    


## Observations
- For a given learning rate as the # of iteration increase the gradient descent converges to the minimum value of the function.
- For Plot 6 # of iterations are not enough to reach the minimum. As we increase # of iterations for the same function the plot converges. 


## Plotting cost function


    
![png](Gradient_Descent_files/Gradient_Descent_11_0.png)
    


## Plotting surface of cost function




    <matplotlib.colorbar.Colorbar at 0x15d635360>




    
![png](Gradient_Descent_files/Gradient_Descent_13_1.png)
    


#### References
- Machine Learning Refined, 2nd Edition, Jeremy Watt, Reza Borhani, Aggelos K. Katsaggelos.
## Applying momentum to gradient descent

- Gradient Descent ethod experiences zig-zag behavior or oscillations in certain situatuions. 
    1)  High learning rate
    2)  Mini-batches: Because mini-batch gradient descent makes a parameter update after seeing just a subset of examples, the direction of the update has some variance, and so the path taken by mini-batch gradient descent will "oscillate" toward convergence. <br> 
<br>

- These oscillations can slow learning down and in some cases where learning rate is very high GD may diverge completely 

- We can solve this by using momentum that uses exponentially weighted averages as an underlying algorithm.
    1) Momentum takes into account the **past gradients** to smooth out the update. The 'direction' of the previous gradients is stored in the variable 𝑣.
    2)  $\beta$ is the weight of the previous data values and $1-\beta$ is the weight of the most recent values. 

#### Dataset
- Ford Dataset from - Machine Learning Refined, 2nd Edition, Jeremy Watt, Reza Borhani, Aggelos K. Katsaggelos.




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Open</th>
      <th>High</th>
      <th>Low</th>
      <th>Close</th>
      <th>Adj Close</th>
      <th>Volume</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1975-03-01</td>
      <td>1.070527</td>
      <td>1.248949</td>
      <td>1.062417</td>
      <td>1.204343</td>
      <td>0.002020</td>
      <td>48741400</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1975-04-01</td>
      <td>1.204343</td>
      <td>1.244894</td>
      <td>1.119188</td>
      <td>1.167848</td>
      <td>0.001958</td>
      <td>29854600</td>
    </tr>
  </tbody>
</table>
</div>



### Example of Exponential Weighted Average
- Trying different values of $\beta$ to see exponentially weighted average.




    <matplotlib.legend.Legend at 0x16d645f60>




    
![png](Momemtum_files/Momemtum_6_1.png)
    


### Apply exponential weighted average to Gradient Descent 
- Convex function we are trying to minimize: g = lambda w: (a1 + np.dot(b1.T,w) + np.dot(np.dot(w.T,C1),w))[0]
- We see the how # of iterations to reach the minimum reduce after using gradient descent

    Plot-1: GD with # of iterations = 50



    
![png](Momemtum_files/Momemtum_9_1.png)
    


    Plot-2: GD with # of iterations = 25



    
![png](Momemtum_files/Momemtum_10_1.png)
    


    Plot-3: GD with # of iterations = 25



    
![png](Momemtum_files/Momemtum_11_1.png)
    


## Observations
- After using momentum GD reaches mininimum faster (with lower number of iterations) at the same learning rate. 
- Plot 1 we reach minimum when # of iterations are 50 and in Plot -3 when momentum is used we reach minimum with 25 iterations

## References
- Machine Learning Refined, 2nd Edition, Jeremy Watt, Reza Borhani, Aggelos K. Katsaggelos.


