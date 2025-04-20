import matplotlib
matplotlib.use('Agg')
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import matplotlib.patches as patches
import os

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % tuple(int(x) for x in rgb)

def get_colors_kmeans(img, n_colors=10, filename="color_palette_kmeans.png"):
    img_array = np.array(img)
    print(f"Image array shape: {img_array.shape}")
    height, width, channels = img_array.shape
    pixels = img_array.reshape((height * width, channels))

    if channels >= 3:
        rgb_pixels = pixels[:, :3]
    else:
        print("Warning: Image has less than 3 channels (e.g., grayscale).")
        return None

    kmeans = KMeans(n_clusters=n_colors, random_state=0, n_init=10)
    kmeans.fit(rgb_pixels)
    cluster_centers_rgb = kmeans.cluster_centers_.astype(int)

    top_colors_rgb = [tuple(color) for color in cluster_centers_rgb]
    top_colors_hex = [rgb_to_hex(rgb) for rgb in top_colors_rgb]

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    y_pos = 0.9
    row_height = 0.08
    x_color = 0.1
    x_code = 0.4

    ax.text(x_color, 0.95, 'Color', fontsize=12, fontweight='bold')
    ax.text(x_code, 0.95, 'Color Code', fontsize=12, fontweight='bold')

    for i, hex_code in enumerate(top_colors_hex):
        rect = patches.Rectangle((x_color, y_pos - row_height), 0.2, row_height * 0.8, facecolor=hex_code, edgecolor='lightgray')
        ax.add_patch(rect)
        ax.text(x_code, y_pos - row_height / 2, hex_code, va='center', fontsize=10)
        y_pos -= row_height

    plt.tight_layout(rect=[0, 0.05, 1, 0.95])
    plot_filepath = os.path.join("static/plots", filename)
    plt.savefig(plot_filepath)
    plt.close(fig)

    return filename