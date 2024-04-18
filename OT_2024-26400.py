import numpy as np
import matplotlib.pyplot as plt


def visualize_rain(buildings, trapped_rain):
    x = np.arange(len(buildings))
    width = 0.35

    fig, ax = plt.subplots()

    bars1 = ax.bar(x, buildings, width, label='Building Height', color='black')

    bars2 = ax.bar(x, trapped_rain, width, label='Trapped Rain', color='skyblue', bottom=buildings)

    ax.set_xlabel('Building Index')
    ax.set_ylabel('Height')
    ax.set_title('Trapped Rain Visualization')
    ax.legend()
    plt.show()


def trapping_rain(buildings):
    total_height = 0
    trapped_rain = [0, ]
    for i in range(1, len(buildings) - 1):
        max_left = max(buildings[:i])
        max_right = max(buildings[i:])

        upper_bound = min(max_left, max_right)
        raindrop = max(0, upper_bound - buildings[i])
        trapped_rain.append(raindrop)
        total_height += raindrop

    trapped_rain.append(0)
    visualize_rain(buildings, trapped_rain)
    print("Input: height = ", buildings)
    print("Output: ", total_height)
    print("The above elevation map(black stick) is represented by array ", buildings, ".")
    print("In this case, ", total_height, "units of rain water(sky blue stick) are being trapped")


trapping_rain([3, 0, 0, 2, 0, 4])
trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])

