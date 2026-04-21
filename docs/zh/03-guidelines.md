# 03 :: 生成原则和执行约束 (GENERATIVE PRINCIPLES AND EXECUTION GUIDELINES)

任何触犯了生成原则的代码合并请求将被静态拒绝。

## P-01 :: 颜色跟随状态 (COLOR FOLLOWS STATE)
没有 `background-color` 是遵循审美强迫症的。必须优先评估状态机的前提条件：“中立”、“警告”还是“阻塞”。非此即彼，没有修饰。

## P-02 :: 角度即承诺 (ANGLE AS COMMITMENT)
CSS 底层基底法则：`* { border-radius: 0 !important; }`。数字系统在笛卡尔的方格 (`X` 与 `Y`) 的核心里运作。模拟平滑曲线是在系统上堆砌掩耳盗铃的图形假象。90° 传达坚硬。

## P-03 :: 机器用等宽，人类用无衬线 (SEMANTIC_DISTINCTION)
`--font-code` 中的视觉块立刻告知用户该数据需要客观推演并决策。`--font-struct` 则进行被动吸收。

## P-04 :: 屏幕上的唯一琥珀色 (AMBER SINGULARITY)
同一视口绝对排斥冲突。执行点必须让 `--color-amber` 单独主导。竞态条件的颜色堆叠等于扼杀信息层级。

## P-05 :: 空间即沉默 (SPACE IS SILENCE)
模块必须在重力中找到依附处。若利用 `--space-1` 则是在传达内部粘合逻辑。拒绝为了填补空白画布而去设置间距。

## P-06 :: 即时反馈 (IMMEDIATE FEEDBACK)
参数设定：`* { transition: none !important; animation: none !important; }`。有限状态机进行状态切换，CSS 控制的时间动画则是系统犹豫的体现。无菌界面必须零延迟响应。

## P-07 :: ASCII 优先于图标 (ASCII FIRST METRIC)
反一切重体力图像资产依赖。
- 关闭进程: `[x]`
- 折叠状态: `[+]` / `[-]`
加载时间和请求数均归于 `0`。
