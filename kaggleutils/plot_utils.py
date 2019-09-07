from math import sqrt, ceil
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

w = 10
h = 10


def get_grid_shape(n):
    h = int(sqrt(n))
    w = int(ceil(n / h))
    return w, h


def plot_img_grid(images):
    n = len(images)
    w, h = get_grid_shape(n)
    fig = plt.figure(figsize=(8, 8))
    for i in range(n):
        # Show image
        ax = fig.add_subplot(h, w, i + 1)
        ax.axis("off")
        ax.set_aspect("equal")
        # Fix the images if it has only 1 channel
        if images[i].ndim == 3 and images[i].shape[-1] == 1:
            images[i] = images[i].squeeze(axis=-1)

        cmap = "gray" if images[i].ndim == 2 else None
        # print(f'Shape -- {images[i].shape}  Cmap -- {cmap}')
        plt.imshow(images[i], cmap=cmap)

    plt.subplots_adjust(wspace=0.01, hspace=0)
    plt.show()


def plot_img_lists(*image_lists):
    assert all(len(images) == len(image_lists[0]) for images in image_lists)
    n = len(image_lists[0])
    flat_image_lists = [img for img_set in zip(*image_lists) for img in img_set]
    plot_img_grid(flat_image_lists)
