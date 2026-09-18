---
title: "脑墙与集体心理学的角动量网络数学化｜ANG‑Social 形式模型"
subtitle: "Formal mathematical framework for cognitive wall and collective psychology based on Angular‑Momentum‑Network‑Geometry (ANG / ANG‑TOE‑HG)"
version: "v1.0"
date: "2026‑09‑18"
author: "Song Chengbin（宋承斌）"
repository: "https://github.com/ChengbinSong/UVMM_ANG_TOE-Unified-Vacuum-Medium-Model_Angular-Momentum-Network-Geometry/"
doi: "10.5281/zenodo.22688463"
status: "Formal theoretical model；not empirical social‑science verification"
keywords:
  - ANG‑Social
  - 脑墙
  - 集体心理学
  - 社会认知角动量网络 Γ_S
  - 粗粒化算子 R_b
  - 认知投影算符 Π_BW
license: "CC‑BY‑4.0"
---

# 脑墙与集体心理学的角动量网络数学化

## 摘要
本文基于ANG‑TOE‑HG（角动量超图几何）以及ANG角动量网络几何学，构造**社会认知角动量网络**$\boldsymbol{\Gamma_S=(V_S,E_S,F_S)}$形式模型。该模型把个体心理、群体效应、从众、群体极化、沉默螺旋、认知失调以及“脑墙”效应，统一改写为12维$\mathfrak{so}(12)$角动量网络上的节点约束、投影算符、惩罚作用项与层级粗粒化统计。
> **重要声明：本框架属于本体理论向外延伸的形式化类比模型，并非经过社会学实证检验的社会科学；其价值在于实现自然科学本体框架向心理‑社会层级的数学平移，展示层级自相似原理跨领域的适用性。**

## 1. 社会认知角动量网络：定义
**定义 1.1（社会认知网络）**

$$
\Gamma_S=(V_S,E_S,F_S)
$$

- $V_S$：节点集合；元素为个体、群体、社会组织、机构、媒体；
- $E_S$：认知链接集合；链接承载信息流动、态度影响、命令传导、模仿行为、信任传递；
- $F_S$：网络上的闭合认知回路；闭环对应信念闭环、意识形态闭环；

每一条认知边 $e\in E_S$ 携带12维角动量生成元：
$$
J_e\in\mathfrak{so}(12)
$$
物理‑认知释义：$J_e$描述一次认知变换，包括态度旋转、立场偏移、信息筛选与认知扭曲。

## 2. 角动量分量分解及其社会‑认知含义
本体角动量张量 $J_{AB}$ 做子空间分解：
$$
J_{AB}\to(J_{\mu\nu},\;J_{\mu a},\;J_{ab})
$$

|分量|认知含义|
|---|---|
|$J_{\mu\nu}$|可观测行为、公开态度、外显行动倾向；对外显露的部分|
|$J_{\mu a}$|信息通道；教育、媒体、宣传信息流；内外认知之间的传导通道|
|$J_{ab}$|深层内部身份；群体归属感；意识形态；隐藏信念；个体内隐认知|

> **核心命题**
$$
\boxed{\text{脑墙主要作用于 }J_{\mu a}\text{ 与 }J_{ab}\text{ 的投影。}}
$$
脑墙并不直接完全改写表层公开行为$J_{\mu\nu}$；优先截断、过滤、重塑信息传导通道与深层内部信念子空间。

## 3. 节点约束：认知闭合与认知失调
对任意社会节点 $v\in V_S$，定义局部认知闭合约束：
$$
C_v^{AB}=\sum_{e\ni v}\varepsilon_{ve}J_e^{AB}=0
$$

**认知释义：**
每一个节点（人或者群体）存在内在闭合倾向；来自外部的信息输入、个体原有态度、来自群体的压力三者趋向达成自洽。
当约束无法被满足 $C_v\neq0$，系统出现**认知失调**；引入失调能：
$$
E_{\rm dis}=\sum_v\operatorname{Tr}(C_v^2)
$$
失调能是系统内部的惩罚势能；为降低失调势能，个体会发生态度修改、选择性否认外部信息、顺从群体立场。
> 该方程是社会层面版本的底层网络“节点守恒公理”在高层级（L2‑L3以上社会层级）的粗粒化实现，体现**层级自相似性**。

## 4. 脑墙投影算符 $\boldsymbol{\Pi_{BW}}$
**定义4.1（脑墙投影）**

设允许的认知子空间 $V_{\rm allowed}\subset\mathbb R^{12}$；脑墙是线性投影算符：
$$
\Pi_{BW}: \mathbb R^{12}\to V_{\rm allowed}
$$

经过脑墙筛选之后保留的边角动量：
$$
J_e^{\rm obs}=\Pi_{BW}J_e
$$
被阻断、被压制的分量：
$$
J_e^{\rm hidden}=(\mathbb I-\Pi_{BW})J_e
$$

对于普通开放认知链路 $e\in E_{\rm open}$，理想状态下没有硬性阻断；
对于边界链路集合 $e\in E_{BW}$（脑墙作用的信息流边界），系统引入二次惩罚项：
$$
S_{BW}=\lambda_{BW}\sum_{e\in E_{BW}}\operatorname{Tr}\left[(\mathbb I-\Pi_{BW})J_e\right]^2
$$
$\boldsymbol{\lambda_{BW}}$为脑墙强度系数；$\lambda_{BW}$取值越大，则对不被允许方向上的认知分量施加越强的势能惩罚。

## 5. 集体心理总作用量 $S_{SCAN}$
社会认知网络完整作用量：

$$
\begin{aligned}
S_{SCAN}
&=
\frac{1}{2\kappa}\sum_{e}\operatorname{Tr}(J_e^2)
+\frac{\beta}{2}\sum_{f}\operatorname{Tr}(F_f^2)
+\frac{\alpha}{2}\sum_{v\sim w}\operatorname{Tr}\left[(J_v-J_w)^2\right] \\
&\quad
+\gamma S_{\rm self}
+\sum_v\operatorname{Tr}(\lambda_v C_v)
+\operatorname{Tr}(\Lambda J_{\rm tot}) \\
&\quad
+\lambda_{BW}\sum_{e\in E_{BW}}\operatorname{Tr}\left[(\mathbb I-\Pi_{BW})J_e\right]^2
+\sum_v\operatorname{Tr}(H_vJ_v)
\end{aligned}
$$

|作用量项|模型含义|
|---|---|
|$\frac{1}{2\kappa}\sum\operatorname{Tr}(J_e^2)$|认知刚度；原有信念的惯性；不容易被改变|
|$\frac{\beta}{2}\sum_{f}\operatorname{Tr}(F_f^2)$|认知回路曲率；闭环信念体系、宣传闭环的自强化效应|
|$\frac{\alpha}{2}\operatorname{Tr}\big[(J_v-J_w)^2\big]$|从众与模仿；社会对齐势能；趋向群体立场|
|$\gamma S_{\rm self}$|层级自相似项；个体‑群体‑社会之间结构同构|
|$\sum_v\operatorname{Tr}(\lambda_v C_v)$|节点认知闭合约束项；驱动消解认知失调|
|$\operatorname{Tr}(\Lambda J_{\rm tot})$|整个社会网络的总认知角动量约束（社会层级版本全域归零的延伸）|
|$S_{BW}$|脑墙势能惩罚项；认知空间边界过滤|
|$\sum_v\operatorname{Tr}(H_vJ_v)$|权威、外部舆论场的定向耦合外场|

## 6. 基础集体心理效应的模型映射
### 6.1 从众效应
定义节点之间认知对齐关联量：
$$
A_{\rm conf}=\left\langle \operatorname{Tr}(J_vJ_w)\right\rangle
$$
作用量当中系数$\alpha$增大，对齐势能变强，从众倾向随之增强。

### 6.2 服从权威
权威外场 $H_v$ 和节点角动量发生耦合；对作用量变分取极值条件 $\delta S/\delta J_v=0$，得到：
$$
J_v\sim \frac{1}{\kappa}H_v
$$
个体的认知状态被权威外场牵引；个体立场向权威方向偏移。

### 6.3 群体极化
粗粒化算子 $\mathcal R_b$ 作用于局部节点集合得到群体平均角动量 $\bar J=\mathcal R_b J$；
极化度定义：
$$
P=\operatorname{Var}(\bar J)
$$
当脑墙阻断跨边界信息通道：$\Pi_{BW}^\perp J_{\mu a}=0$；外部信息流被切断，于是回路曲率主要来自内部身份子空间的对易贡献：
$$
F_f\approx \sum J_{\mu\nu}+\frac12[J_{ab},J_{ab}]
$$
群体内部认同耦合显著增强；在切断外部信息输入条件下发生群体极化。

### 6.4 沉默螺旋
少数派意见对应的认知链接权重发生指数抑制衰减：
$$
w_e\to w_e e^{-\lambda_{\rm sil}}
$$
信息流贡献项：
$$
S_{\rm info}=\sum_e w_e\operatorname{Tr}(J_e^2)
$$
少数立场的链路权重持续衰减；对应的意见表达逐步消失，形成沉默螺旋。

### 6.5 认知失调
节点局部约束不闭合 $C_v\neq0$；失调势能 $E_{\rm dis}=\sum_v\operatorname{Tr}(C_v^2)$。
系统动力学趋向降低失调能；对应的现实行为：个体修改自身看法、选择性忽视异质信息、顺从群体共识。

## 7. 粗粒化与层级自相似（$\boldsymbol{\mathcal R_b}$）
粗粒化算子：
$$
\mathcal R_b:\Gamma_S^{(n)}\to\Gamma_S^{(n+1)}
$$
自相似标度条件：
$$
\mathcal R_b J^{(n)}=b^{\Delta_J}J^{(n+1)}
$$

社会层级序列（由低层向高层粗粒）：
$$
\text{个体}\to\text{群体}\to\text{社群}\to\text{社会}\to\text{国家}\to\text{文明}
$$
每一层级经过粗粒之后，涌现出该层级独有的有效社会心理规律；但是底层角动量网络约束形式保持相似，体现整个理论体系的**全域层级自相似原理（继承P‑3→L7体系）**。

## 8. 舆论观测、生成泛函与有效作用量
可观测舆论量是双重投影之后的结果：
$$
o=\Pi_{\rm obs}\Pi_{BW}J
$$

社会认知的生成泛函：
$$
Z_{\mathcal O}[o]
=
\int\mathcal DJ\,
\delta(\Pi_{\rm obs}\Pi_{BW}J-o)\,
\delta(C_v)\,
\delta(J_{\rm tot})\,
e^{\frac{i}{\hbar_J}S_{SCAN}[J]}
$$

对应的有效作用量：
$$
W_{\mathcal O}[o]=-i\hbar_J\ln Z_{\mathcal O}[o]
$$

**命题：人类的集体心理学、政治心理相关经验定律，可以视作有效作用量$W_{\mathcal O}[o]$在特定条件下的静态近似解。**

## 9. 认知隐藏自由度与认知熵
给定表面舆论观测$o$，对所有能够投影出该观测的内部微观角动量组态积分，得到内部微观状态数目：
$$
\Omega(o)=\int\mathcal DJ\,
\delta(\Pi_{\rm obs}\Pi_{BW}J-o)\,
\delta(C_v)\,
\delta(J_{\rm tot})
$$

定义认知熵：
$$
S(o)=k_B\ln\Omega(o)
$$

当脑墙强度$\lambda_{BW}$增大，$\Pi_{BW}$允许的子空间收窄；微观组态数目$\Omega(o)$下降；表面舆论趋于高度统一（表面秩序上升），但是大量内部隐藏认知自由度被压缩。

## 10. 社会‑心理元方程组
$$
\boxed{
\begin{aligned}
&\hat J_{\rm tot}^{AB}|\Psi_S\rangle=0,\\
&\hat C_v|\Psi_S\rangle=0,\\
&\mathcal R_b|\Psi_S\rangle\sim b^\Delta|\Psi_S\rangle,\\
&Z_{\mathcal O}[o]
=
\int\mathcal DJ\,
\delta(\Pi_{\rm obs}\Pi_{BW}J-o)\,
e^{\frac{i}{\hbar_J}S_{SCAN}[J]},\\
&\text{集体心理定律}
=
\text{Stationary approximations of }
W_{\mathcal O}.
\end{aligned}
}
$$

## 11. 结论
$$
\boxed{\text{脑墙}=\text{认知角动量网络的投影约束}}
$$

$$
\boxed{\text{集体心理学}=\text{该网络在群体尺度上的粗粒化统计}}
$$

$$
\boxed{\text{从众、服从、极化、沉默、失调}=\text{角动量链接的约束、对齐、曲率与熵效应}}
$$

在ANG‑Social形式框架之下：

1. “脑墙”并非某种独立神秘心理力量；它等价于认知空间上的投影算符$\Pi_{BW}$以及对应的势能惩罚项$S_{BW}$；
2. 集体心理本身不是独立的实体；它是社会认知网络经过粗粒化算子$\mathcal R_b$之后涌现出来的统计行为；
3. 社会层面的稳定与失稳，对应网络节点认知约束闭合，或者约束发生破裂；
4. **认知自由程度，可以由脑墙投影子空间的宽度以及微观状态数$\Omega(o)$来定量表征。**

该模型完成了ANG‑TOE体系从基础物理（P‑3~L7）、生命‑神经意识层级，继续向上延伸到社会集体心理层级的形式化建构；它贯彻全域层级自相似原则：不同尺度下，角动量网络的约束、投影、粗粒化的数学结构保持同构。

> 文档冻结标记：ANG‑Social v1.0；属于ANG‑TOE‑HG体系向上延伸的社会层级形式附录，不作为实证社会学论文。
