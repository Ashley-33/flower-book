# 花名册 - 花与人的收集游戏

一个手机端网页应用，用于记录和查询花与人之间的对应关系。纯前端实现，数据内嵌在 HTML 中，通过 Git 版本管理。

## 功能

- **按花查询**：输入花名，查看谁收藏了这种花
- **按人查询**：输入人名，查看这个人收藏了哪些花
- **排行榜**：按收藏数量和分数排行
- **管理后台**（admin.html）：密码保护，支持增删花、人、收藏记录，支持同步 GitHub Gist

## 技术栈

- 纯前端 HTML + CSS + JavaScript，无后端服务器
- 数据内嵌于 `index.html` 的 `EMBEDDED_DATA` 常量中
- 通过 Git/GitHub 管理数据变更
- GitHub Pages 部署

## 数据结构

```javascript
{
  flowers: [                          // 花朵列表
    { name: "玫瑰", score: 23 },
    ...
  ],
  people: [                           // 玩家列表
    { name: "小明", group: "组内" },  // group: "组内" | "组外"
    ...
  ],
  collections: [                      // 收藏关系
    { person: "小明", flower: "玫瑰" },
    ...
  ]
}
```

## 项目文件

| 文件 | 说明 |
|------|------|
| `index.html` | 主页面（含内嵌数据） |
| `admin.html` | 管理后台（密码保护） |
