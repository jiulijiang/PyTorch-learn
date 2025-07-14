#!/usr/bin/env python3
"""
init_repo.py
一次性生成 pytorch-learning-journal 的目录骨架
"""

from pathlib import Path
import os

# 1. 根目录（脚本所在位置）
ROOT = Path(__file__).resolve().parent
# 如果想在别的路径创建，改成 ROOT = Path("/your/path/pytorch-learning-journal")

# 2. 需要创建的目录列表（相对于 ROOT）
DIRS = [
    "docs",
    "notebooks",
    "scripts",
    "src/data",
    "src/models",
    "src/utils",
    "src/configs",
    "experiments",
    "slides",
]

# 3. 需要创建的占位文件（空文件即可）
FILES = [
    "README.md",
    "requirements.txt",
    ".gitignore",
    "src/__init__.py",
    "src/data/__init__.py",
    "src/models/__init__.py",
    "src/utils/__init__.py",
    "src/configs/.gitkeep",
    "experiments/.gitkeep",
    "slides/.gitkeep",
]

# 4. 创建目录
for d in DIRS:
    (ROOT / d).mkdir(parents=True, exist_ok=True)

# 5. 创建文件（若不存在则 touch）
for f in FILES:
    (ROOT / f).touch(exist_ok=True)

# 6. 给空目录补 .gitkeep（若需要）
for d in DIRS:
    gitkeep = ROOT / d / ".gitkeep"
    if not gitkeep.exists():
        gitkeep.touch()
