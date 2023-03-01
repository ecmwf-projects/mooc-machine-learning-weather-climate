from sklearn.metrics import r2_score, mean_squared_error
import seaborn as sns
import tensorflow as tf
from tqdm.notebook import tqdm
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib import pyplot as plt

def scatter_plot(x,y,ax=None):
    ax = sns.regplot(x=x, y=y, ax=ax)
    r2 = r2_score(x, y)
    mse = mean_squared_error(x, y)
    ax.set_title(f'R2={r2:.2f}, MSE={mse:.2e}')
    return ax

# custom progress bar for long training
class tqdm_callback(tf.keras.callbacks.Callback):
    
    def __init__(self, num_epochs, desc, loss=None, val_loss=None):
        self.num_epochs = num_epochs
        self.desc = desc
        self.metrics = {'loss':loss, 'val_loss':val_loss}
    
    def on_train_begin(self, logs={}):
        self.epoch_bar = tqdm(total=self.num_epochs, desc=self.desc)
    
    def on_train_end(self, logs={}):
        self.epoch_bar.close()
        
    def on_epoch_end(self, epoch, logs={}):
        for name in self.metrics:
            self.metrics[name]  = logs.get(name, self.metrics[name])
        self.epoch_bar.set_postfix(mse=self.metrics['loss'], val_mse=self.metrics['val_loss'], refresh=False)
        self.epoch_bar.update()

        
        
#For memory, how to plot the difference (not used):
def plot():
    fig, ax = plt.subplots(nrows=2, sharex= True, figsize=(18, 12))
    plt.grid(False)
    im = ax[0].imshow(xhyb[2].T, 
               aspect = 'auto',
               origin = 'lower',
               interpolation = 'spline36',
               cmap = sns.diverging_palette(240, 60, as_cmap=True),
               extent = [0, dt*xhyb[2].shape[0], 0, Nx],
               vmin = -10,
               vmax = 15)
    divider = make_axes_locatable(ax[0])
    cax = divider.append_axes('right', size='2%', pad=0.2)

    fig.colorbar(im, cax=cax)
    ax[0].set_ylabel('Hybrid model variables')


    im = ax[1].imshow(xhyb[2].T-Xtest[2].T, 
               aspect = 'auto',
               origin = 'lower',
               interpolation = 'spline36',
               cmap = sns.color_palette("vlag", as_cmap=True),
               extent = [0, dt*xhyb[2].shape[0], 0, Nx],
               vmin = -10,
               vmax = 10)
    divider = make_axes_locatable(ax[1])
    cax = divider.append_axes('right', size='2%', pad=0.2)

    fig.colorbar(im, cax=cax)
    ax[1].set_ylabel('Hybrid - True')


    ax[1].set_xlabel('Time (MTU)')
    #ax[0].set_tick_params(direction='out', left=True, bottom=True)
