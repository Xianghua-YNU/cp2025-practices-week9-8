import numpy as np
import matplotlib.pyplot as plt

def get_fern_params():
    """
    返回巴恩斯利蕨的IFS参数
    每个变换包含6个参数(a,b,c,d,e,f)和概率p
    """
    # TODO: 实现巴恩斯利蕨的参数
    return [
        [0.00, 0.00, 0.00, 0.16, 0.00, 0.00, 0.01],  # T1 (Stem)
        [0.85, 0.04, -0.04, 0.85, 0.00, 1.60, 0.85],  # T2 (Successively smaller leaflets)
        [0.20, -0.26, 0.23, 0.22, 0.00, 1.60, 0.07],  # T3 (Largest left-hand leaflet)
        [-0.15, 0.28, 0.26, 0.24, 0.00, 0.44, 0.07]  # T4 (Largest right-hand leaflet)
    ]


def get_tree_params():
    """
    返回概率树的IFS参数
    每个变换包含6个参数(a,b,c,d,e,f)和概率p
    """
    # TODO: 实现概率树的参数 
    return [
        [0.0, 0.0, 0.0, 0.5, 0.0, 0.0, 0.1],  # T1 (Trunk/Base scaling)
        [0.42, -0.42, 0.42, 0.42, 0.0, 0.2, 0.45],  # T2 (Left Branch)
        [0.42, 0.42, -0.42, 0.42, 0.0, 0.2, 0.45]  # T3 (Right Branch)
    ]


def apply_transform(point, params):
    """
    应用单个变换到点
    :param point: 当前点坐标(x,y)
    :param params: 变换参数[a,b,c,d,e,f,p]
    :return: 变换后的新坐标(x',y')
    """
    # TODO: 实现变换公式
    x, y = point
    a, b, c, d, e, f, _ = params
    x_new = a * x + b * y + e
    y_new = c * x + d * y + f
    return x_new, y_new

def run_ifs(ifs_params, num_points=100000, num_skip=100):
    """
    运行IFS迭代生成点集
    :param ifs_params: IFS参数列表
    :param num_points: 总点数
    :param num_skip: 跳过前n个点
    :return: 生成的点坐标数组
    """
    # TODO: 实现混沌游戏算法
    x, y = (0, 0)
    x_coords = []
    y_coords = []
    probabilities = [param[-1] for param in ifs_params]
    for i in range(num_points):
        transform_index = random.choices(range(len(ifs_params)), probabilities)[0]
        x, y = apply_transform((x, y), ifs_params[transform_index])
        if i > num_skip:
            x_coords.append(x)
            y_coords.append(y)
    return x_coords, y_coords

def plot_ifs(points, title="IFS Fractal"):
    """
    绘制IFS分形
    :param points: 点坐标数组
    :param title: 图像标题
    """
    # TODO: 实现分形绘制
    title="IFS Fractal", filename="ifs_fractal.png"):
    """
    绘制IFS分形
    :param x_coords: 点的x坐标列表
    :param y_coords: 点的y坐标列表
    :param title: 图像标题
    :param filename: 保存图像的文件名
    """
    plt.scatter(x_coords, y_coords, s=1, alpha=0.5)
    plt.title(title)
    plt.axis('equal')
    plt.axis('off')
    plt.savefig(filename)
    plt.show()

if __name__ == "__main__":
    # 生成并绘制巴恩斯利蕨
    fern_params = get_fern_params()
    fern_points = run_ifs(fern_params)
    plot_ifs(fern_points, "Barnsley Fern")
    
    # 生成并绘制概率树
    tree_params = get_tree_params()
    tree_points = run_ifs(tree_params)
    plot_ifs(tree_points, "Probability Tree")
