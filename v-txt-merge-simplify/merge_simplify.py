#!/usr/bin/env python3
"""
merge_simplify.py — 合并多个 txt 文件，繁体转简体，修复乱码/错别字

用法:
  python3 merge_simplify.py <输入目录> [输出文件]

示例:
  python3 merge_simplify.py ./my-novel
  python3 merge_simplify.py ./my-novel ./merged.txt

功能:
  1. 按文件名自然排序，合并目录下所有 .txt 文件
  2. 繁体中文 → 简体中文（基于 opencc-python-reimplemented）
  3. 修复韩文乱码字符（常见于某些网文平台的编码错误）
  4. 修复「著→着」等繁简转换遗漏
  5. 修复两岸用语差异（如「简讯→短信」）
  6. 输出合并后的单一 txt 文件

依赖:
  pip install opencc-python-reimplemented
"""

import os
import re
import sys
import glob
import shutil
import subprocess
import tempfile


# ──────────────────────────────────────────────
# 1. 乱码字符修复映射（韩文字符 → 中文）
#    来源：部分网文平台编码错误导致中文字符被替换为韩文
# ──────────────────────────────────────────────

GLITCH_FIX = {
    # 代词/助词
    '놖': '我', '놆': '是', '놛': '他', '놜': '她', '놝': '它',
    '놞': '们', '놈': '你', '놅': '的', '놇': '在', '놉': '也',
    '놊': '不', '놋': '这', '몌': '么', '농': '和', '놎': '了',
    '놏': '有', '놐': '人', '놑': '我', '높': '是', '놓': '不',
    '놔': '也', '놕': '都', '놗': '一',

    # 动词/动作
    '눒': '作', '놚': '要', '놠': '说', '놡': '对', '놢': '地',
    '놲': '让', '놳': '给', '놸': '出', '놹': '生', '놽': '去',
    '놾': '看', '놿': '想', '뇨': '打', '뇩': '新', '뇧': '别',

    # 名词/量词
    '꿛': '手', '떘': '下', '놙': '只', '꺳': '才', '꿁': '少',
    '괗': '二', '꺘': '三', '꽮': '元', '껙': '口', '께': '小',
    '굛': '十', '떚': '子',

    # 副词/连词
    '늀': '就', '꿯': '反', '꾿': '切', '꿫': '又', '꺗': '又',
    '놘': '由', '땢': '同', '그': '人', '극': '入',

    # 情感/心理
    '꿩': '仇',   # 仇恨、复仇

    # 方位/处所
    '늌': '外',   # 校外、格外、窗外
    '뀘': '方',   # 警方、方向、地方
    '뀞': '心',   # 心头、担心

    # 动作相关
    '꿀': '止',   # 阻止
    '놀': '布',   # 散布
    '꺲': '工',   # 工作
    '돗': '它',   # 它们

    # 其他
    '땡': '百',   # 百般
    '꼐': '及',   # 触及
    '늂': '乎',   # 似乎
    '뀙': '火',   # 野火
    '꾨': '尤',   # 尤其是
    '꾮': '互',   # 互联网
    '꽬': '夫',   # 奸夫
    '녡': '世',   # 前世
}


# ──────────────────────────────────────────────
# 2. 两岸用语差异修复
# ──────────────────────────────────────────────

REGIONAL_FIXES = [
    ('简讯', '短信'),       # 台湾「简讯」→ 大陆「短信」
    ('网路', '网络'),       # 台湾「网路」→ 大陆「网络」
    ('资讯', '信息'),       # 台湾「资讯」→ 大陆「信息」（视语境，保留"资讯"用于"资讯类"场景）
    ('软体', '软件'),       # 台湾「软体」→ 大陆「软件」
    ('硬体', '硬件'),       # 台湾「硬体」→ 大陆「硬件」
    ('程式', '程序'),       # 台湾「程式」→ 大陆「程序」
    ('荧幕', '屏幕'),       # 台湾「荧幕」→ 大陆「屏幕」
    ('视窗', '窗口'),       # 台湾「视窗」→ 大陆「窗口」
    ('滑鼠', '鼠标'),       # 台湾「滑鼠」→ 大陆「鼠标」
    ('印表机', '打印机'),   # 台湾「印表机」→ 大陆「打印机」
    ('伺服器', '服务器'),   # 台湾「伺服器」→ 大陆「服务器」
    ('部落格', '博客'),     # 台湾「部落格」→ 大陆「博客」
]


# ──────────────────────────────────────────────
# 3. 核心处理函数
# ──────────────────────────────────────────────

def ensure_opencc():
    """确保 opencc 已安装"""
    try:
        from opencc import OpenCC
        return OpenCC('t2s')
    except ImportError:
        print('[INFO] 正在安装 opencc-python-reimplemented ...')
        subprocess.check_call(
            [sys.executable, '-m', 'pip', 'install',
             'opencc-python-reimplemented', '-q']
        )
        from opencc import OpenCC
        return OpenCC('t2s')


def natural_sort_key(path):
    """自然排序：file2.txt < file10.txt"""
    basename = os.path.basename(path)
    return [
        int(c) if c.isdigit() else c.lower()
        for c in re.split(r'(\d+)', basename)
    ]


def fix_glitch_chars(text):
    """修复韩文乱码字符"""
    return ''.join(GLITCH_FIX.get(ch, ch) for ch in text)


def fix_zhe_zhe(text):
    """修复 opencc 遗漏的「著→着」"""
    return re.sub(r'([\u4e00-\u9fff])著', r'\1着', text)


def fix_regional_terms(text):
    """修复两岸用语差异"""
    for old, new in REGIONAL_FIXES:
        text = text.replace(old, new)
    return text


def process_file(filepath):
    """读取单个文件，返回段落列表"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.strip().split('\n')
    paragraphs = []

    for line in lines:
        # 去掉行首逗号（某些格式以逗号开头）
        cleaned = line.lstrip(',').strip()
        if cleaned:
            paragraphs.append(cleaned)

    return paragraphs


def merge_and_simplify(input_dir, output_file=None):
    """
    主函数：合并目录下所有 txt，转简体，修复错别字

    Args:
        input_dir:   输入目录路径
        output_file: 输出文件路径（默认为 input_dir/合并.txt）
    """
    # 0. 初始化
    cc = ensure_opencc()

    if output_file is None:
        output_file = os.path.join(input_dir, '合并.txt')

    # 1. 收集并排序 txt 文件
    txt_files = sorted(
        glob.glob(os.path.join(input_dir, '*.txt')),
        key=natural_sort_key,
    )

    # 排除输出文件本身（避免重复）
    output_basename = os.path.basename(output_file)
    txt_files = [f for f in txt_files if os.path.basename(f) != output_basename]

    # 排除输入目录中已有的合并文件（避免把上次输出当输入）
    merge_names = {'合并.txt', 'merged.txt', '合并输出.txt'}
    txt_files = [f for f in txt_files if os.path.basename(f) not in merge_names]

    if not txt_files:
        print(f'[ERROR] 目录 {input_dir} 下没有找到 .txt 文件')
        sys.exit(1)

    print(f'[INFO] 找到 {len(txt_files)} 个 txt 文件:')
    for f in txt_files:
        print(f'       - {os.path.basename(f)}')

    # 2. 合并所有段落
    all_paragraphs = []
    for filepath in txt_files:
        paras = process_file(filepath)
        all_paragraphs.extend(paras)

    # 3. 修复乱码 + 繁转简 + 后处理
    result_paras = []
    for p in all_paragraphs:
        p = fix_glitch_chars(p)
        p = cc.convert(p)
        result_paras.append(p)

    result = '\n\n'.join(result_paras)

    # 后处理
    result = fix_zhe_zhe(result)
    result = fix_regional_terms(result)

    # 4. 写入输出文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(result)

    # 5. 统计报告
    kr_remaining = re.findall(r'[\uAC00-\uD7A3]', result)
    print(f'\n[DONE] 合并完成！')
    print(f'       输出文件: {output_file}')
    print(f'       总段落数: {len(result_paras)}')
    print(f'       总字符数: {len(result)}')
    if kr_remaining:
        unique = set(kr_remaining)
        print(f'[WARN] 仍有 {len(kr_remaining)} 个韩文乱码字符未修复:')
        for ch in sorted(unique, key=ord):
            idx = result.find(ch)
            start = max(0, idx - 8)
            end = min(len(result), idx + 8)
            print(f'       {ch} (U+{ord(ch):04X}) → ...{result[start:end]}...')
        print(f'[TIP]  请将上述字符添加到 GLITCH_FIX 映射中')
    else:
        print(f'       韩文乱码字符: 全部修复 ✓')

    return output_file


# ──────────────────────────────────────────────
# CLI 入口
# ──────────────────────────────────────────────

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('用法: python3 merge_simplify.py <输入目录> [输出文件]')
        print('示例: python3 merge_simplify.py ./my-novel')
        print('      python3 merge_simplify.py ./my-novel ./merged.txt')
        sys.exit(0)

    input_dir = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    merge_and_simplify(input_dir, output_file)
