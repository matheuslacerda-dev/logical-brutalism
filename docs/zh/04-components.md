# 04 :: 核心组件的解剖与数学分析 (CORE COMPONENT ANATOMY)

## 1. 原地组件 :: 按钮 (BUTTON)
这是直接执行节点。
* **强制底线尺寸:** 边界框 (`min-height`) 强制锁定在 `44px` 以严格遵循基于触控安全的 WCAG 合规性。
* **禁用 CSS** `transition: none`。
* **边界暴露:** 必须含有 `1px solid var(--color-surface)`。
* **聚焦锁定 (Focus State Exposed):** 忽略 `outline` 的代码直接视为事故。最小执行需达到 `outline: 2px solid var(--color-amber)` 和 `outline-offset: 2px` 以协助辅助工程技术进行 "tab" 流捕捉。

## 2. 输出组件 :: 粗野的错误边界 (ERROR STATE)
原生系统警告弹窗拒绝提供溯源追踪能力。粗野主义的阻断容器强制封装诺曼 (Norman) 提出的四层认知阶段：
1. **故障指令 (Code):** 什么操作失败了？(系统字体 + 红色警告)
2. **路由节点 (Title):** 在哪个切片？(系统字体 + 白光)
3. **语言学定性 (Description):** 为何崩溃？(人类可阅读字体 Inter + 缓和色文本)
4. **决策行动 (Action):** 点击它恢复。

## 3. 进行时组件 :: ASCII 加载器 (PROCESSING LOADER)
这是整个粗野库中唯一允许存在假时序位移逻辑的异常体。
* **纯文本流控制:** 彻底抛弃数十帧循环的 GIF 加载图形，仅由 JS 控制 `['|', '/', '-', '\\' ]` 的无延迟更新。表示出宿主环境存在对 CPU 的底层持有锁锁定特征。
