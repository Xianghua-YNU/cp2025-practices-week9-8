import numpy as np
import matplotlib.pyplot as plt

def koch_generator(u, level):
    """
    递归生成科赫曲线的点序列。

    参数:
        u: 初始线段的端点数组（复数表示）
        level: 迭代层数

    返回:
        numpy.ndarray: 生成的所有点（复数数组）
    """
    if level == 0:
        return u
    else:
        # 计算每段的长度
        segment_length = np.abs(u[1] - u[0]) / 3
        # 计算每段的方向
        direction = (u[1] - u[0]) / np.abs(u[1] - u[0])
        # 生成新的点
        new_points = np.array([
            u[0],
            u[0] + segment_length * direction,
            u[0] + segment_length * direction * (0.5 + 0.5j * np.sqrt(3)),
            u[0] + 2 * segment_length * direction,
            u[1]
        ])
        # 递归生成下一层
        return np.concatenate([
            koch_generator(new_points[:2], level - 1),
            koch_generator(new_points[1:3], level - 1),
            koch_generator(new_points[2:4], level - 1),
            koch_generator(new_points[3:5], level - 1)
        ])

def minkowski_generator(u, level):
    """
    递归生成闵可夫斯基香肠曲线的点序列。

    参数:
        u: 初始线段的端点数组（复数表示）
        level: 迭代层数

    返回:
        numpy.ndarray: 生成的所有点（复数数组）
    """
    if level == 0:
        return u
    else:
        # 计算每段的长度
        segment_length = np.abs(u[1] - u[0]) / 4
        # 计算每段的方向
        direction = (u[1] - u[0]) / np.abs(u[1] - u[0])
        # 生成新的点
        new_points = np.array([
            u[0],
            u[0] + segment_length * direction * (1 + 1j),
            u[0] + segment_length * direction * (2 + 1j),
            u[0] + segment_length * direction * (3 + 1j),
            u[0] + segment_length * direction * (4 + 1j),
            u[0] + segment_length * direction * (5 + 1j),
            u[0] + segment_length * direction * (6 + 1j),
            u[0] + segment_length * direction * (7 + 1j),
            u[0] + segment_length * direction * (8 + 1j),
            u[1]
        ])
        # 递归生成下一层
        return np.concatenate([
            minkowski_generator(new_points[:2], level - 1),
            minkowski_generator(new_points[1:3], level - 1),
            minkowski_generator(new_points[2:4], level - 1),
            minkowski_generator(new_points[3:5], level - 1),
            minkowski_generator(new_points[4:6], level - 1),
            minkowski_generator(new_points[5:7], level - 1),
            minkowski_generator(new_points[6:8], level - 1),
            minkowski_generator(new_points[7:9], level - 1),
            minkowski_generator(new_points[8:10], level - 1)
        ])

if __name__ == "__main__":
    # 初始线段
    init_u = np.array([0, 1])

    # 绘制不同层级的科赫曲线
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))
    for i in range(4):
        koch_points = koch_generator(init_u, i)
        axs[i//2, i%2].plot(
            np.real(koch_points), np.imag(koch_points), 'k-', lw=1
        )
        axs[i//2, i%2].set_title(f"Koch Curve Level {i+1}")
        axs[i//2, i%2].axis('equal')
        axs[i//2, i%2].axis('off')
    plt.tight_layout()
    plt.savefig("koch_curve.png")
    plt.show()

    # 绘制不同层级的闵可夫斯基香肠曲线
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))
    for i in range(4):
        minkowski_points = minkowski_generator(init_u, i)
        axs[i//2, i%2].plot(
            np.real(minkowski_points), np.imag(minkowski_points), 'k-', lw=1
        )
        axs[i//2, i%2].set_title(f"Minkowski Sausage Level {i+1}")
        axs[i//2, i%2].axis('equal')
        axs[i//2, i%2].axis('off')
    plt.tight_layout()
    plt.savefig("minkowski_sausage.png")
    plt.show()
