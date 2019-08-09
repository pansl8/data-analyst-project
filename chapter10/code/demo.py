"""
    用水处理：
        1. 将水流量数据读入内存中，根据阈值划分用水事件
"""
def get_event(lst, T):
    result = []
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if abs(lst[i] - lst[j]) > T:
                result.append(lst[i:j])
                break

