from Robot import Robot
from Runner import Runner
from Maze import Maze
import random


def run_training(maze_size=(6, 6), trap_number=1, epoch=20, epsilon0=0.3, alpha=0.3, gamma=0.9):

    # # 可选的参数：
    # epoch = 20

    # # 随机探索的初始概率
    # epsilon0 = 0.3

    # # 松弛变量
    # alpha = 0.3

    # # 折扣因子
    # gamma = 0.9

    # # 地图大小
    # maze_size = (6, 6)

    # # 陷阱数量
    # trap_number = 1

    g = Maze(maze_size=maze_size, trap_number=trap_number)
    r = Robot(g, alpha=alpha, epsilon0=epsilon0, gamma=gamma)
    r.set_status(learning=True)

    runner = Runner(r, g)
    runner.run_training(epoch, display_direction=True)
    # runner.generate_movie(filename = "final1.mp4") # 你可以注释该行代码，加快运行速度，不过你就无法观察到视频了。

    # runner.plot_results()
    return runner


params = [
    ((12, 12), 3, 20, 0.3, 0.3, 0.9),
    ((12, 12), 3, 20, 0.3, 0.3, 0.9),
    ((12, 12), 3, 20, 0.3, 0.3, 0.9),
    ((12, 12), 3, 20, 0.3, 0.3, 0.9)
]

results = []
for p in params:
    r = run_training(p[0], p[1], p[2], p[3], p[4], p[5])
    results.append((r, p))

for r in results:
    print(
        "maze_size={}, trap_number={}, epoch={}, epsilon0={}, alpha={}, gamma={}".format(p[0]))
    r[0].plot_results()

# runner1 = run_training(maze_size=(12, 12), trap_number=3,
#                        epoch=20, epsilon0=0.3, alpha=0.3, gamma=0.9)
# runner2 = run_training(maze_size=(12, 12), trap_number=3,
#                        epoch=20, epsilon0=0.3, alpha=0.3, gamma=0.9)
# runner3 = run_training(maze_size=(12, 12), trap_number=3,
#                        epoch=20, epsilon0=0.3, alpha=0.3, gamma=0.9)
# runner4 = run_training(maze_size=(12, 12), trap_number=3,
#                        epoch=20, epsilon0=0.3, alpha=0.3, gamma=0.9)

# runner1.plot_results()
# runner2.plot_results()
# runner3.plot_results()
# runner4.plot_results()
