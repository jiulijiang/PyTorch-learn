# PyTorch-learn
个人PyTorch学习记录
## 2025年7月14日
从今天正式开始学习PyTorch模块，上午入职材料出了问题，直到下午才堪堪找到问题所在，利用傍晚和晚上的闲余时间稍微学一些开头基本知识
  
这次在仓库结构上进行一些简单的优化，如下：  
```python
pytorch-learning-journal/            # 仓库根目录
├── README.md                        # 项目总览 + 快速导航
├── requirements.txt                 # 统一的依赖
├── .gitignore                       # 忽略数据、日志、缓存等

├── docs/                            # 按时间轴的 markdown 笔记
│   ├── 2025-07-14_tensor-basics.md
│   ├── 2025-07-15_autograd-in-depth.md
│   └── ……

├── notebooks/                       # 按次实验的 Jupyter Notebook
│   ├── 2025-07-14_mnist-linear.ipynb
│   ├── 2025-07-16_cifar10-cnn.ipynb
│   └── ……

├── scripts/                         # 可复用的小脚本（数据下载、可视化）
│   ├── download_cifar10.py
│   └── plot_loss.py

├── src/                             # 正式可重用的源码（随学习深度逐渐丰富）
│   ├── data/                        # 数据集加载与预处理
│   │   ├── __init__.py
│   │   └── cifar10_dataset.py
│   ├── models/                      # 网络结构
│   │   ├── __init__.py
│   │   ├── lenet.py
│   │   └── resnet18.py
│   ├── utils/                       # 工具函数
│   │   ├── __init__.py
│   │   ├── metrics.py
│   │   └── seed.py
│   └── configs/                     # yaml / json 超参配置
│       ├── lenet_cifar10.yaml
│       └── resnet_cifar10.yaml

├── experiments/                     # 每次“正式跑实验”一个文件夹
│   ├── exp_2025-07-20_lenet_cifar10/
│   │   ├── main.py                  # 训练入口
│   │   ├── checkpoints/             # 保存的 *.pth
│   │   ├── logs/                    # TensorBoard 或 txt 日志
│   │   └── outputs/                 # 生成的图片、结果 txt 等
│   └── exp_2025-07-25_resnet_cifar10/
│       └── ……

└── slides/                          # 可选：课堂/论文 PPT 或思维导图 PDF
    └── 2025-07-18_attention-mechanism.pdf
```
发现了一些问题，在创建完基本目录结构后，我发现我的基础不够牢固，我需要先学习几个前置的常用包：pandas，numpy，除此以外我还需要在强化一下数学的基础，所以我目前要回归到Python的学习中，在Python学习同时进行数学的学习