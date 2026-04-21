# 逻辑粗野主义 (LOGICAL BRUTALISM) v1.1.1 :: 官方文档

> "如果不解决问题，它就不存在。"

这是一个专为高密度信息环境设计的系统。每一个视觉决策都由功能证明。技术真相是最高形式的美学。

**作者:** Matheus Lacerda Ferreira  
**状态:** 活文档 (LIVING DOCUMENT)  

---

## 00 :: 核心论点与起源

逻辑粗野主义不相信美学空谈。它生于必然。在不稳定环境中，唯一不会失效的指标是逻辑。如果不加修饰的 X 被执行，Y 必然发生。这并非冷漠，这是生存。
如同建筑学的粗野主义拒绝粉饰，逻辑粗野主义暴露软件的逻辑。没有矛盾的视觉层，没有无信息量的装饰。

---

## 01 :: 三大公理 (THE THREE AXIOMS)

基于人类认知处理机制的不可变前提 (参考 Kahneman 的系统 1 与系统 2)。

* **公理 I: 功能先于形式 (FUNCTION PRECEDES FORM)。** DOM 节点的存在仅为传输数据或提示操作。既不传输也不提示的节点是认知噪音。功能可见性 (Affordances) 高于符号暗示。
* **公理 II: 暴露结构 (EXPOSED STRUCTURE)。** 应用程序状态的拓扑和层级树必须在 `t < 100ms` 内具备清晰的可读性。框架不能掩盖内部机制。
* **公理 III: 限制即工具 (CONSTRAINT AS A TOOL)。** 减少输入选择 = 最大化输出一致性。一个由 6 个数学控制的标记 (tokens) 组成的设计矩阵，优于包含 20 种无根据颜色的系统。

---

## 02 :: 五大支柱 (THE FIVE PILLARS)

1. **暴露结构 (Raw Code):** 逻辑不隐藏在不必要的抽象之后。终端、等宽字体和 ASCII 就是语言，因为一切归结于数据。
2. **绝对虚无 (#0A0A0A):** 专注所需的低刺激环境。是对抗世界噪音的构建者的沉默。
3. **触发点 (#FFB000 / 原 #00FF00):** 对颜色的唯一让步。起效的部署，至关重要的操作。外科手术般精准，绝非装饰。
4. **冰冷算计 (Senior Coldness):** 资深工程师的冷酷。不对时髦框架动感情。选择工具，执行，交付。
5. **质感与权威 (Texture and Authority):** 计算过的瑕疵。区分软件工匠与模板机器人的数字颗粒感。

---

## 03 :: 颜色系统与标记 (COLOR SYSTEM AND TOKENS)

调色板是一个注意力层级系统。在指定角色之外使用标记将破坏逻辑。

### 主题 1: 虚无优先 (VOID-FIRST / DARK)
* `--color-void` **(#0A0A0A)**: 极暗主背景 (Absence of noise)。
* `--color-amber` **(#FFB000)**: 唯一操作节点。每屏最多一个。AAA 对比度 (10.81:1)。
* `--color-surface` **(#1E1E1E)**: 卡片边界，上下文分离。
* `--color-text` **(#888888)**: 连续阅读文字。消除高对比度疲劳。
* `--color-white` **(#F0F0F0)**: 关键数据，标题。
* `--color-error` **(#FF4444)**: 错误与警报。激活系统 1 进行即时读取。

### 主题 2: 无限白 (INFINITY-WHITE / LIGHT)
* `--color-infinity` **(#E3E3E3)**: 工业混凝土。主背景，防眩光。
* `--color-accent` **(#B35900)**: 氧化的琥珀色，用于亮度的 AAA 对比度。
* `--color-surface` **(#CCCCCC)**: 结构分离板。
* `--color-text` **(#4D4D4D)**: 石墨书写色。
* `--color-ink` **(#0A0A0A)**: 绝对黑。用于逻辑界面的关键排版。
* `--color-error` **(#BE123C)**: 紧急停止。技术红色，在灰色画布上不产生视觉振动。

---

## 04 :: 排版与间距 (TYPOGRAPHY AND SPACING)

两大系列。严格的功能角色划分。

* `--font-struct` (**Inter**): 人类层。为可读性而生。用于连续阅读内容。
* `--font-code` (**JetBrains Mono**): 逻辑层。代码解析、ID、时间戳、状态。系统的声音。

**间距 (结构上的沉默):**
`--space-1` (0.25rem) 到 `--space-6` (3rem) 规定了逻辑上的邻近关系。同一上下文中的元素保持紧密；不同的上下文需要空间屏障。

---

## 05 :: 生成规则与执行指引 (GENERATIVE PRINCIPLES)

* **P-01 颜色跟随状态 (COLOR FOLLOWS STATE):** 先确认状态 (活跃、错误、中立)，再应用颜色。
* **P-02 角度即承诺 (ANGLE AS COMMITMENT):** `border-radius: 0`。系统不柔化现实。
* **P-03 机器用等宽，人类用无衬线 (MONO FOR MACHINE, SANS FOR HUMAN):** 这是语义区分，非审美区分。
* **P-04 屏幕上的唯一琥珀色 (AMBER ONCE PER SCREEN):** 竞争会破坏层级。
* **P-05 空间即沉默 (SPACE IS SILENCE):** 用间距表达逻辑关系，而非填补空白。
* **P-06 即时反馈 (IMMEDIATE FEEDBACK):** `transition: none`。状态是离散的。平滑过渡意味着机器的犹豫。
* **P-07 ASCII 优先于图标 (ASCII BEFORE ICON):** 文本符号 (`[+]`, `[x]`, `[>]`) 可减少系统开销和外部依赖。

---

## 06 :: 核心组件解剖 (CORE COMPONENT ANATOMY)

### 按钮 (BUTTON)
无过渡动画。`min-height: 44px`。主状态使用 `--color-amber`。通过 `outline` 提供明确的焦点反馈。

### 错误状态 (ERROR STATE)
必须包含 4 个 Norman 层级，并配合红色左边框：
1. **代码 (Code):** 哪里出了故障 (JetBrains Mono + Error Color)
2. **标题 (Title):** 属于什么业务 (JetBrains Mono + White)
3. **描述 (Description):** 发生了什么事 (Inter + Text Color)
4. **操作 (Action):** 如何恢复 (JetBrains Mono + Amber Color)

### 加载器 (LOADER)
唯一允许位移的节点。使用原生 JS 轮换的 ASCII 字符 (`| / - \`)。

MISSION STATUS: **INEVITABLE.**
