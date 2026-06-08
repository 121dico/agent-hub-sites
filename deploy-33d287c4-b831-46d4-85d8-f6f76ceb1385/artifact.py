import random
import time


# ========== 方式一：使用标准库（实际项目推荐） ==========
def demo_stdlib():
    print("随机浮点 [0,1):", random.random())
    print("随机整数 [1,100]:", random.randint(1, 100))
    print("区间随机浮点:", random.uniform(1.5, 9.9))
    print("列表随机选一个:", random.choice(["苹果", "香蕉", "橙子"]))
    print("随机打乱列表:", random.sample(range(1, 11), 5))


# ========== 方式二：从零实现（线性同余生成器 LCG） ==========
class SimpleRandom:
    """线性同余随机数生成器（Linear Congruential Generator）。

    公式: next = (a * seed + c) % m
    参数采用 glibc 的常用取值。
    """

    def __init__(self, seed=None):
        # 不给种子就用当前时间，保证每次运行结果不同
        self.state = seed if seed is not None else int(time.time() * 1000)
        self.a = 1103515245
        self.c = 12345
        self.m = 2 ** 31

    def next_int(self):
        """返回 [0, m) 范围内的随机整数。"""
        self.state = (self.a * self.state + self.c) % self.m
        return self.state

    def random(self):
        """返回 [0, 1) 范围内的随机浮点数。"""
        return self.next_int() / self.m

    def randint(self, low, high):
        """返回 [low, high] 范围内的随机整数（含两端）。"""
        return low + self.next_int() % (high - low + 1)


if __name__ == "__main__":
    print("=== 标准库实现 ===")
    demo_stdlib()

    print("\n=== 自定义 LCG 实现 ===")
    rng = SimpleRandom(seed=42)
    print("5 个随机整数 [1,100]:", [rng.randint(1, 100) for _ in range(5)])
    print("5 个随机浮点 [0,1):", [round(rng.random(), 4) for _ in range(5)])