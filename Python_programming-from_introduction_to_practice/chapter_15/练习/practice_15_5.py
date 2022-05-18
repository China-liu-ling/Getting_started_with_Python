from random import choice

class RandomWalk:
    """一个生成随机漫步数据的类"""

    def __init__(self, num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points

        #所有随机漫步都始于(0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算算计漫步包含的所有点"""

        #不断漫步，直到列表达到指定的长度
        while len(self.x_values) < self.num_points:

            #决定前进方向以及沿着这个方向前进的距离
            x_step = self.get_step()
            y_step = self.get_step()

            #计算下一个点的位置
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
    
    def get_step(self):
        direction = choice([1, -1])
        distance = choice([1, 2, 3, 4])
        step = direction * distance
        return step