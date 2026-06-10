#!/usr/bin/env python3
"""
重新生成 index.html 中的 FLOWER_PY 拼音索引。

按花查人的屏幕键盘搜索依赖每朵花预生成的「全拼 + 首字母」。
当通过 admin 新增/修改花名后，运行本脚本即可同步更新拼音索引：

    pip install pypinyin
    python3 tools/gen-pinyin.py

脚本会就地读取并改写 index.html 中的 EMBEDDED_DATA / FLOWER_PY。
"""
import re
import json
import os

from pypinyin import pinyin, Style

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML = os.path.join(ROOT, "index.html")


def build_map(flowers):
    py_map = {}
    for f in flowers:
        name = f["name"]
        syl = pinyin(name, style=Style.NORMAL, errors=lambda x: [c for c in x])
        full = re.sub(r"[^a-z]", "", "".join(s[0] for s in syl).lower())
        abbr = re.sub(r"[^a-z]", "", "".join(s[0][0] for s in syl if s[0]).lower())
        py_map[name] = [full, abbr]
    return py_map


def main():
    html = open(HTML, encoding="utf-8").read()

    data = json.loads(re.search(r"const EMBEDDED_DATA = (\{.*?\});", html, re.S).group(1))
    py_map = build_map(data["flowers"])
    new_const = "const FLOWER_PY = " + json.dumps(py_map, ensure_ascii=False, separators=(",", ":")) + ";"

    html, n = re.subn(r"const FLOWER_PY = \{.*?\};", new_const, html, count=1, flags=re.S)
    if n != 1:
        raise SystemExit("未找到 FLOWER_PY，请确认 index.html 是否已包含拼音索引。")

    open(HTML, "w", encoding="utf-8").write(html)
    print(f"已更新 FLOWER_PY，共 {len(py_map)} 朵花。")


if __name__ == "__main__":
    main()
