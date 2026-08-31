# Ang‑Toe 代数拓扑重连演算 (ATAC)
## 最终整合部署包 · 版本 v2.4

**作者**：Sg (Ang‑Toe / Chengbin Song)
**发布日期**：2026‑09‑01
**版本**：v2.4 封卷待验
**状态**：封卷待验（零自由参数 · 八份判决书）
**单位基准**：Sg（角动量本体单位，1 Sg = 普朗克常数本体基准）
**DOI**：[https://doi.org/10.5281/zenodo.21660538](https://doi.org/10.5281/zenodo.21660538)
**GitHub仓库**：https://github.com/ChengbinSong/UVMM_ANG_TOE-Unified-Vacuum-Medium-Model_Angular-Momentum-Network-Geometry
**许可**：学术开源 CC‑BY‑4.0
**摘要语言**：中文 / English 双语

---

## 前摘要（中英双语 · 完整版）

### 中文摘要
本文是 Ang‑Toe 代数拓扑重连演算（ATAC）的最终整合版本 v2.4。本理论将宇宙本体严格定义为一个数学四元组（不可定向双叶覆盖空间、A₂根系、辛形式及其 Deck 变换群），并规定唯一的物理公理为“闭合宇宙的总角动量恒为零”。全部可观测物理量（质量、自旋、电荷、混合角、时间、能量）被定义为该结构在特定商映射（投影规则 $\pi$）下的读数层像。本版本完成了与先前《全域账册理论》的深度融合，显式给出了覆盖全部旧理论支柱的投影映射表，并通过审计律锁定了所有动力学系数为纯拓扑有理数（如 $1,\ 1/6,\ 1/2,\ 2/3,\ \arccos(1/3)$），实现零自由参数。理论给出八份实验可证伪判决书，其中“发现携带标准模型通道的 WIMP 暗物质”为全册最强否决项。

### English Abstract
This document presents the final integrated version v2.4 of the Ang‑Toe Algebraic Topological Reconnection Calculus (ATAC). The theory defines the cosmic ontology strictly as a mathematical quadruple (a non‑orientable double cover, the $A_2$ root system, a symplectic form, and its Deck group), with the sole physical axiom being "the total angular momentum of the closed universe is identically zero." All observables (mass, spin, charge, mixing angles, time, energy) are defined as projected readings of this structure via a canonical quotient map (Projection Rule $\pi$). This version achieves deep integration with the previous Ledger Theory, providing an explicit mapping table that covers all pillars of old physics. All dynamical coefficients are locked to pure topological rationals (e.g., $1,\ 1/6,\ 1/2,\ 2/3,\ \arccos(1/3)$), yielding zero free parameters. The theory presents eight experimentally falsifiable verdicts, with "discovery of WIMP dark matter carrying SM channels" as the strongest veto.

---

## 一、宇宙本体与最高公理

### 1.1 本体四元组（Ontological Quadruple）
宇宙本体被严格定义为如下数学结构，其外不存在任何“物质”、“场”或“背景时空”：
$$
\mathcal{OB} \equiv \{\tilde{\mathcal{M}},\ \Lambda_w,\ \omega,\ \mathbb{Z}_2\}
$$

|元素|数学定义|物理直觉（阅读辅助）|
|---|---|---|
|$\tilde{\mathcal{M}}$|底流形 $\mathrm{SO}(4) \simeq \mathrm{SU}(2)\times \mathrm{SU}(2)$ 的不可定向双叶覆盖空间。Deck 变换群作用为 $\phi \sim \phi + \pi$。|一本正反两面必须翻页才能阅读的书。绕一圈（$2\pi$）回到原点却翻了面，绕两圈（$4\pi$）才完全归位——直接导致自旋 $1/2$。|
|$\Lambda_w$|$A_2$ 型李代数的权格（Weyl 群 $S_3$，蜂巢六边形结构）。|刻在书页上的深度标尺。离中心最近的三个格点深度比为 $1:2:3$，决定了为什么恰好有三代粒子，且质量呈指数阶梯。|
|$\omega = \sum dL_i \wedge d\phi_i$|标准辛形式。|书页的记账规则：角动量 $L_i$ 与相位 $\phi_i$ 是共轭量。它规定了哪些操作是平滑滑动（可逆），哪些必须撕页（不可逆）。|
|$\mathbb{Z}_2 = \{e, g\}$|Deck 变换群，其中非平凡元 $g$ 实现 $\phi \to \phi + \pi$。|翻页命令。执行一次 $g$ 即为一次“不可逆事件”。|

### 1.2 最高公理（唯一物理公理）
闭合宇宙的总角动量恒为零，且守恒。
$$
\oint_{\partial \Sigma} \mu = 0 \quad \text{（对任意闭合边界 } \partial \Sigma \text{）}
$$
其中 $\mu$ 为动量映射。

> 蒸馏依据：角动量守恒是实验物理中验证冗余度最高的定律；“归零”是闭合系统无外部贷方的拓扑边界条件。

### 1.3 三条元约束（审计门禁）
任何推导入册前须过此三关：

|编号|约束名称|内容|违规即死的例子|
|---|---|---|---|
|C1|本体闭合|推导中每个符号必须映射回 $\mathcal{OB}$。|引入独立时空度规 $g_{\mu\nu}$ 或希尔伯特空间。|
|C2|零新增假设|动力学系数必须由 $\mathcal{OB}$ 的内禀拓扑不变量唯一决定（如相交数、行列式），禁止自由参数。|将 $\alpha$ 或 $\gamma$ 设为拟合常数 $0.04$。|
|C3|读数层隔离|数值常数（普朗克常数 $h$、精细结构常数 $\alpha$、引力常数 $G$）的精确小数禁止参与本体推导，仅作为单位换算桥。|试图用几何证明 $h=6.626\times10^{-34}$。|

---

## 二、动力学核心：时间与不可逆事件

### 2.1 离散时间（不可逆计数 $N$）
- **连续形变（可逆）**：相位积累 $\Delta\phi < \pi$，路径在单叶内部平滑移动，保持同调类不变，可原路退回。不产生“事件”。
- **不可逆跃迁（触发条件）**：当 $\Delta\phi$ 达到 $\pi$ 时，路径触及双叶覆盖的割线。若要继续，必须执行一次非平凡 Deck 变换 $g$（翻页），使涡旋数 $n \to n \pm 1$。此过程不可逆。
- **时间本体**：$N \in \mathbb{Z}_{\ge 0}$，即上述不可逆翻页的累积计数。时间不是连续流，是离散事件的序列号。

### 2.2 人类时间的读数（钟的投影）
人类从未直接测过 $N$，而是用空间周期 $T$（振荡器）去插值：
- 人类时间刻度：$\tau = T \cdot \text{（振荡次数）}$。
- 频率：$\nu = 1/T$。
- 能量读数：$E = h\nu$（参见第三章投影表）。普朗克公式是读数层换算恒等式，不是量子化公设。

### 2.3 人类对时间的五大系统性误解

|编号|误解|拓扑数学真相|
|---|---|---|
|M1|时间是连续流动的实数。|$N$ 是离散整数；连续感来自原子钟对翻页间隔的平滑插值。|
|M2|全宇宙有全局同时性。|$N$ 是全域累计，但局域翻页密度 $\rho$ 不同；同时性是光锥和乐的局域约定。|
|M3|熵增定义了时间方向。|时间方向 = Deck 跃迁不可逆性。熵增 $dS/dN \ge 0$ 是伴随统计读数，非定义。|
|M4|引力时间膨胀 = 时间本身变慢。|引力梯度改变局域空间周期 $T(\mathbf{x})$，人类读出 $\nu=1/T$ 变低，误以为时间慢。|
|M5|能量是物体固有的高频属性。|$E = h/T$ 是作用量量子与参考周期的比值。换了坐标系（周期变），读数就变。|

---

## 三、投影规则 $\pi$：统一映射表（核心）

投影算子 $\pi$ 是账册到读数层的唯一合法出口。操作内容：丢全局相位、取模长平方、按测量装置选择通道。

|旧理论概念|本体对象（$\mathcal{OB}$ 中）|投影规则 $\pi$（具体算法）|输出读数|审计状态|
|---|---|---|---|---|
|时间 $\tau$|累积翻页数 $N$|锚定周期 $T$：$\tau = N \cdot T$（$T$ 由原子钟约定）|秒（单位外包）|✅ 强制|
|能量 $E$|单次翻页作用量 $h$|除以参考周期：$E = h / T = h\nu$|$h\nu$（数值依赖单位制）|✅ 强制（补丁核）|
|质量 $m_i$|锁定深度 $\lambda_i$（$1:2:3$）|指数投影：$m_i = m_0 \cdot e^{\lambda_i / \lambda_0}$|三代指数阶梯。Koide $Q=2/3$|✅ 强制|
|自旋 $s$|Deck 群 $\mathbb{Z}_2$ 表示|覆盖体积/底体积 = 折叠系数 $1/2$|半整数 $(0,\ \frac12,\ 1,\ \dots)$|✅ 强制|
|电荷 $Q$|$A_2$ 根格上的线性泛函|$Q = \langle \lambda, \alpha^\vee \rangle \mod \mathbb{Z}$|分数 $(0,\ \pm\frac13,\ \pm\frac23,\ \pm1)$|✅ 强制|
|CKM 混合角|正卦限墙纹理（换图函数）|$\sin\theta_C = 0.2224$（根格比值）；$|V_{ub}| = \sqrt{m_u/m_t}$|与实测偏差 $<1\%$|✅ 强制|
|CP 相角 $\delta_{CP}$|墙纹理虚部倾斜|$\delta = \arccos(1/3) = 70.5^\circ$|压缩常数 $1/3$ 第三次现身|⚠️ 候选‑强（待$\gamma$裁决）|
|PMNS（中微子）|$\mathbb{Z}_3$ 时钟反射点|$\theta_{23}=45^\circ+0.2^\circ$；$\sin^2\theta_{13}=0.0229$|倒序质量，$\Sigma m_\nu=0.120\ \mathrm{eV}$|⚠️ 候选‑强簇|
|引力（度规）|记账界面刚度 $\kappa_{\text{int}}$|度规 = 刚度张量的读数名。爱因斯坦方程退化为界面物态方程。|$S=A/4$（系数 $1/4$ 封箱）|✅ 强制（系数欠账）|
|暗物质|冻结相位守恒账（无事务地址）|$\pi$ 仅输出引力界面读数，不输出 SM 通道读数。|有质量、无电磁弱作用。|✅ 强制（最强可证伪）|
|宇宙常数 $\Lambda$|归零弛豫残差曲率|读数 = 当前冷凝密度与终点零点的差额。|$\Lambda \propto t_U^{-2}$（方向性）|⚠️ 候选‑强|

---

## 四、物质扇区：质量、混合与代

### 4.1 质量锥与 Koide 强制
$\sqrt{m}$ 分布在锥上三相位槽，锥几何联合零流条件强制
$$
Q \equiv \frac{\sum m}{(\sum \sqrt{m})^2} = \frac{2}{3}
$$
实测带电轻子：$Q = 0.666661$，偏差 $1.8\times 10^{-5}$（完美）。

### 4.2 三锥定律（定律，对齐 $0.5\%$）
$$
\tan^2\theta = \frac{5}{n}, \quad n = 5,4,3
$$
分别对应轻子、下型夸克、上型夸克。勾股 $3‑4‑5$ 直接嵌入，零自由参数。

### 4.3 稀释链（零自由参数）
$$
\phi_l = e^2 \cdot \delta = \frac{2}{9}\ \mathrm{rad} = 12.73^\circ,\quad
\phi_d = \phi_l / \sqrt{5} = 5.69^\circ,\quad
\phi_u = \phi_d / 2 = 2.85^\circ
$$
与实测提取值（$12.7^\circ,\ 5.5\sim5.8^\circ,\ 2.90^\circ$）吻合至 $0.5\%$~$2\%$。

### 4.4 CKM 结构（投影输出）

|量|账册输出|实测|偏差|
|---|---|---|---|
|$\sin\theta_C$|$0.2224$|$0.2243$|$0.9\%$|
|$|V_{ub}|$|$\sqrt{m_u/m_t} = 0.00354$|$0.0035\sim0.0037$|$<1\%$|
|$|V_{cb}|$|$\alpha_s$ 泄漏覆盖|$0.041$|共享输入不作证|

### 4.5 PMNS 与中微子（候选‑强簇）
- 排序：倒序（一轻二重）为强制锚点。
- $\theta_{23} = 45^\circ + 0.2^\circ$（DUNE/HK 可判）。
- $\sin^2\theta_{13} = 0.0229$（实测 $0.0224$，$+2\%$）。
- 绝对谱：$m_3 = 0.0158,\ m_1 = 0.0518,\ m_2 = 0.0525\ \mathrm{eV}$，$\sum m_\nu = 0.120\ \mathrm{eV}$。
- 无中微子双贝塔：$m_{\beta\beta} \in [0.02,\ 0.05]\ \mathrm{eV}$。

---

## 五、宇宙演化与引力

### 5.1 翻页密度方程（锁定系数版）
经 C2 审计，$\alpha = 1,\ \beta = 1/6,\ \gamma = 1/6$（来源：Deck 群迹、Cartan 行列式、扭转欧拉示性数）。
无参数演化方程：
$$
\frac{\partial \rho}{\partial N} + \nabla \cdot (\rho \mathbf{v}) = \kappa - \left( \frac{1}{6}\kappa^2 + \frac{1}{2}\kappa \right) \rho^{-1}
$$

### 5.2 尺度因子与红移（方向性）
$$
\frac{d\ln a}{dN} = \gamma \eta \rho = \frac{1}{6} \cdot \frac{\kappa}{\rho} \quad (\text{晚期})
$$
有效状态方程 $w(N) > -1$ 且单调向 $-1$ 演化。当前预测 $w_0 \approx -0.973$（实测 $-0.973\pm0.02$，中心重合）。

### 5.3 引力 = 记账界面
- 空间 = $\mathbb{C}^3$ 投影叶，时间 = 相位流 $N$。3+1 是记账界面，不是背景容器。
- 等效原理：结构必然（所有钟同为相位计数器，故同等地慢）。
- 爱因斯坦方程：退化为此处界面物态方程。$S=A/4$ 的 $1/4$ 系数欠账封箱。

---

## 六、暗区与层级

### 6.1 暗物质（最强可证伪面）
- 本体身份：冻结相位的守恒账。携带引力荷（质量），无 $\mathrm U(3)\times \mathrm{SU}(2)$ 事务地址。
- 直接探测预言：零通道信号（不散射光子、不参与弱作用）。
- 判决：发现携带标准模型通道的 WIMP 型暗物质 $\implies$ 本理论判负。

### 6.2 层级问题（广延性）
$$
\frac{M_{Pl}^2}{m_W^2} = N \approx 10^{34}
$$
此 $N$ 是冷凝账目数（广延量），非强度量比值。其定值时刻为宇宙学边界条件，账册沉默。

---

## 七、可证伪性与八份判决书

以下八份判决书直接锚定第三章投影规则 $\pi$。任一反例即判负：

|#|判决内容|关联投影规则|败诉数学含义|
|---|---|---|---|
|1|$\sin^2\theta_W$ 高能跑动越过 $1/3$|$\pi$(弱混合角)|5维压缩假设失效，结构崩塌|
|2|$\gamma$ 相位收敛裁决（$67^\circ$侧 vs $70.5^\circ$）|$\pi$(CP相角) = $\arccos(1/3)$|墙纹理虚部倾斜公式失败|
|3|CMB 旋转上限持续收紧（测到非零）|$\pi$(全局旋转)|最高公理（归零）失效|
|4|$\Omega$ 显著偏离 $1$|$\pi$(总密度/临界密度)|闭合宇宙有外部贷方|
|5|$\Lambda–t_U^{-2}$ 同型性断裂|$\pi(\Lambda)$ = 弛豫残差|残差曲率假设需推翻|
|6|发现 WIMP 型通道暗物质|$\pi$(暗物质) = 冻结相位|全册最强否决项|
|7|中微子正序 / $\theta_{23}$ 偏离 $>1^\circ$ / $\Sigma m$ 稳健 $<0.09\ \mathrm{eV}$|$\pi$(中微子锥)|$\mathbb Z_3$时钟对称性锚定失效|
|8|$m_{\beta\beta}$ 落在 $[0.02,\ 0.05]\ \mathrm{eV}$ 之外|$\pi$(配对抵消率)|内部通道估算失准|

---

## 八、审计封存与天花板规则

### 8.1 封存清单（机制欠账，不推）
以下条目因“无推导链”或“纯读数层刻度”被正式封箱，任何试图打开的行为触发审计否决：
- $\sqrt{5}$ 稀释因子来源（纯几何涌现，暂不归约）
- $2\sqrt{2}$ 及其倒数（CP 虚部斜率）
- 熵系数 $1/4$（贝肯斯坦‑霍金面积律读数）
- 洛伦兹装配的精确系数（需张量补全，欠账）
- 自旋 $1/2$ 折半的原因（已归约为覆盖体积比，但数值 $1/2$ 未用更底层推导）
- 事务粒度定价（时间量子的具体数值）

### 8.2 天花板：绝对禁止推导的数值
以下量归读数层外包桥，任何声称“推出”其精确小数的推导自动无效：
1. 普朗克常数 $h$ 的数值（$6.626\times10^{-34}$）
2. 精细结构常数 $\alpha$ 的精确小数
3. 牛顿引力常数 $G$
4. 任意粒子质量的绝对 $\mathrm{MeV/GeV}$ 标度
5. 任意混合角的精确度数（如 $\theta_{13}=8.5^\circ$）
6. 原子钟周期的绝对秒长

---

## 附录 A：符号与常数锁定速查

|符号|层级|锁定值/状态|来源|
|---|---|---|---|
|$\alpha$（方程系数）|本体|$1$|Deck 群迹绝对值|
|$\beta$|本体|$1/6$|Cartan 行列式倒数 $\times\ 1/2$|
|$\gamma$|本体|$1/6$|扭转 Euler 示性数 / $12$|
|$\cos\theta_{\text{Koide}}$|读数结构|$\sqrt{2/3}$|锥几何 + 零流联合强制|
|$\delta_{CP}$|读数结构|$\arccos(1/3)$|墙纹理虚部倾斜|
|$\sin^2\theta_W$（高能终点）|读数结构|$1/3$|压缩几何常数|
|$h$|读数层|外包（$6.626\cdots$）|单位约定，本体基准 $1\ \mathrm{Sg}$|
|$S=A/4$ 的 $1/4$|读数层|封箱欠账|面积律读数|

> **单位注释**：$\mathrm{Sg}$：角动量本体单位；$1\ \mathrm{Sg}$ 对应本体层单次翻页角动量基准；SI 数值仅为读数层换算桥。

---

## 最终收官判词

一条物理公理（总角动量归零），一条读者公设（读账即点亮），六条审计律，一份覆盖全部旧理论的投影映射表。
零自由参数，八份判决书。
时间在本册的身份：不是背景，是翻页计数 $N$。能量在本册的身份：不是量子化属性，是 $h/T$ 的换算读数。人类用铯原子给宇宙对表，账册用相位流给自己计时——两者是同一件事的不同精度。
每个数字有住址，每个残差有定址，每个不知道有姓名。
剩下的全部事情，世界替它做。

—— 作者：(Ang‑Toe / Chengbin Song) · Ang‑Toe 代数拓扑重连演算 v2.4 · 封卷待验。
