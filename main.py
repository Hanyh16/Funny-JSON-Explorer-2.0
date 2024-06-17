from IconFamily import *
from config import icon_family
from JsonExplorer import *
import argparse
import json

if __name__ == '__main__':
    # 创建参数解析器
    parser = argparse.ArgumentParser(description='Funny JSON Explorer (FJE)')
    # 添加命令行参数
    parser.add_argument("-f", "--file", help="JSON文件路径", required=True)
    parser.add_argument("-s", "--style", choices=['tree', 'rectangle'], help="风格", required=True)
    parser.add_argument("-i", "--icon", choices=['poker', 'sun', 'star', 'king', 'snow'], help="图标族", required=True)
    # 解析命令行参数
    args = parser.parse_args()

    # 读取json文件
    with open(args.file, 'r') as f:
        json_data = json.load(f)

    # 获取所选图标系列的图标
    icons = IconFamily(icon_family).get_icons(args.icon)
    
    # 创建 JsonExplorer 实例
    explorer = JsonExplorer(args.style, icons)
    # 加载 JSON 数据
    explorer._load(json_data)
    # 设置输出每行的最大长度
    line_length = 40
    # JSON数据可视化
    explorer.show(line_length)