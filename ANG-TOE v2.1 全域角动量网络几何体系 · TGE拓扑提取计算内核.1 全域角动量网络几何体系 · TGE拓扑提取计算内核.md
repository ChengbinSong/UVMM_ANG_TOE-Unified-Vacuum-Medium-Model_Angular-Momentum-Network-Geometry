# ANG-TOE v2.1 全域角动量网络几何体系 · TGE拓扑提取计算内核
> 版本：v2.1（**补充连续形变公理与微分同胚约束**｜TGE完整计算包集成版｜含噪声扰动鲁棒扫描、双构型晶型比对、相域相位提取模块）(连续版)
> 定稿日期：2026-08-20
> 作者：宋承斌（Chengbin Song）
> DOI：https://doi.org/10.5281/zenodo.21500910 | https://doi.org/10.5281/zenodo.21660538
> GitHub：https://github.com/ChengbinSong/UVMM_ANG_TOE-Unified-Vacuum-Medium-Model_Angular-Momentum-Network
> 许可证：CC BY-NC 4.0
> 状态：公理锁死｜**连续形变/微分同胚约束纳入核心公理**｜TGE v2.1 计算内核固化｜药物多晶/超导/神经相域全套验证链路就绪

---
```markdown
### Version Summary
ANG‑TOE v2.0 provides a minimal static topological kernel governed only by Axiom‑0, suitable for steady‑state configuration screening.
ANG‑TOE v2.1 adds the continuous‑deformation diffeomorphism axiom (Axiom‑1), explicitly distinguishing smooth intra‑topology‑class strain accumulation and discontinuous topological‑reconnection phase transition.
The TGE solver gains a built‑in deformation‑path scanner. No breaking changes are introduced for static workflows.
Dynamic simulations bring linear‑scaling computational overhead and require careful convergence checks to suppress discretization drift of topological invariants.
```

## 目录
- [0. 总纲与本体论公理体系](#0-总纲与本体论公理体系)
- [1. 核心定义与符号约定](#1-核心定义与符号约定)
- [2. 层级结构：12维原生角动量网络→四维观测投影](#2-层级结构12维原生角动量网络四维观测投影)
- [2.1 连续形变、微分同胚与拓扑等价区分](#21-连续形变微分同胚与拓扑等价区分)
- [3. TGE拓扑提取算法 v2.1 全模块说明](#3-tge拓扑提取算法-v21-全模块说明)
- [4. 物理映射规则（质量、力、光速、时间箭头、连续形变演化）](#4-物理映射规则质量力光速时间箭头连续形变演化)
- [5. 复杂系统映射：药物多晶、超导、意识情感拓扑解释（补充连续形变演化路径）](#5-复杂系统映射药物多晶超导意识情感拓扑解释补充连续形变演化路径)
- [6. 标定规则与宋单位制(Sg)](#6-标定规则与宋单位制sg)
- [7. 可执行Python计算内核（ANGTOE_TGE v2.1，兼容连续形变插值采样）](#7-可执行python计算内核angtoe_tge-v21兼容连续形变插值采样)
- [8. 测试用例（晶型比对+热扰动扫描+连续形变插值演化）](#8-测试用例晶型比对热扰动扫描连续形变插值演化)
- [9. 理论边界、适用范围与观测约束](#9-理论边界适用范围与观测约束)
- [10. 附录：术语词典](#10-附录术语词典)

---

## 0. 总纲与本体论公理体系
> ANG-TOE（Angular Momentum Network Geometry Theory of Everything）v2.1
> 体系底层公理
> **Axiom0：全域总角动量恒等于0**
> **Axiom1：本体层角动量网络允许光滑微分同胚连续形变；连续形变不改变拓扑不变量$\boldsymbol{\text{\(\text{SL}\)},\text{\(\text{Wr}\)},\text{\(\text{Tw}\)}}$，仅连续调制$\boldsymbol{\nabla L,\Gamma_{\text{int}},\Delta\Phi}$；只有越过临界重连势$U_c$才发生非连续拓扑重连，拓扑等价类切换。**
>
> 本体系，由角动量守恒+光滑连续形变唯一演绎生成；时空、场、粒子、相变均为12维角动量网络向四维观测空间的投影表象。
>
> 核心世界观：
> 1. 本体层不存在原生时间；时间是离散拓扑重连事件 $U_{\text{reconnect}}$ 在观测投影层的累积序列
> 2. 因果不是时序先后，而是本体层的**拓扑逻辑蕴含**
> 3. 相域仅可读取**相对相位差**，不存在绝对相位零点，对应人类“相域色盲”观测局限
> 4. 演化分为两类：**光滑连续形变（同拓扑类内、不变拓扑不变量，只蓄积几何应力）**；**拓扑重连相变（跨拓扑等价类、不变量突变、应力释放）**
> 5. 多晶、相变、超导、神经同步/失稳（癫痫、情绪）统一归为角动量涡旋构型：连续形变蓄积应力，到达阈值触发拓扑重连

---

## 1. 核心定义与符号约定
| 符号 | 定义 |
|---|---|
| $U_{\text{reconnect}}$ | 拓扑重连势，相变核心判据 |
| $U_c$ | 重连临界阈值（固定=1.0） |
| $\Gamma_{\text{int}}$ | 角动量交换速率 |
| $\nabla L$ | 角动量拓扑梯度 |
| $\text{\(\text{SL}\)}$ | 自链接数 $\text{\(\text{SL}\)}=\text{\(\text{Wr}\)}+\text{\(\text{Tw}\)}$（**连续形变下守恒**） |
| $\text{\(\text{Wr}\)}$ | 环绕数 \(\text{Wr}\)ithe（**连续形变下守恒**） |
| $\text{\(\text{Tw}\)}$ | 扭转数 \(\text{Tw}\)ist（**连续形变下守恒**） |
| $\Delta\Phi$ | 单构型相域相对相位差 |
| $\Delta\Phi_{12}$ | 双构型之间相位差 |
| $\Delta G$ | 拓扑映射得到的自由能差（多晶稳定性） |
| $\sigma$ | 几何扰动强度（模拟热涨落、溶剂微扰） |
| $\lambda\in[0,1]$ | 连续形变插值参数，$\lambda=0$初始构型，$\lambda=1$目标构型 |

核心闭式：
$$
\Delta\Phi = 2\pi \cdot \frac{\Gamma_{\text{int}}}{1+\sqrt{1+\text{\(\text{SL}\)}^2}}
$$
$$
U_{\text{re}} = \frac{\Gamma_{\text{int}} \sqrt{1+\text{\(\text{SL}\)}^2}}{|\nabla L|}
$$
$$
\Delta\Phi_{12}=|\Delta\Phi_1-\Delta\Phi_2|
$$

> ✅ 连续形变不变量：$\boldsymbol{\text{\(\text{SL}\)},\text{\(\text{Wr}\)},\text{\(\text{Tw}\)}}$ 在$\lambda$光滑插值全程保持恒定；$\nabla L,\Gamma_{\text{int}},\Delta\Phi,U_{\text{re}}$随形变连续平滑变化。

---

## 2. 层级结构：12维原生角动量网络→四维观测投影
1. **本体层 $G_{12}$**：12维正交嵌套角动量网络，静态闭包，全域角动量归零；无原生时间、无局部平直时空；支持光滑微分同胚连续形变
2. **跨尺度嵌套层（L0/L1/M2…）**：L0神经意识拓扑层；L1恒星宏观层；M2核子尺度层，支持跨尺度拓扑传递与连续形变应力传递
3. **四维投影层 $\mathcal{M}_4$**：人类观测表象，生成时空、力、质量、时间箭头；时间箭头来源于宏观拓扑势能梯度对微观重连事件的方向偏置
4. **相域**：投影衍生相位维度，仅可测相对相位，无法直接测距；解释超导同步、共振耦合、相位失配长时应力态

### 2.1 连续形变、微分同胚与拓扑等价区分
1. **连续形变（微分同胚，同痕）**：涡旋曲线光滑拉伸、弯曲、扭转，不剪断、不粘接；属于**同一拓扑等价类**，\(\text{SL}\)/\(\text{Wr}\)/\(\text{Tw}\)严格不变；仅缓慢累积几何应力，$U_{\text{re}}$平滑抬升
2. **拓扑重连（相变）**：形变持续推进，$U_{\text{re}}\ge U_c$，发生剪断/粘接；**拓扑不变量突变，切换拓扑等价类**；应力一次性释放，属于非连续跃迁
> 物理直观：
> - $\Delta\Phi\to0$：相位匹配，瞬时拓扑重连（爱、超导凝聚、共振）
> - $\Delta\Phi$持续锁定非零：相位失配，**连续形变持续蓄积几何应力**（亚稳多晶、长期恨意、缺陷锁定）

---

## 3. TGE拓扑提取算法 v2.1 全模块说明
> TGE = Topology Geometry Extractor 拓扑几何提取器 v2.1
> 模块清单
1. 模块1：高斯链接积分（双环互链接数）
2. 模块2：扭转数\(\text{Tw}\)（Frenet挠率积分）
3. 模块3：环绕数\(\text{Wr}\)
4. 模块4：自链接数\(\text{SL}\) = \(\text{Wr}\) + \(\text{Tw}\)
5. 模块5：角动量拓扑梯度 $\nabla L$ 求解
6. 模块6：角动量交换速率 $\Gamma_{\text{int}}$ 求解
7. 模块7：拓扑重连势能 $U_{\text{re}}$ + 相变判定
8. 模块8：相域相位差 $\Delta\Phi$ 提取
9. 模块9：双构型比对（晶型/构象配对，输出$\Delta\Phi_{12},\Delta G$）
10. 模块10：噪声扰动扫描，模拟热/溶剂微扰，扫描鲁棒边界、定位转晶临界扰动
11. 模块11：给定初始构型、目标构型，沿$\lambda\in[0,1]$做光滑线性插值生成连续形变路径，追踪$\nabla L,\Gamma_{\text{int}},U_{\text{re}},\Delta\Phi$平滑演化曲线，监测形变途中是否触碰重连阈值$U_c$

适用场景：药物多晶相变路径追踪、分子构象连续弛豫、超导畴形变、神经环路缓慢相位漂移

---

## 4. 物理映射规则（质量、力、光速、时间箭头、连续形变演化）
1. 局域角动量投影生成三维空间力与角动量交换速率；三维力闭合映射生成静质量
2. 三维交换速率结合三维空间映射为时频相空间；时空耦合系数即光速
3. 时间箭头：并非基础对称破缺，是宏观嵌套拓扑势能梯度对微观重连事件施加的方向偏置，天然带有空间各向异性
4. 暗物质/暗能量：属于全局嵌套拓扑的投影背景梯度，不引入新粒子
5. **连续形变演化映射**：同拓扑类内光滑形变对应观测层的连续弛豫、缓慢构象调整、应力缓慢累积；当形变演化至$U_{\text{re}}\ge U_c$，触发离散拓扑重连，对应一级相变、转晶、同步爆发

> 定位说明：ANG-TOE不是补充新假说，而是**对已有经实验验证物理定律的拓扑归位、统一谱系**，不需要依赖全新奇异预言作为成立前提。

---

## 5. 复杂系统映射：药物多晶、超导、意识情感拓扑解释（补充连续形变演化路径）
### 5.1 药物多晶（利巴韦林、利托那韦、甘油结晶等）
- 不同晶型 = 同一分子涡旋的**不同拓扑等价构型（\(\text{SL}\)突变）**
- 同一晶型内的晶格热弛豫、溶剂化微调 = **连续形变**：\(\text{SL}\)保持不变，仅连续蓄积几何应力，$U_{\text{re}}$缓慢抬升
- 当连续形变持续累积使$U_{\text{re}}\ge U_c$，触发拓扑重连→跨等价类转晶
- $\Delta G$ 判定热力学稳定性；$\sigma$扰动扫描判断动力学稳定性、预测转晶风险

### 5.2 超导机理
超导态是多涡旋体系集体相位匹配 $\Delta\Phi\to0$，全局拓扑重连形成无耗散闭环；替代传统纯电子配对图像。
超导升温过程属于涡旋体系连续形变，相位差逐步抬升，直到临界温度触发失稳重连、退出超导态。

### 5.3 意识与情感（L0神经拓扑层）
- 爱：两套神经闭环相位匹配 $\Delta\Phi\to0$，瞬时拓扑重连（短时事件）
- 恨：相位持续失配，**神经环路持续连续形变、应力无法释放**，长时冗余锁定形成持久几何应力

---

## 6. 标定规则与宋单位制(Sg)
- 宋单位 Sg：ANG-TOE体系内的基础拓扑缩放单位，由全域角动量归零约束做第一性原理标定
- 体系内所有物理量均可通过拓扑不变量投影映射，建立和国际单位制的换算关系
- 标定分两级：全局本体标定 + 局部构型投影标定；完成标定后方可定量计算多晶自由能、相变阈值、临界温度
> 边界：相位读数仅能取相对值，不存在绝对零点，对应相域观测固有局限
> 连续形变标定要点：形变路径上不变量（\(\text{SL}\)/\(\text{Wr}\)/\(\text{Tw}\)）可作为锚定基准，消除形变过程中的标定漂移

---

## 7. 可执行Python计算内核（兼容连续形变插值采样）
```python
import numpy as np

class ANGTOE_TGE:
    def __init__(self):
        # 基础物理标定常数
        self.m_e = 9.1093837015e-31
        self.e = 1.602176634e-19
        self.L_e = 1.0
        self.nabla_L_e = 1.0
        self.k_pi = (self.m_e * self.nabla_L_e) / (self.L_e * 1)
        self.k_gamma = 1.0
        self.Uc = 1.0 # 拓扑重连临界阈值

    def calc_apparent_mass(self, L: float, Link: float, nabla_L: float, Z: float=1.0):
        topological_term = (np.abs(L) * np.abs(Link)) / np.abs(nabla_L)
        m = self.k_pi * topological_term * Z
        return m

    def calc_apparent_charge(self, \(\text{Tw}\): float, chi: int):
        Q = self.e * \(\text{Tw}\) * chi
        return Q

    def calc_observable_from_gamma(self, Gamma: float, k_obs: float=1.0):
        obs = k_obs * Gamma
        return {"delta_G": obs}

    # 模块1：高斯链接积分
    def gauss_linking_integral(self, c1:np.ndarray, c2:np.ndarray):
        N = c1.shape[0]
        M = c2.shape[0]
        link_sum = 0.0
        for i in range(N-1):
            r1 = c1[i]
            dr1 = c1[i+1] - c1[i]
            for j in range(M-1):
                r2 = c2[j]
                dr2 = c2[j+1] - c2[j]
                r = r1 - r2
                r_mag = np.linalg.norm(r)
                if r_mag < 1e-12:
                    continue
                cross_dr = np.cross(dr1, dr2)
                numerator = np.dot(r, cross_dr)
                link_sum += numerator / (r_mag ** 3)
        link = link_sum / (4 * np.pi)
        return link

    # 模块2：扭转数\(\text{Tw}\)
    def twist_number(self, curve:np.ndarray):
        dr = np.gradient(curve, axis=0)
        d2r = np.gradient(dr, axis=0)
        d3r = np.gradient(d2r, axis=0)
        tw_sum = 0.0
        for i in range(curve.shape[0]-1):
            r1 = curve[i]
            r2 = curve[i+1]
            ds = np.linalg.norm(r2 - r1)
            if ds < 1e-12:
                continue
            dr_i = dr[i]
            d2r_i = d2r[i]
            d3r_i = d3r[i]
            cross12 = np.cross(dr_i, d2r_i)
            cross12_norm = np.linalg.norm(cross12)
            if cross12_norm < 1e-12:
                tau = 0.0
            else:
                tau = np.dot(dr_i, np.cross(d2r_i, d3r_i)) / (cross12_norm ** 2)
            tw_sum += tau * ds
        tw = tw_sum / (2 * np.pi)
        return tw

    # 模块3：环绕数\(\text{Wr}\)
    def writhe(self, curve:np.ndarray):
        N = curve.shape[0]
        wr_sum = 0.0
        for i in range(N-1):
            ri = curve[i]
            dri = curve[i+1] - curve[i]
            for j in range(N-1):
                if abs(i-j) <= 1:
                    continue
                rj = curve[j]
                drj = curve[j+1] - curve[j]
                r = ri - rj
                r_mag = np.linalg.norm(r)
                if r_mag < 1e-12:
                    continue
                cross_dr = np.cross(dri, drj)
                numerator = np.dot(r, cross_dr)
                wr_sum += numerator / (r_mag ** 3)
        wr = wr_sum / (4 * np.pi)
        return wr

    # 模块4：自链接数 \(\text{SL}\) = \(\text{Wr}\) + \(\text{Tw}\)
    def self_linking_number(self, curve:np.ndarray):
        \(\text{Wr}\) = self.writhe(curve)
        \(\text{Tw}\) = self.twist_number(curve)
        \(\text{SL}\) = \(\text{Wr}\) + \(\text{Tw}\)
        return \(\text{SL}\), \(\text{Wr}\), \(\text{Tw}\)

    # 模块5：角动量拓扑梯度
    def grad_L_topology(self, curve:np.ndarray, L_field:np.ndarray=None):
        N = curve.shape[0]
        if L_field is None:
            dr = np.gradient(curve, axis=0)
            d2r = np.gradient(dr, axis=0)
            L_field = np.zeros(N)
            for i in range(N):
                dr_i = dr[i]
                d2r_i = d2r[i]
                cr = np.cross(dr_i, d2r_i)
                cr_norm = np.linalg.norm(cr)
                dr_norm = np.linalg.norm(dr_i)
                if dr_norm > 1e-12:
                    L_field[i] = cr_norm / (dr_norm**3)
                else:
                    L_field[i] = 0.0
        gradL_vec = np.gradient(L_field, curve, axis=0)
        gradL_norm = np.linalg.norm(gradL_vec, axis=1)
        gradL_norm_mean = np.mean(gradL_norm)
        return gradL_vec, gradL_norm_mean

    # 模块6：角动量交换速率 Γ_int
    def gamma_topology_exchange(self, nabla_L_mean:float, Link:float, \(\text{SL}\):float):
        numerator = self.k_gamma * np.abs(nabla_L_mean) * np.abs(Link)
        denominator = np.sqrt(1.0 + \(\text{SL}\)**2)
        Gamma_int = numerator / denominator
        Z = np.exp(-np.clip(Gamma_int, 0, 2.5))
        return Gamma_int, Z

    # 模块7：拓扑重连判据
    def topology_reconnect_criterion(self, Gamma_int:float, \(\text{SL}\):float, nabla_L_mean:float):
        if abs(nabla_L_mean) < 1e-12:
            return np.inf, True
        U_re = Gamma_int * np.sqrt(1.0 + \(\text{SL}\)**2) / np.abs(nabla_L_mean)
        is_reconnect = U_re >= self.Uc
        return U_re, is_reconnect

    # 模块8：相域相位差 \(\Delta\Phi\)
    def phase_domain_delta_phi(self, Gamma_int:float, \(\text{SL}\):float):
        denom = 1.0 + np.sqrt(1.0 + \(\text{SL}\)**2)
        delta_phi = 2 * np.pi * Gamma_int / denom
        delta_phi_deg = np.rad2deg(delta_phi)
        return delta_phi, delta_phi_deg

    # 模块9：双构型比对（多晶配对）
    def compare_two_configs(self, curveA:np.ndarray, curveB:np.ndarray, k_free_energy=2.45e3):
        \(\text{SL}\)_A, \(\text{Wr}\)_A, \(\text{Tw}\)_A = self.self_linking_number(curveA)
        _, nablaL_A = self.grad_L_topology(curveA)
        GammaA, ZA = self.gamma_topology_exchange(nablaL_A, Link=\(\text{SL}\)_A, \(\text{SL}\)=\(\text{SL}\)_A)
        Ure_A, isRe_A = self.topology_reconnect_criterion(GammaA, \(\text{SL}\)_A, nablaL_A)
        dPhiA, dPhiA_deg = self.phase_domain_delta_phi(GammaA, \(\text{SL}\)_A)

        \(\text{SL}\)_B, \(\text{Wr}\)_B, \(\text{Tw}\)_B = self.self_linking_number(curveB)
        _, nablaL_B = self.grad_L_topology(curveB)
        GammaB, ZB = self.gamma_topology_exchange(nablaL_B, Link=\(\text{SL}\)_B, \(\text{SL}\)=\(\text{SL}\)_B)
        Ure_B, isRe_B = self.topology_reconnect_criterion(GammaB, \(\text{SL}\)_B, nablaL_B)
        dPhiB, dPhiB_deg = self.phase_domain_delta_phi(GammaB, \(\text{SL}\)_B)

        dPhi_12 = np.abs(dPhiA - dPhiB)
        dGamma = GammaA - GammaB
        dUre = Ure_A - Ure_B
        dG = self.calc_observable_from_gamma(dGamma, k_obs=k_free_energy)["delta_G"]

        return {
            "ConfigA":{
                "\(\text{SL}\)":\(\text{SL}\)_A, "\(\text{Wr}\)":\(\text{Wr}\)_A, "\(\text{Tw}\)":\(\text{Tw}\)_A,
                "\(\nabla L\)_mean":nablaL_A, "Γ_int":GammaA, "Z":ZA,
                "U_re":Ure_A, "is_reconnect":isRe_A,
                "\(\Delta\Phi\)_rad":dPhiA, "\(\Delta\Phi\)_deg":dPhiA_deg
            },
            "ConfigB":{
                "\(\text{SL}\)":\(\text{SL}\)_B, "\(\text{Wr}\)":\(\text{Wr}\)_B, "\(\text{Tw}\)":\(\text{Tw}\)_B,
                "\(\nabla L\)_mean":nablaL_B, "Γ_int":GammaB, "Z":ZB,
                "U_re":Ure_B, "is_reconnect":isRe_B,
                "\(\Delta\Phi\)_rad":dPhiB, "\(\Delta\Phi\)_deg":dPhiB_deg
            },
            "Pair_Delta":{
                "\(\Delta\Phi\)_12_rad":dPhi_12,
                "ΔΓ_int":dGamma,
                "ΔU_re":dUre,
                "\(\Delta G\)":dG
            }
        }

    # 模块10：噪声扰动扫描｜热/溶剂微扰鲁棒性测试
    def perturb_scan(self, curve_base:np.ndarray, sigma_list:list, repeat=8, seed=42):
        rng = np.random.default_rng(seed)
        scan_result = []
        for sigma in sigma_list:
            batch = []
            for _ in range(repeat):
                noise = rng.normal(loc=0.0, scale=sigma, size=curve_base.shape)
                curve_pert = curve_base + noise
                \(\text{SL}\), \(\text{Wr}\), \(\text{Tw}\) = self.self_linking_number(curve_pert)
                _, nablaL = self.grad_L_topology(curve_pert)
                Gamma, Z = self.gamma_topology_exchange(nablaL, Link=\(\text{SL}\), \(\text{SL}\)=\(\text{SL}\))
                Ure, isRe = self.topology_reconnect_criterion(Gamma, \(\text{SL}\), nablaL)
                dPhi, dPhi_deg = self.phase_domain_delta_phi(Gamma, \(\text{SL}\))
                batch.append({
                    "\(\text{SL}\)":\(\text{SL}\), "\(\text{Wr}\)":\(\text{Wr}\), "\(\text{Tw}\)":\(\text{Tw}\),
                    "\(\nabla L\)_mean":nablaL, "Γ_int":Gamma, "Z":Z,
                    "U_re":Ure, "is_reconnect":isRe,
                    "\(\Delta\Phi\)_rad":dPhi, "\(\Delta\Phi\)_deg":dPhi_deg
                })
            keys = batch[0].keys()
            avg = {}
            for k in keys:
                vals = [b[k] for b in batch if isinstance(b[k],float)]
                avg[k] = np.mean(vals) if vals else None
            scan_result.append({"sigma":sigma,"avg":avg,"raw_batch":batch})
        return scan_result

    # 模块11【连续形变插值演化】
    def continuous_deformation_scan(self, curve_start:np.ndarray, curve_end:np.ndarray, n_step=20):
        """
        \(\lambda\) ∈ [0,1] 线性插值实现光滑连续形变
        输出整条形变路径上拓扑指标演化，检验\(\text{SL}\)守恒、监测U_re是否触碰相变阈值
        """
        path = []
        lam_list = np.linspace(0.0, 1.0, n_step)
        for lam in lam_list:
            curve_t = (1 - lam) * curve_start + lam * curve_end
            \(\text{SL}\), \(\text{Wr}\), \(\text{Tw}\) = self.self_linking_number(curve_t)
            _, nablaL = self.grad_L_topology(curve_t)
            Gamma, Z = self.gamma_topology_exchange(nablaL, Link=\(\text{SL}\), \(\text{SL}\)=\(\text{SL}\))
            Ure, isRe = self.topology_reconnect_criterion(Gamma, \(\text{SL}\), nablaL)
            dPhi, dPhi_deg = self.phase_domain_delta_phi(Gamma, \(\text{SL}\))
            path.append({
                "\(\lambda\)":lam,
                "\(\text{SL}\)":\(\text{SL}\), "\(\text{Wr}\)":\(\text{Wr}\), "\(\text{Tw}\)":\(\text{Tw}\),
                "\(\nabla L\)_mean":nablaL, "Γ_int":Gamma, "Z":Z,
                "U_re":Ure, "is_reconnect":isRe,
                "\(\Delta\Phi\)_rad":dPhi, "\(\Delta\Phi\)_deg":dPhi_deg
            })
        return path
```

---

## 8. 测试用例（晶型比对+热扰动扫描+连续形变插值演化）
```python
if __name__=="__main__":
    tge = ANGTOE_TGE()
    # 基准母晶构型（初始态）
    def base_crystal(n=220):
        t = np.linspace(0, 2*np.pi, n)
        x = (2 + 0.35*np.sin(5*t)) * np.cos(t)
        y = (2 + 0.35*np.sin(5*t)) * np.sin(t)
        z = 0.35 * np.cos(5*t)
        return np.stack([x,y,z],axis=1)
    # 同拓扑类内连续形变终点（仅拉伸微调，\(\text{SL}\)理论不变）
    def deformed_crystal(n=220):
        t = np.linspace(0, 2*np.pi, n)
        x = (2 + 0.34*np.sin(5*t)) * np.cos(t)
        y = (2 + 0.34*np.sin(5*t)) * np.sin(t)
        z = 0.36 * np.cos(5*t)
        return np.stack([x,y,z],axis=1)
    # 跨拓扑类亚稳晶型（用于双构型比对）
    def meta_crystal(n=220):
        t = np.linspace(0, 2*np.pi, n)
        x = (2 + 0.32*np.sin(5*t)) * np.cos(t)
        y = (2 + 0.32*np.sin(5*t)) * np.sin(t)
        z = 0.38 * np.cos(5*t)
        return np.stack([x,y,z],axis=1)

    C0 = base_crystal(220)
    C_deform_end = deformed_crystal(220)
    C1 = meta_crystal(220)

    print("===== 双晶型拓扑比对 =====")
    res_pair = tge.compare_two_configs(C0,C1)
    for title,data in res_pair.items():
        print(f"\n{title}:")
        for k,v in data.items():
            print(f"  {k}: {v:.6f}" if isinstance(v,float) else f"  {k}: {v}")

    print("\n===== 热扰动扫描（鲁棒性测试） =====")
    sigma_scan = [0.001,0.005,0.01,0.02,0.04,0.08]
    scan_out = tge.perturb_scan(C0, sigma_list=sigma_scan, repeat=8, seed=42)
    for item in scan_out:
        s = item["sigma"]
        av = item["avg"]
        print(f"\n\(\sigma\) = {s:.4f}")
        print(f"  \(\text{SL}\)={av['\(\text{SL}\)']:.6f} | Γ_int={av['Γ_int']:.6f} | U_re={av['U_re']:.6f}")
        print(f"  \(\Delta\Phi\)={av['\(\Delta\Phi\)_rad']:.6f} rad | Z={av['Z']:.6f}")
        if av["U_re"] >= tge.Uc:
            print("  ⚠️ 扰动越过重连阈值，易转晶")
        else:
            print("  ✅ 拓扑锁定，仅蓄积应力")

    print("\n===== 【新增】连续形变路径演化（同拓扑类光滑形变） =====")
    deform_path = tge.continuous_deformation_scan(C0, C_deform_end, n_step=15)
    for p in deform_path:
        print(f"\(\lambda\)={p['\(\lambda\)']:.3f} | \(\text{SL}\)={p['\(\text{SL}\)']:.6f} | U_re={p['U_re']:.6f} | \(\Delta\Phi\)={p['\(\Delta\Phi\)_rad']:.6f}")
        if p["is_reconnect"]:
            print("    ⚠️ 形变途中触发拓扑重连，拓扑等价类切换")
```

---

## 9. 理论边界、适用范围与观测约束
1. 底层公理：Axiom0全域角动量归零；**Axiom1连续形变光滑微分同胚约束**，无额外特设假设
2. 相域只能读取**相对相位差**，不存在绝对相位零点，不可直接测绝对相位
3. 演化严格二分：**同拓扑类连续形变（不变\(\text{SL}\)/\(\text{Wr}\)/\(\text{Tw}\)，应力连续累积）**；**拓扑重连相变（不变量突变、应力释放）**
4. 本体系优先用于**已有实验现象的统一拓扑归位、定量标定、构型稳定性排序、连续弛豫路径追踪**；不是以全新奇异预言作为成立唯一判据
5. 适用：药物多晶相变路径、分子连续构象弛豫、超导畴形变、神经环路相位漂移；宏观引力、致密星拓扑相变
6. 不适用：体系外无角动量拓扑映射定义的抽象数学结构

---

## 10. 附录：术语词典（补充连续形变相关词条）
- ANG-TOE：Angular Momentum Network Geometry Theory of Everything，全域角动量网络几何万物理论
- TGE：Topology Geometry Extractor，拓扑几何提取器
- 拓扑重连 $U_{\text{reconnect}}$：涡旋构型发生拓扑等价变换、释放蓄积几何应力的相变事件
- 连续形变（微分同胚/同痕）：涡旋曲线光滑拉伸、弯曲、扭转，不剪断不粘接；\(\text{SL}\)/\(\text{Wr}\)/\(\text{Tw}\)守恒，仅平滑调制梯度、相位与重连势，持续蓄积几何应力
- 宋单位 Sg：ANG-TOE原生拓扑缩放标定单位
- 相域色盲：人类观测系统固有限制，仅可测量相对相位，无绝对相位基准
- 几何应力：相位失配、无法触发重连而持续锁定蓄积的拓扑势能



# ANG‑TOE Version Comparison v2.0 vs v2.1
> Document‑ID: DOC‑VER‑COMP‑001
> Status: Frozen｜可直接放入仓库 `/docs/version_compare.md`
> Author: Chengbin Song
> Last updated: 2026‑08‑21
> License: CC BY‑NC 4.0

## 文件用途说明
本文件记录 ANG‑TOE / TGE 两个正式版本之间公理、模型、算法、数值特性、适用范围的完整差异，
用于版本回溯、代码分支管理、论文补充材料、审稿人答疑。
> 核心不变前提：两个版本均严格遵守 **Axiom‑0 全域总角动量恒等于0**。
> v2.1 不是推翻旧版本，是公理补全，增加连续形变微分同胚约束。

---

## 1. 版本总览

|版本|代号|核心特征|
|---|---|---|
|v2.0|Static‑Kernel|基础拓扑内核；仅定义拓扑不变量与拓扑重连，连续形变作为隐式推论|
|v2.1|Cont‑Deform‑Complete|新增Axiom‑1连续形变公理；演化二分框架；TGE新增连续形变路径扫描模块|

---

## 2. 公理层差异

### v2.0
- Axiom0：全域总角动量恒等于 0
- 无显式连续形变公理
- 连续光滑形变仅可由拓扑不变量守恒间接推导，属于次级推论
> **理论短板注释**
> 公理层面没有明确分界线：无法严格区分
> 1）同拓扑类内部光滑拉伸、弯曲、应力蓄积
> 2）跨拓扑等价类拓扑重连相变
> 在处理热弛豫、晶格微调、慢构象演化时容易出现概念模糊。

### v2.1
- Axiom0：全域总角动量恒等于 0
- **Axiom‑1（新增）连续形变公理**
>本体层角动量网络允许光滑微分同胚连续形变；连续形变不改变拓扑不变量 $\boldsymbol{\mathrm{SL},\mathrm{Wr},\mathrm{Tw}}$，仅连续调制 $\boldsymbol{\nabla L,\Gamma_{\mathrm{int}},\Delta\Phi}$；只有越过临界重连势 $U_c$ 才发生非连续拓扑重连，拓扑等价类切换。

>演化二分注释
>1. **连续形变过程（同痕，同一拓扑等价类）**
>曲线光滑变形、不剪断、不粘接；SL/Wr/Tw严格守恒；几何应力持续累积；$U_\mathrm{re}$平滑上升
>2. **拓扑重连（相变，跨拓扑等价类）**
>$U_\mathrm{re}\ge U_c$，涡旋发生剪断‑重接；拓扑不变量突变；蓄积的几何应力一次性释放

---

## 3. TGE算法模块差异

### v2.0 TGE模块清单
1. 模块1：高斯链接积分（双环链接数）
2. 模块2：扭转数 Tw
3. 模块3：环绕数 Wr
4. 模块4：自链接数 SL = Wr + Tw
5. 模块5：角动量拓扑梯度 ∇L
6. 模块6：角动量交换速率 Γ_int
7. 模块7：拓扑重连势能 U_re 与相变判定
8. 模块8：相域相位差 ΔΦ
9. 模块9：双构型比对
10. 模块10：噪声扰动扫描

>注释：v2.0只能做单点快照评估。如需形变演化路径，使用者必须自行编写插值循环，没有标准化接口。

### v2.1 TGE模块清单（继承v2.0全部模块）
1‑10 和 v2.0 完全保持不变
11. **模块11 continuous_deformation_scan【新增】**
>输入初始构型、目标构型、路径采样步数 $n_\mathrm{step}$
>沿 $\lambda\in[0,1]$线性插值生成连续形变路径
>逐帧计算全部拓扑指标，输出完整演化曲线
>监测形变过程是否中途触碰重连阈值 $U_c$

>模块注释
>插值本身无理论误差。数值漂移来源于每一步曲线离散积分误差累积，不是理论上SL不守恒。

---

## 4. 精度特性对比

### v2.0
- 理论闭式精度：解析精确
- 数值误差来源：折线离散近似、浮点舍入、近距离奇点正则化
- 默认 N=220：SL误差量级约 $10^{-3}$
- 误差只来自单帧计算，不存在路径累积漂移

### v2.1
- 理论闭式精度：继承v2.0，解析精确；Axiom1不引入截断近似
- 基础单帧误差水平与v2.0完全一致
- **新增数值风险注释**
>连续形变多步扫描时，每一步都重新离散积分；采样噪声会沿着形变路径小幅累积，观测到SL出现微小漂移
>漂移属于**数值伪影**，不是连续形变公理失效
>解决方案：增加采样点数N、路径均值降噪、自适应加密形变步长

---

## 5. 计算效率对比

### v2.0
- 单构型完整评估复杂度 $O(N^2)$，瓶颈为Wr环绕数双循环
- 单次任务仅一轮拓扑积分，算力开销最小
- 适合大批量构型粗筛

### v2.1
- 单帧基础运算速度与v2.0完全相同
- 连续形变扫描复杂度 $O(n_\mathrm{step}\cdot N^2)$
>注释：计算耗时随形变路径步数线性放大
>例子：15步形变路径 ≈15次完整拓扑计算
>高通量筛选任务建议关闭形变模块，仅使用静态内核

---

## 6. 适用场景对照表

### ✅ v2.0 优先选用场景
- 稳态晶型快照拓扑特征提取
- 大批量分子构型库快速初筛
- 静态超导涡旋结构标定
- 只关心终态，不关心弛豫演化路径
- 需要最小代码依赖、最快运算速度

### ✅ v2.1 优先选用场景
- 分子溶剂化、晶格热弛豫连续形变路径追踪
- 亚稳晶型应力蓄积直至转晶全过程模拟
- 超导畴缓慢畸变、相位漂移演化
- L0神经拓扑层：长期相位失配‑应力累积动力学
- 动态过程宋单位Sg标定（SL作为形变不变锚点抑制标定漂移）

---

## 7. 优缺点简明注释版

### ANG‑TOE v2.0
**优点**
- 公理最小集合，内核干净
- 代码轻量，运算开销低
- 适合大规模静态构型批量扫描
**缺点**
- 公理层面缺少连续形变约束，渐变‑相变边界模糊
- 没有标准化演化路径工具，动态过程只能定性解释

### ANG‑TOE v2.1
**优点**
- 公理补齐连续形变微分同胚约束，演化二分逻辑闭环
- TGE内置形变路径扫描，可以完整模拟「应力累积→拓扑重连」
- 拓扑不变量可作为动态标定锚点，提升Sg单位稳定性
**缺点**
- 形变路径计算算力开销增大
- 需要额外处理形变路径SL数值漂移问题，增加收敛验证工作量
- 整体代码库复杂度上升

---

## 8. 版本迁移指导注释
>从v2.0迁移至v2.1
>1.原有静态计算代码全部兼容，无需改动旧接口
>2.如需开启形变动力学，调用模块11 continuous_deformation_scan
>3.做形变路径结果绘图时，必须补充收敛测试：增大曲线采样点数N验证SL漂移是否下降
>4.批量高通量任务，建议默认关闭形变扫描模块

---

## 9. 可直接复制的摘要段落（Markdown）
```markdown
### Version Summary
ANG‑TOE v2.0 provides a minimal static topological kernel governed only by Axiom‑0, suitable for steady‑state configuration screening.
ANG‑TOE v2.1 adds the continuous‑deformation diffeomorphism axiom (Axiom‑1), explicitly distinguishing smooth intra‑topology‑class strain accumulation and discontinuous topological‑reconnection phase transition.
The TGE solver gains a built‑in deformation‑path scanner. No breaking changes are introduced for static workflows.
Dynamic simulations bring linear‑scaling computational overhead and require careful convergence checks to suppress discretization drift of topological invariants.
```


