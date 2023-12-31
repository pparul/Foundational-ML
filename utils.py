from sklearn.datasets import make_blobs
from keras.utils import to_categorical
import numpy as np
from autograd import grad 
from autograd import numpy as np
from autograd import value_and_grad 
import matplotlib.pyplot as plt


## Adapted from 

### PYTEST FUNCTIONS ####

def square(x: float) -> float:
    return x * x
    #pass




def gen_plot_varaiables(weight_1,weight_2, g):
    # run gradient descent on mesh grid
    w1_vals, w2_vals = np.meshgrid(weight_1,weight_2)
    w1_vals.shape = (len(w1_vals)**2,1)
    w2_vals.shape = (len(w2_vals)**2,1)
    h = np.concatenate((w1_vals, w2_vals), axis =1)
    func_vals = np.asarray([g(np.reshape(s, (2,1))) for s in h])
    w1_vals.shape = (len(weight_1),len(weight_2))
    w2_vals.shape = (len(weight_2),len(weight_1))
    func_vals.shape = (len(weight_1),len(weight_2))
    return w1_vals, w2_vals, func_vals


def plot_contour_plots(w1_vals, w2_vals, weight_history, func_vals, alpha_choice):    
    plt.figure(figsize = (8,3))
    plt.contourf(w1_vals, w2_vals, func_vals)
    plt.colorbar()
    plt.title(f'learning rate: {alpha_choice}')
    
    for j in range(len(weight_history)):
        w_val = weight_history[j] # the results from Gradient descent and starting from an initial value 
        plt.scatter(w_val[0], w_val[1],  marker='o', s=50, c='r')
    
        if j > 0:
                    pt1 = weight_history[j-1]
                    pt2 = weight_history[j]
                    
                    # produce scalar for arrow head length
                    pt_length = np.linalg.norm(pt1 - pt2)
                    head_length = 0.1
                    alpha = (head_length - 0.35)/pt_length + 1
                    
                    # if points are different draw error
                    if np.linalg.norm(pt1 - pt2) > head_length:
                        if np.ndim(pt1) > 1:
                            pt1 = pt1.flatten()
                            pt2 = pt2.flatten()
                            
                        # draw color connectors for visualization
                        w_old = pt1
                        w_new = pt2
                        plt.arrow(w_old[0],w_old[1],w_new[0]-w_old[0],w_new[1]-w_old[1],length_includes_head=True,head_width=0.05, head_length=0.01)

    

def gradient_descent(g,alpha_choice,max_its,w):
    gradient = value_and_grad(g)

    # run the gradient descent loop
    weight_history = []      # container for weight history
    cost_history = []        # container for corresponding cost function history
    alpha = 0
    for k in range(1,max_its+1):
        # check if diminishing steplength rule used
        if alpha_choice == 'diminishing':
            alpha = 1/float(k)
        else:
            alpha = alpha_choice
        
        # returns gradient dJ/dw and cost function J evaluated at current w
        cost_eval,grad_eval = gradient(w)
        weight_history.append(w)
        cost_history.append(cost_eval)

        # take gradient descent step
        w = w - alpha*grad_eval
            
    # collect final weights
    weight_history.append(w)
    # compute final cost function value via g itself (since we aren't computing 
    # the gradient at the final step we don't get the final cost function value 
    # via the Automatic Differentiatoor) 
    cost_history.append(g(w))  
    return weight_history,cost_history



def momentum(g,alpha_choice,max_its,w, beta):
    gradient = value_and_grad(g)
    weight_history = []      
    cost_history = []        
    alpha = 0

    h = np.zeros((np.shape(w)))
    for k in range(1,max_its+1):
        # check if diminishing steplength rule used
        if alpha_choice == 'diminishing':
            alpha = 1/float(k)
        else:
            alpha = alpha_choice
        
        cost_eval,grad_eval = gradient(w)
        weight_history.append(w)
        cost_history.append(cost_eval)

        #print(grad_eval)
        h = beta*h + (1-beta)*grad_eval
        w = w - alpha*h
        #print(w)

    # collect final weights
    weight_history.append(w)
    cost_history.append(g(w))  
    return weight_history,cost_history


